
import pytest
from homework_11 import QuestRoom

def test_init():
    room = QuestRoom("Island", 3, 2)
    assert room.name == "Island"
    assert room.difficulty == 3
    assert room.limit == 2
    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log == []


def test_add_player_success():
    room = QuestRoom("Island", 3, 2)
    room.add_player("Oleg")
    assert "Oleg" in room.players
    assert room.events_log[-1] == "Player Oleg joined"

def test_add_player_full():
    room = QuestRoom("Island", 3, 1)
    room.add_player("Oleg")
    result = room.add_player("Dasha")
    assert result == "No free slots!"
    assert len(room.players) == 1


def test_remove_player_exists():
    room = QuestRoom("Island", 3, 2)
    room.add_player("Oleg")
    room.remove_player("Oleg")
    assert "Oleg" not in room.players
    assert room.events_log[-1] == "Player Oleg left"

def test_remove_player_missing():
    room = QuestRoom("Island", 3, 2)
    result = room.remove_player("Unknown")
    assert result == "Player not found!"


def test_is_full_and_free_slots():
    room = QuestRoom("Island", 3, 2)
    assert room.free_slots() == 2
    assert not room.is_full()
    room.add_player("P1")
    room.add_player("P2")
    assert room.is_full()
    assert room.free_slots() == 0


def test_start_empty():
    room = QuestRoom("Island", 3, 2)
    assert room.start() == "Room is empty!"
    assert room.status == "waiting"

def test_start_with_players():
    room = QuestRoom("Island", 3, 2)
    room.add_player("Oleg")
    result = room.start()
    assert "started with 1 players" in result
    assert room.status == "active"
    assert "Quest started" in room.events_log


def test_reset_room():
    room = QuestRoom("Island", 3, 2)
    room.add_player("Oleg")
    room.start()
    room.reset_room()
    assert room.players == []
    assert room.status == "waiting"
    assert "Room reset" in room.events_log


def test_complex_scenario():
    room = QuestRoom("Matrix", 5, 2)
    room.add_player("Neo")
    room.add_player("Trinity")
    assert room.is_full()
    room.start()
    assert room.status == "active"
    room.reset_room()
    assert len(room.players) == 0
    assert room.free_slots() == 2
    assert "Player Neo joined" in room.show_log()