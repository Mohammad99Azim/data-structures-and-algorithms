from Animal_Shelter.AnimalShelter import AnimalShelter, NodeAnimal
import pytest


def test_expected_outcome_1():
    dog1 = NodeAnimal("dog", "dogOne")
    q = AnimalShelter()
    q.enqueue(dog1)
    assert q.front.type == "dog"


def test_dequeue(new_shelter):
    actual = new_shelter.dequeue('cat')
    expected = "cat"
    assert actual == expected


def test_enqueue(new_shelter):
    dogee = NodeAnimal("dog", "dogee")
    new_shelter.enqueue(dogee)
    assert new_shelter.rare.name == "dogee"


def test_raises_exception():
    q = AnimalShelter()
    with pytest.raises(Exception) as e:
        q.dequeue('cat')
    assert repr(e) == '<ExceptionInfo Exception("Can\'t dequeue The AnimalShelter is Empty") tblen=2>'


def test_edge_cases(new_shelter):
    cat3 = NodeAnimal("cat", "cat3")
    no_type1 = NodeAnimal("noType1", "noName1")
    no_type2 = NodeAnimal("noType2", "noName2")

    new_shelter.enqueue(cat3)
    assert new_shelter.rare.name == "cat3"

    new_shelter.enqueue(no_type1)
    assert new_shelter.rare.name == "noName1"

    new_shelter.enqueue(no_type2)
    assert new_shelter.rare.name == "noName2"

    new_shelter.dequeue("noTy")
    assert new_shelter.rare.name == "noName2"

@pytest.fixture
def new_shelter():
    dog1 = NodeAnimal("dog", "dogOne")
    dog2 = NodeAnimal("dog", "dog2")
    dog3 = NodeAnimal("dog", "dog3")
    cat1 = NodeAnimal("cat", "cat1")
    cat2 = NodeAnimal("cat", "cat2")
    cat3 = NodeAnimal("cat", "cat3")
    no_type1 = NodeAnimal("noType1", "noName1")
    no_type2 = NodeAnimal("noType2", "noName2")

    q = AnimalShelter()

    q.enqueue(dog1)
    q.enqueue(dog2)
    q.enqueue(dog3)

    q.enqueue(cat1)
    q.enqueue(cat2)
    q.enqueue(cat3)

    q.enqueue(no_type1)
    q.enqueue(no_type2)

    return q
