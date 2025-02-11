import unittest
from pet import Need

class NeedTests(unittest.TestCase):

    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300

    TEST_IMAGE_WIDTH = 100
    TEST_IMAGE_HEIGHT = 100
    
    def test_need_remaining_time_correct(self):
        startLevel = 0
        coolDown = 5
        test_need = Need(startLevel, coolDown)

        self.assertEqual(test_need.remainingTime, coolDown)

        startLevel = 0.5
        coolDown = 3
        test_need = Need(startLevel, coolDown)

        self.assertEqual(test_need.remainingTime, 1.5)

        startLevel = 1
        coolDown = 0.5
        test_need = Need(startLevel, coolDown)

        self.assertEqual(test_need.remainingTime, 0)

        
if __name__ == '__main__':
    unittest.main()