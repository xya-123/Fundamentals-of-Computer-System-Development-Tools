import pytest
from greetlab.cli import main


def test_main_normal(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "25060012033"])
    main()
    out, _ = capsys.readouterr()
    assert out.strip() == "Hello, 25060012033!"


def test_main_blank_name(monkeypatch):
    # name只有空格、空白字符，预期SystemExit(2)
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
