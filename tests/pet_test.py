import unittest
import pygame
import os
from pet import Pet

class PetTests(unittest.TestCase):

    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300

    TEST_IMAGE_WIDTH = 100
    TEST_IMAGE_HEIGHT = 100

    def setUp(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.data_dir = os.path.join("tests","test_data")
        return super().setUp()
    
    def test_setup_pet_success(self):
        pet_instance = Pet.instantiate(os.path.join(self.data_dir,"test_pet.json"))

        self.assertIsNotNone(pet_instance.type)
        self.assertNotEqual(pet_instance.type, "")

        self.assertIsNotNone(pet_instance.sprite)

        self.screen.blit(pet_instance.sprite[0], (0,0))

        pygame.display.flip()

        expected_color = pygame.Color(255,0,0,255)
        actual_color = self.screen.get_at((self.TEST_IMAGE_WIDTH * pet_instance.spriteScale - 1, self.TEST_IMAGE_HEIGHT * pet_instance.spriteScale - 1 ))

        self.assertEqual(actual_color, expected_color)

    @unittest.expectedFailure
    def test_setup_pet_wrong_path_fail(self):
        pet_instance = Pet.instantiate("wrongPath")

    @unittest.expectedFailure
    def test_setup_pet_json_mismatch_fail(self):
        pet_instance = Pet.instantiate(os.path.join(self.data_dir,"test_pet_corrupted.json"))

if __name__ == '__main__':
    unittest.main()