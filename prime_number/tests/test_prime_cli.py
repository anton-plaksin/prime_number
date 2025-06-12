import sys
import os
import pytest

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prime_cli import main


def run_cli(args, monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['prime_cli.py'] + args)
    main()
    return capsys.readouterr().out.strip()


def test_cli_prime(monkeypatch, capsys):
    assert run_cli(['17'], monkeypatch, capsys) == '17 is prime'


def test_cli_non_prime(monkeypatch, capsys):
    assert run_cli(['18'], monkeypatch, capsys) == '18 is not prime'
