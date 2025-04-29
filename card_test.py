import pytest
from PyQt5.QtWidgets import QApplication
from memory_cards import MainWindow, TrainingWindow, CreatCardsWindow, ListCardsWindow, StatisticsWindow


@pytest.fixture(scope="session")
def qapp():
    app = QApplication([])
    yield app

@pytest.fixture
def main_window(qapp):
    window = MainWindow()
    yield window

@pytest.fixture
def training_window(main_window):
    window = TrainingWindow(main_window)
    yield window

@pytest.fixture
def create_cards_window(main_window):
    window = CreatCardsWindow(main_window)
    yield window

@pytest.fixture
def list_cards_window(main_window):
    window = ListCardsWindow(main_window)
    yield window

@pytest.fixture
def statistics_window(main_window):
    window = StatisticsWindow(main_window)
    yield window


def test_main_window_initialization(main_window):
    assert main_window.true_answer == 0
    assert main_window.false_answer == 0
    assert main_window.all_cards == {}
