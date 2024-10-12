import pytest

from src.tui import HelloApp


@pytest.mark.asyncio
async def test_initial_state():
    """Test that the initial state of the app is correct."""
    app = HelloApp()

    async with app.run_test() as pilot:
        assert app.screen.get_widget_by_id("name_input").value == ""
        assert "Submit" in app.screen.get_widget_by_id("submit_button").label
        assert app.screen.get_widget_by_id("greeting_output").renderable == ""
