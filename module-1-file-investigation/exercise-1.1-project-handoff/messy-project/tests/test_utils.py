"""Tests for utility functions."""

from src.utils import validate_input, parse_csv_line, format_size

class TestValidateInput:
    def test_none_input(self):
        assert validate_input(None) is False

    def test_empty_dict(self):
        assert validate_input({}) is True

    def test_required_fields_present(self):
        data = {"name": "Alice", "email": "alice@example.com"}
        assert validate_input(data, required=["name", "email"]) is True

    def test_required_fields_missing(self):
        data = {"name": "Alice"}
        assert validate_input(data, required=["name", "email"]) is False

    def test_required_field_empty_string(self):
        data = {"name": "", "email": "alice@example.com"}
        assert validate_input(data, required=["name"]) is False

class TestParseCSVLine:
    def test_simple_line(self):
        result = parse_csv_line("a,b,c")
        assert result == ["a", "b", "c"]

    def test_quoted_fields(self):
        result = parse_csv_line('"hello, world",b,c')
        assert result == ["hello, world", "b", "c"]

    def test_empty_fields(self):
        result = parse_csv_line("a,,c")
        assert result == ["a", "", "c"]

class TestFormatSize:
    def test_bytes(self):
        assert format_size(500) == "500.0 B"

    def test_kilobytes(self):
        assert format_size(2048) == "2.0 KB"

    def test_megabytes(self):
        assert format_size(5 * 1024 * 1024) == "5.0 MB"
