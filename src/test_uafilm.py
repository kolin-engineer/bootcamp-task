import os
from dataclasses import asdict
from pathlib import Path

import pytest

from uafilm import Fieldnames, UAFilm

FILE_PATH = "dummy.csv"
dummy_data = [
    Fieldnames(
        film_name="Котигорошко", note="Мультик, який варто подивиться", rating=5
    ),
    Fieldnames(film_name="Людина Павук", note="Супергероїв кусають", rating=4),
    Fieldnames(film_name="Роксолана", note="Не цікавить", rating=3),
]


@pytest.fixture(scope="module")
def instance():
    yield UAFilm(FILE_PATH)
    # os.remove(FILE_PATH)


def test_new_file_exists(instance: UAFilm):
    assert Path(FILE_PATH).exists()


def test_create_note(instance: UAFilm):
    for note in dummy_data:
        instance.create(**asdict(note))


def test_read_note(instance: UAFilm, capsys):
    instance.read()
    out, err = capsys.readouterr()
    assert dummy_data[0].film_name in out
    assert dummy_data[1].film_name in out
    assert dummy_data[2].film_name in out


def test_update_note(instance: UAFilm, capsys):
    instance.update(
        current_film_name="Роксолана", film_name="Roksolana", note="New NOte", rating=3
    )
    instance.read()
    out, err = capsys.readouterr()
    assert "Роксолана" not in out
    assert "Roksolana" in out


def test_top_rating(instance: UAFilm, capsys):
    instance.get_top_rated()
    out, err = capsys.readouterr()
    assert "5" in out


def test_low_rating(instance: UAFilm, capsys):
    instance.get_low_rated()
    out, err = capsys.readouterr()
    print(out)
    assert "3" in out
