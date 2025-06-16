###############
#
# This is your favorite file!
# Write your tests here
#
###############

import pytest
from student import *
from dog import *

def test_from_same_nest():
    assert from_same_nest(luna, max)
    assert not from_same_nest(bella, daisy)
    assert not from_same_nest(rex, bella)
    assert not from_same_nest(rex, rex)

def test_is_pure_breed():
    assert is_pure_breed(rex, "Labrador")
    assert is_pure_breed(max, "Labrador")
    assert is_pure_breed(penny, "Beagle")
    assert is_pure_breed(leo, "German Shepherd")
    assert not is_pure_breed(ruby, "Labrador")
    assert not is_pure_breed(pepper, "Labrador")
    assert is_pure_breed(None, "Labrador")

def test_years_of_birth():
    assert years_of_birth(all_dogs, 2010, 2015) == {2010, 2011, 2012, 2014, 2015}
    assert years_of_birth(all_dogs, 2012, 2017) == {2012, 2014, 2015, 2016, 2017}

def test_years_of_birth_sorted():
    assert years_of_birth_sorted(all_dogs, 2010, 2015) == [2010, 2011, 2012, 2014, 2015]
    assert years_of_birth_sorted(all_dogs, 2012, 2017) == [2012, 2014, 2015, 2016, 2017]

def test_find_dog_names_regex():
    assert find_dog_names_regex(all_dogs) == ['Bella', 'Buddy']