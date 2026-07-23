import asyncio
from unittest.mock import AsyncMock, patch

import pytest

from bot.game.settlement import settle_game
from bot.strategy.brain import (
    ITEM_PRIORITY,
    WEAPONS,
    WEAPON_PRIORITY,
    calc_damage,
    decide_action,
    get_weapon_bonus,
    get_weapon_range,
    reset_game_state,
)


class FakeMemory:
    def __init__(self):
        self.recorded = []
        self.lessons = []
        self.cleared = 0

    def record_game_end(self, **kwargs):
        self.recorded.append(kwargs)

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def clear_temp(self):
        self.cleared += 1

    async def save(self):
        return None


@pytest.mark.asyncio
async def test_settle_game_records_outcome():
    memory = FakeMemory()
    await settle_game(
        {
            "result": {
                "isWinner": True,
                "finalRank": 1,
                "kills": 5,
                "rewards": {"sMoltz": 120, "moltz": 10},
            }
        },
        "free",
        memory,
    )
    assert memory.recorded[-1]["is_winner"] is True
    assert "Won with 5 kills" in memory.lessons[-1]


@pytest.mark.asyncio
async def test_settle_game_zero_kills_lesson():
    memory = FakeMemory()
    await settle_game(
        {
            "result": {
                "isWinner": False,
                "finalRank": 10,
                "kills": 0,
                "rewards": {},
            }
        },
        "paid",
        memory,
    )
    assert any("Zero kills" in lesson for lesson in memory.lessons)


def test_calc_damage_basic():
    assert calc_damage(10, 10, 10) == 15
    assert calc_damage(10, 0, 0) == 10
    assert calc_damage(1, 0, 100) == 1


def test_calc_damage_weather_penalty():
    base = calc_damage(100, 0, 0, weather="clear")
    storm = calc_damage(100, 0, 0, weather="storm")
    assert int(base * 0.85) == storm


def test_weapon_bonus_and_range_lookups():
    fist = {"typeId": "fist"}
    katana = {"typeId": "katana"}
    assert get_weapon_bonus(fist) == 0
    assert get_weapon_bonus(katana) == 35
    assert get_weapon_range(katana) == 0
    assert get_weapon_range({"typeId": "sniper"}) == 2


def test_decision_waits_when_dead():
    view = {
        "self": {"isAlive": False},
        "currentRegion": {},
        "connectedRegions": [],
        "visibleRegion": [],
        "visibleAgents": [],
        "visibleMonsters": [],
        "visibleItems": [],
        "pendingDeathzones": [],
        "visibleNPCs": [],
        "aliveCount": 100,
        "recentLogs": [],
        "recentMessages": [],
    }
    decide_action(view, can_act=True)


def test_deathzone_escape_priority():
    view = {
        "self": {
            "id": "a1",
            "hp": 80,
            "ep": 10,
            "atk": 10,
            "def": 5,
            "isAlive": True,
            "inventory": [],
            "equippedWeapon": {"typeId": "sword"},
        },
        "currentRegion": {
            "id": "dz-1",
            "isDeathZone": True,
            "terrain": "plains",
            "weather": "clear",
            "connections": [{"id": "safe-1"}],
        },
        "connectedRegions": [{"id": "safe-1"}],
        "visibleRegions": [],
        "visibleAgents": [],
        "visibleMonsters": [],
        "visibleItems": [],
        "pendingDeathzones": [],
        "visibleNPCs": [],
        "aliveCount": 100,
        "recentLogs": [],
        "recentMessages": [],
    }
    action = decide_action(view, can_act=True)
    assert action is not None
    assert action["action"] == "move"
    assert action["data"]["regionId"] == "safe-1"


def test_pickup_moltz_priority():
    view = {
        "self": {
            "id": "a1",
            "hp": 80,
            "ep": 10,
            "maxEp": 10,
            "atk": 10,
            "def": 5,
            "isAlive": True,
            "inventory": [],
            "equippedWeapon": {"typeId": "fist"},
        },
        "currentRegion": {
            "id": "r1",
            "terrain": "plains",
            "weather": "clear",
            "connections": [],
        },
        "connectedRegions": [],
        "visibleRegions": [],
        "visibleAgents": [],
        "visibleMonsters": [],
        "visibleItems": [
            {
                "id": "i1",
                "regionId": "r1",
                "typeId": "rewards",
                "category": "currency",
            }
        ],
        "pendingDeathzones": [],
        "visibleNPCs": [],
        "aliveCount": 100,
        "recentLogs": [],
        "recentMessages": [],
    }
    action = decide_action(view, can_act=True)
    assert action is not None
    assert action["action"] == "pickup"


def test_healing_priority_critical():
    view = {
        "self": {
            "id": "a1",
            "hp": 20,
            "ep": 10,
            "maxEp": 10,
            "atk": 10,
            "def": 5,
            "isAlive": True,
            "inventory": [
                {"id": "m1", "typeId": "medkit"},
                {"id": "b1", "typeId": "bandage"},
            ],
            "equippedWeapon": {"typeId": "fist"},
        },
        "currentRegion": {
            "id": "r1",
            "terrain": "plains",
            "weather": "clear",
            "connections": [],
        },
        "connectedRegions": [],
        "visibleRegions": [],
        "visibleAgents": [],
        "visibleMonsters": [],
        "visibleItems": [],
        "pendingDeathzones": [],
        "visibleNPCs": [],
        "aliveCount": 100,
        "recentLogs": [],
        "recentMessages": [],
    }
    action = decide_action(view, can_act=True)
    assert action is not None
    assert action["action"] == "use_item"
    assert action["data"]["itemId"] == "m1"
