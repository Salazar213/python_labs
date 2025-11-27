import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# Тесты для normalize
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
        ("ЁЖИК-ЁЖ", "ежик-еж"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


def test_normalize_without_yo2e():
    result = normalize("ёжик", yo2e=False)
    assert "ё" in result


# Тесты для tokenize
@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("!!!", []),
        ("word1 word2-word3", ["word1", "word2-word3"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


# Тесты для count_freq
def test_count_freq_basic():
    tokens = ["a", "b", "a", "c", "b", "a"]
    result = count_freq(tokens)
    expected = {"a": 3, "b": 2, "c": 1}
    assert result == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_count_freq_single_word():
    assert count_freq(["test"]) == {"test": 1}


def test_count_freq_case_sensitive():
    tokens = ["Word", "word", "WORD"]
    result = count_freq(tokens)
    assert result["Word"] == 1
    assert result["word"] == 1
    assert result["WORD"] == 1


# Тесты для top_n
def test_top_n_basic():
    freq = {"a": 3, "b": 2, "c": 1}
    result = top_n(freq, 2)
    expected = [("a", 3), ("b", 2)]
    assert result == expected


def test_top_n_tie_breaker():
    freq = {"bb": 2, "aa": 2, "cc": 1}
    result = top_n(freq, 2)
    expected = [("aa", 2), ("bb", 2)]
    assert result == expected


def test_top_n_more_than_available():
    # Запрашиваем больше элементов, чем есть
    freq = {"a": 3, "b": 2}
    result = top_n(freq, 5)
    expected = [("a", 3), ("b", 2)]
    assert result == expected
