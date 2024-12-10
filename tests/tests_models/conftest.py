from datetime import date

import pytest

from src.models.person import Person


@pytest.fixture
def adult():
    """Fixture for an adult Person instance."""
    return Person(firstname="Zoé", name="Michel", birth=date(1990, 5, 15), city="Paris")


@pytest.fixture
def minor():
    """Fixture for a Person instance representing a minor."""
    return Person(firstname="Jacques", name="Simon", birth=date(2020, 8, 23), city="Rome")


@pytest.fixture
def elder():
    """Fixture for a Person instance representing an elderly person."""
    return Person(firstname="Pichet", name="Josiane", birth=date(1951, 3, 16), city="Paris")

@pytest.fixture
def person_list(adult, minor, elder):
    """Fixture for a list of Person instances."""
    return [adult, minor, elder]
