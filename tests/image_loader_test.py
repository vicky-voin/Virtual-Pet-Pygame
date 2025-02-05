import unittest
import os
import pygame
from image_loader import ImageLoader

class ImadeLoaderTests(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((300, 300))
        return super().setUp()

    @unittest.expectedFailure
    def test_wrong_directory(self):
        loader = ImageLoader("wrongDirectory")
        loader.load_image("red_square.png")

    @unittest.expectedFailure
    def test_wrong_name(self):
        loader = ImageLoader(os.path.join("tests","test_images"))
        loader.load_image("wrongName.png")

    def test_correct_directory(self):
        loader = ImageLoader(os.path.join("tests","test_images"))
        square = loader.load_image("red_square.png")

        self.screen.blit(square[0], (0,0))

        pygame.display.flip()

        expected_color = pygame.Color(255,0,0,255)
        actual_color = self.screen.get_at((0,0))

        self.assertEqual(actual_color, expected_color)


if __name__ == '__main__':
    unittest.main()