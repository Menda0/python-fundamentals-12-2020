import unittest
from unittest import TestCase
from session6_inheritance import Dog


class TestAnimals(TestCase):

    ## Test if dog is dog
    def test_if_dog_is_dog(self):
        dog = Dog()

        ## dog.name == "Dog"
        self.assertEqual(dog.name, "Dog")

    ## Test if snake is snake
    def test_if_snake_is_snake(self):
        pass

    ## Test if duck is duck
    def test_if_duck_is_duck(self):
        pass

    ## Test if animals can walk
    def test_if_animals_can_walk(self):
        dog = Dog()

        expected_output = "Dog start walking"
        output = dog.walks()

        self.assertEqual(output, expected_output)


if __name__ ==  '__main__':
    unittest.main()

# Execute the coverage of test
# coverage run -m unittest discover
# Give the report of coverage of test
# coverage report -m
# Generates an html document with the coverage test
# coverage html
