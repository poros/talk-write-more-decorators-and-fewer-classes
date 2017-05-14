import pytest


@pytest.fixture
def widget():
    Widget('The widget')


def test_default_widget_size(widget):
    assert widget.size() == (50, 50), 'incorrect default size'


def test_widget_resize(widget):
    widget.resize(100, 150)
    assert widget.size() == (100, 150), 'wrong size after resize'
