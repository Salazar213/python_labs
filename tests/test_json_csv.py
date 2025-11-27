import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic_conversion(tmp_path):
    """Позитивный тест: корректная конвертация JSON → CSV"""
    src_json = tmp_path / "test.json"
    test_data = [
        {"name": "Alice", "age": 22, "city": "Moscow"},
        {"name": "Bob", "age": 25, "city": "SPb"},
    ]

    src_json.write_text(json.dumps(test_data, ensure_ascii=False), encoding="utf-8")

    dst_csv = tmp_path / "test.csv"
    json_to_csv(str(src_json), str(dst_csv))

    assert dst_csv.exists()

    with open(dst_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == len(test_data)
    assert set(rows[0].keys()) == {"name", "age", "city"}
    assert rows[0]["name"] == "Alice"
    assert rows[0]["age"] == "22"
    assert rows[1]["name"] == "Bob"


def test_csv_to_json_basic_conversion(tmp_path):
    """Позитивный тест: корректная конвертация CSV → JSON"""
    src_csv = tmp_path / "test.csv"

    with open(src_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22", "city": "Moscow"})
        writer.writerow({"name": "Bob", "age": "25", "city": "SPb"})

    dst_json = tmp_path / "test.json"
    csv_to_json(str(src_csv), str(dst_json))

    assert dst_json.exists()

    with open(dst_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert set(data[0].keys()) == {"name", "age", "city"}
    assert data[0]["name"] == "Alice"
    assert data[0]["age"] == "22"
    assert data[1]["name"] == "Bob"


def test_json_to_csv_preserves_all_fields(tmp_path):
    """Тест: все поля сохраняются при конвертации"""
    src_json = tmp_path / "test.json"
    test_data = [
        {"name": "Alice", "age": 22, "city": "Moscow", "email": "alice@test.com"},
        {"name": "Bob", "age": 25, "city": "SPb"},  # Отсутствует email
    ]

    src_json.write_text(json.dumps(test_data, ensure_ascii=False), encoding="utf-8")

    dst_csv = tmp_path / "test.csv"
    json_to_csv(str(src_json), str(dst_csv))

    with open(dst_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert set(rows[0].keys()) == {"name", "age", "city", "email"}
    assert rows[1]["email"] == ""


def test_csv_to_json_preserves_string_values(tmp_path):
    """Тест: значения сохраняются как строки"""
    src_csv = tmp_path / "test.csv"
    with open(src_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "score"])
        writer.writeheader()
        writer.writerow({"id": "001", "name": "Alice", "score": "95.5"})

    dst_json = tmp_path / "test.json"
    csv_to_json(str(src_csv), str(dst_json))

    with open(dst_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data[0]["id"] == "001"
    assert data[0]["name"] == "Alice"
    assert data[0]["score"] == "95.5"


def test_json_to_csv_roundtrip(tmp_path):
    """Тест полного цикла: JSON → CSV → JSON"""
    original_data = [
        {"name": "Alice", "age": 22, "active": True},
        {"name": "Bob", "age": 25, "active": False},
    ]

    json1 = tmp_path / "original.json"
    csv_file = tmp_path / "converted.csv"
    json2 = tmp_path / "final.json"

    json1.write_text(json.dumps(original_data, ensure_ascii=False), encoding="utf-8")
    json_to_csv(str(json1), str(csv_file))
    csv_to_json(str(csv_file), str(json2))

    with open(json2, "r", encoding="utf-8") as f:
        final_data = json.load(f)

    assert len(final_data) == len(original_data)
    assert final_data[0]["name"] == original_data[0]["name"]
    assert final_data[1]["name"] == original_data[1]["name"]


def test_json_to_csv_invalid_json(tmp_path):
    """Негативный тест: некорректный JSON"""
    src_json = tmp_path / "invalid.json"
    src_json.write_text("{invalid json}", encoding="utf-8")

    dst_csv = tmp_path / "output.csv"

    # Ожидаем ошибку, но не проверяем конкретный тип
    with pytest.raises(Exception):
        json_to_csv(str(src_json), str(dst_csv))


def test_json_to_csv_not_list_structure(tmp_path):
    """Негативный тест: JSON не является списком словарей"""
    src_json = tmp_path / "not_list.json"
    src_json.write_text('{"name": "Alice"}', encoding="utf-8")

    dst_csv = tmp_path / "output.csv"

    with pytest.raises(TypeError):
        json_to_csv(str(src_json), str(dst_csv))


def test_json_to_csv_file_not_found():
    """Негативный тест: исходный JSON файл не существует"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


def test_csv_to_json_file_not_found():
    """Негативный тест: исходный CSV файл не существует"""
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


def test_json_to_csv_empty_json_file(tmp_path):
    """Негативный тест: пустой JSON файл"""
    src_json = tmp_path / "empty.json"
    src_json.write_text("[]", encoding="utf-8")  # Пустой массив

    dst_csv = tmp_path / "output.csv"

    with pytest.raises(ValueError):
        json_to_csv(str(src_json), str(dst_csv))


def test_csv_to_json_empty_csv_file(tmp_path):
    """Негативный тест: пустой CSV файл"""
    src_csv = tmp_path / "empty.csv"
    src_csv.write_text("", encoding="utf-8")  # Полностью пустой файл

    dst_json = tmp_path / "output.json"

    with pytest.raises(ValueError):
        csv_to_json(str(src_csv), str(dst_json))
