""" "Tests for the main module."""

from pytest import CaptureFixture

from src.main import main


def test_main(capsys: CaptureFixture) -> None:
    """Test the main function output."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from dev-container-template!\n"
