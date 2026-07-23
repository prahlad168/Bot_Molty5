import json
from pathlib import Path
from unittest.mock import patch

import pytest

from app.core.gaurangga_bridge import (
    AuditTrail,
    ConsolidatedStatus,
    DigitalCore,
    DISTRIBUTION,
    EnterpriseHub,
    GauranggaCommandBridge,
    SyncResult,
    load_json,
    save_json,
)


ROOT = Path(__file__).resolve().parents[1]
FAKE_CFG = ROOT / "tests" / "fixtures" / "config.json"
FAKE_REV = ROOT / "tests" / "fixtures" / "revenue.json"


def _write_fixtures(tmp_path: Path):
    cfg = tmp_path / "config.json"
    rev = tmp_path / "revenue.json"
    cfg.write_text(
        json.dumps(
            {
                "companies": [
                    {
                        "id": "C1",
                        "name": "TestCo",
                        "target_monthly": 1000000,
                        "current_revenue": 250000,
                    }
                ],
                "ceo": {"name": "CEO"},
                "destination": {},
            }
        ),
        encoding="utf-8",
    )
    rev.write_text(
        json.dumps({"transactions": [{"amount_idr": 500000}]}),
        encoding="utf-8",
    )
    return cfg, rev


def test_load_json_returns_empty_when_missing(tmp_path: Path):
    missing = tmp_path / "nope.json"
    assert load_json(missing) == {}


def test_save_json_creates_parents(tmp_path: Path):
    target = tmp_path / "a" / "b" / "x.json"
    save_json(target, {"ok": True})
    assert target.exists()
    assert json.loads(target.read_text(encoding="utf-8")) == {"ok": True}


def test_enterprise_hub_revenue_calculation(tmp_path: Path):
    cfg, _ = _write_fixtures(tmp_path)
    with patch("app.core.gaurangga_bridge.CONFIG_FILE", cfg), patch(
        "app.core.gaurangga_bridge.REVENUE_FILE", tmp_path / "revenue.json"
    ), patch(
        "app.core.gaurangga_bridge.AUDIT_FILE", tmp_path / "audit.json"
    ), patch(
        "app.core.gaurangga_bridge.REPORTS_DIR", tmp_path / "reports"
    ), patch(
        "app.core.gaurangga_bridge.SCRIPT_DIR", tmp_path
    ):
        hub = EnterpriseHub()
        ledger = tmp_path / "ledger.json"
        ledger.write_text(
            json.dumps({"entries": [{"amount": 100000}, {"amount": 200000}]}),
            encoding="utf-8",
        )
        with patch.object(hub, "offline_ledger_file", ledger):
            with patch.object(hub, "wire_tracking_file", tmp_path / "wt.json"):
                with patch.object(hub, "procurement_file", tmp_path / "proc.json"):
                    assert hub.calculate_offline_revenue() == 300000


def test_digital_core_revenue_calculation(tmp_path: Path):
    cfg, rev = _write_fixtures(tmp_path)
    with patch("app.core.gaurangga_bridge.CONFIG_FILE", cfg), patch(
        "app.core.gaurangga_bridge.REVENUE_FILE", rev
    ), patch("app.core.gaurangga_bridge.SCRIPT_DIR", tmp_path):
        core = DigitalCore()
        assert core.calculate_digital_revenue() == 500000


def test_bridge_consolidated_status_has_correct_distribution(tmp_path: Path):
    cfg, rev = _write_fixtures(tmp_path)
    with patch("app.core.gaurangga_bridge.CONFIG_FILE", cfg), patch(
        "app.core.gaurangga_bridge.REVENUE_FILE", rev
    ), patch(
        "app.core.gaurangga_bridge.AUDIT_FILE", tmp_path / "audit.json"
    ), patch(
        "app.core.gaurangga_bridge.REPORTS_DIR", tmp_path / "reports"
    ), patch(
        "app.core.gaurangga_bridge.SCRIPT_DIR", tmp_path
    ):
        bridge = GauranggaCommandBridge()
        ledger = tmp_path / "ledger.json"
        ledger.write_text(
            json.dumps({"entries": [{"amount": 100000}]}), encoding="utf-8"
        )
        with patch.object(bridge.enterprise_hub, "offline_ledger_file", ledger):
            with patch.object(bridge.enterprise_hub, "wire_tracking_file", tmp_path / "wt.json"):
                with patch.object(bridge.enterprise_hub, "procurement_file", tmp_path / "proc.json"):
                    status = bridge.get_consolidated_status()
        assert status.distribution == {
            "ceo_share_percent": DISTRIBUTION["ceo_share_percent"],
            "ops_share_percent": DISTRIBUTION["ops_share_percent"],
        }
        assert status.total_revenue == pytest.approx(600000.0)
        assert status.ceo_share == pytest.approx(480000.0)
        assert status.ops_share == pytest.approx(120000.0)


def test_sync_result_serializes():
    result = SyncResult(
        success=True,
        message="ok",
        timestamp="2026-01-01T00:00:00",
        entries_processed=2,
        audit_log_id="ABC",
        daily_report_path="/tmp/r.md",
    )
    data = result.__dict__
    assert data["success"] is True
    assert data["entries_processed"] == 2


def test_audit_trail_logs_and_retrieves(tmp_path: Path):
    audit_file = tmp_path / "audit.json"
    audit_file.write_text(
        json.dumps({"execution_log": [], "metadata": {}}), encoding="utf-8"
    )
    with patch("app.core.gaurangga_bridge.AUDIT_FILE", audit_file):
        trail = AuditTrail()
        aid = trail.log_entry("TEST", {"x": 1})
        assert isinstance(aid, str)
        assert len(aid) > 0
        logs = trail.get_recent_logs(limit=5)
        assert len(logs) == 1
        assert logs[0]["action"] == "TEST"
