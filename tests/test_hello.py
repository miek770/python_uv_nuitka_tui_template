from click.testing import CliRunner, Result
import pytest
from app.hello import main


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_main_hello(runner: CliRunner):
    result: Result = runner.invoke(main, ["Michel"])
    assert result.exit_code == 0
    assert "Hello Michel!" in result.output
