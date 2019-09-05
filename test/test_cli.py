from click.testing import CliRunner
from ServerCheck.cli import ping_servers


def test_ping_servers():
    # Test that the command can be called without error
    runner = CliRunner()
    command_result = runner.invoke(ping_servers)
    assert command_result.exit_code == 0


