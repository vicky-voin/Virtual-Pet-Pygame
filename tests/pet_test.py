import unittest
from pet import Pet

class PetTests(unittest.TestCase):
    def test_setup_pet_success(self):
        pet_instance = Pet.load("tests/test_data/test_pet.json")
        self.assertIsNotNone(pet_instance.type)
        self.assertNotEqual(pet_instance.type, "")

    @unittest.expectedFailure
    def test_setup_pet_wrong_path_fail(self):
        pet_instance = Pet.load("wrongPath")

    @unittest.expectedFailure
    def test_setup_pet_json_mismatch_fail(self):
        pet_instance = Pet.load("tests/test_data/test_pet_corrupted.json")

if __name__ == '__main__':
    unittest.main()