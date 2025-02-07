import unittest
import os
import pygame
from image_loader import ImageLoader

class ImadeLoaderTests(unittest.TestCase):

    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300

    TEST_IMAGE_WIDTH = 100
    TEST_IMAGE_HEIGHT = 100

    def setUp(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        return super().setUp()

    @unittest.expectedFailure
    def test_wrong_directory(self):
        loader = ImageLoader("wrongDirectory")
        loader.load_image("red_square.png")

    @unittest.expectedFailure
    def test_wrong_name(self):
        loader = ImageLoader(os.path.join("tests","test_data"))
        loader.load_image("wrongName.png")

    def test_correct_directory(self):
        loader = ImageLoader(os.path.join("tests","test_data"))
        square = loader.load_image("red_square.png", -1)                                                                                                      

        self.screen.blit(square[0], (0,0))

        pygame.display.flip()

        expected_color = pygame.Color(255,0,0,255)
        actual_color = self.screen.get_at((0,0))

        self.assertEqual(actual_color, expected_color)

    def test_image_scaled_up(self):
        test_scale = 3
        loader = ImageLoader(os.path.join("tests","test_data"))
        square = loader.load_image("red_square.png", -1,test_scale)

        self.screen.blit(square[0], (0,0))

        pygame.display.flip()

        expected_color = pygame.Color(255,0,0,255)
        actual_color = self.screen.get_at((self.TEST_IMAGE_WIDTH * test_scale - 1, self.TEST_IMAGE_HEIGHT * test_scale - 1 ))

        self.assertEqual(actual_color, expected_color)

        self.assertEqual(square[1].height, 300)
        self.assertEqual(square[1].width, 300)


if __name__ == '__main__':
    unittest.main()