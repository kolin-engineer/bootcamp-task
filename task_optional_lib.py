import csv
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class Fieldnames:
    film_name: str = ""
    note: str = ""
    rating: str | int = 1


class UAFilm:
    __dump: Any = []
    _fieldnames = (
        "film_name",
        "note",
        "rating",
    )
    _rating = range(1, 5)

    def __init__(self, path_to_csv: str | Path = "uafilms.csv") -> None:
        self.path_to_csv: str | Path = path_to_csv
        # If file doesn't exist create and write headers
        if not Path(path_to_csv).exists():
            with open(path_to_csv, "w") as fs:
                csv.DictWriter(fs, fieldnames=self._fieldnames).writeheader()
        return

    def _get_reader(self):
        with open(self.path_to_csv, "r") as f:
            yield from csv.DictReader(f, self._fieldnames)
        return

    def __make_dump(self) -> None:
        self._dump = [line for line in self._get_reader()]

    def create(self, **new_note: Any):
        "Add note to csv"
        self.__make_dump()
        self.__dump.append(asdict(Fieldnames(**new_note)))
        with open(self.path_to_csv, "w") as f:
            writer = csv.DictWriter(f, self._fieldnames)
            writer.writeheader()
            writer.writerows(self.__dump)

    def read(self):
        [print(line) for line in self._get_reader()]

    def update(self, current_film_name: str, **new_note: Any):
        "Update note in csv by film_name"
        self.__make_dump()
        with open(self.path_to_csv, "w") as f:
            writer = csv.DictWriter(f, self._fieldnames)
            for note in self._dump:
                if note.get("film_name") == current_film_name:
                    note = asdict(Fieldnames(**new_note))
                writer.writerow(note)

    def delete(self, film_name_to_del: str):
        "Remove note from csv"
        self.__make_dump()
        with open(self.path_to_csv, "w") as f:
            writer = csv.DictWriter(f, self._fieldnames)
            for note in self._dump:
                if note.get("film_name") == film_name_to_del:
                    continue
                writer.writerow(note)

    def get_top_rated(self):
        "Get top rated note"
        self.__make_dump()
        if self.__dump:
            print(sorted(self.__dump, key=lambda x: x["rating"], reverse=True)[0])

    def get_low_rated(self):
        "Get low rated note"
        self.__make_dump()
        if self.__dump:
            print(sorted(self.__dump, key=lambda x: x["rating"])[0])

    def get_avg_rating(self):
        "Get avg rating among all films"
        self.__make_dump()
        if self.__dump:
            print(sum([x["rating"] for x in self.__dump]) / len(self.__dump))


lib = UAFilm()
lib.create(film_name="adsff1", note="asfadfaf", rating=2)
lib.create(film_name="adsff2", note="asfadfaf", rating=2)
lib.create(film_name="adsff3", note="asfadfaf", rating=2)
lib.create(film_name="adsff4", note="asfadfaf", rating=5)
lib.update(
    current_film_name="adsff3",
    film_name="adsff3asdfasdfasfd",
    note="asfadfaf",
    rating=4,
)
lib.delete(film_name_to_del="adsff1")
lib.read()

lib.get_top_rated()
lib.get_low_rated()
lib.get_avg_rating()
