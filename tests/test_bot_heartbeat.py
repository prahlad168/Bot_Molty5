from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bot.heartbeat import Heartbeat
from bot.state_router import (
    IN_GAME,
    NO_IDENTITY,
    READY_FREE,
)


@pytest.mark.asyncio
async def test_heartbeat_stops_on_keyboard_interrupt():
    heartbeat = Heartbeat()
    creds = {"api_key": "k", "agent_name": "a"}
    with patch("bot.heartbeat.ensure_account_ready", AsyncMock(return_value=creds)), patch(
        "bot.heartbeat.MoltyAPI", MagicMock()
    ) as mock_api:
        api_instance = MagicMock()
        api_instance.get_accounts_me = AsyncMock()
        api_instance.close = AsyncMock()
        mock_api.return_value = api_instance
        with patch.object(heartbeat, "_heartbeat_cycle", AsyncMock()) as cycle_mock:
            cycle_mock.side_effect = KeyboardInterrupt()
            with patch("bot.heartbeat.AgentMemory", autospec=True):
                await heartbeat.run()
    assert heartbeat.running is False


@pytest.mark.asyncio
async def test_heartbeat_retries_account_setup_on_none():
    heartbeat = Heartbeat()
    call_count = 0

    async def fake_ensure():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            await asyncio_sleep_mock()
            return None
        return {"api_key": "k", "agent_name": "a"}

    asyncio_sleep_mock = AsyncMock()

    with patch("bot.heartbeat.ensure_account_ready", fake_ensure), patch(
        "asyncio.sleep", asyncio_sleep_mock
    ), patch("bot.heartbeat.MoltyAPI", MagicMock()) as mock_api, patch(
        "bot.heartbeat.AgentMemory", autospec=True
    ), patch(
        "bot.heartbeat.dashboard_state", MagicMock()
    ), patch(
        "bot.heartbeat.load_credentials", return_value={}
    ):
        api_instance = MagicMock()
        api_instance.get_accounts_me = AsyncMock()
        api_instance.close = AsyncMock()
        mock_api.return_value = api_instance
        with patch.object(heartbeat, "_heartbeat_cycle", AsyncMock()) as cycle_mock:
            async def fake_cycle():
                raise KeyboardInterrupt()
            cycle_mock.side_effect = fake_cycle
            await heartbeat.run()


@pytest.mark.asyncio
async def test_heartbeat_routes_ready_free_to_join():
    heartbeat = Heartbeat()
    creds = {"api_key": "k", "agent_name": "a"}
    with patch("bot.heartbeat.ensure_account_ready", AsyncMock(return_value=creds)), patch(
        "bot.heartbeat.MoltyAPI", MagicMock()
    ) as mock_api, patch("bot.heartbeat.AgentMemory", autospec=True), patch(
        "bot.heartbeat.dashboard_state", MagicMock()
    ), patch("bot.heartbeat.load_credentials", return_value=creds):
        api_instance = MagicMock()
        api_instance.get_accounts_me = AsyncMock()
        api_instance.close = AsyncMock()
        mock_api.return_value = api_instance
        with patch.object(heartbeat, "_heartbeat_cycle", AsyncMock()) as cycle_mock:
            calls = [
                {"state": NO_IDENTITY},
                {"state": READY_FREE},
                KeyboardInterrupt(),
            ]

            async def fake_cycle():
                item = calls.pop(0)
                if isinstance(item, dict):
                    with patch("bot.heartbeat.determine_state", return_value=(item["state"], {})):
                        pass
                    return None
                raise item

            cycle_mock.side_effect = fake_cycle
            await heartbeat.run()
    assert heartbeat.running is False


@pytest.mark.asyncio
async def test_heartbeat_consecutive_backoff_increases():
    heartbeat = Heartbeat()
    creds = {"api_key": "k", "agent_name": "a"}
    with patch("bot.heartbeat.ensure_account_ready", AsyncMock(return_value=creds)), patch(
        "bot.heartbeat.MoltyAPI", MagicMock()
    ) as mock_api:
        api_instance = MagicMock()
        api_instance.close = AsyncMock()
        mock_api.return_value = api_instance
        with patch("bot.heartbeat.AgentMemory", autospec=True), patch(
            "bot.heartbeat.dashboard_state", MagicMock()
        ), patch("bot.heartbeat.load_credentials", return_value=creds):
            attempts = 0
            wait_times = []

            async def fake_cycle():
                nonlocal attempts
                attempts += 1
                raise RuntimeError("fail")

            async def fake_sleep(duration):
                wait_times.append(duration)
                if len(wait_times) >= 3:
                    heartbeat.running = False

            with patch.object(heartbeat, "_heartbeat_cycle", AsyncMock(side_effect=fake_cycle)), patch(
                "asyncio.sleep", fake_sleep
            ):
                await heartbeat.run()
    assert attempts >= 2
    assert wait_times[0] == 10
    assert wait_times[1] == 20
