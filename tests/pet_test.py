import unittest
from pet import Pet

class PetTests(unittest.TestCase):
    def test_setup_pet_success(self):
        pet_instance = Pet.load("tests/test_data/test_pet.json")
        self.assertIsNotNone(pet_instance.petType)

if __name__ == '__main__':
    unittest.main()