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
        test_need = Need(startLevel, coolDown, "Test")

        self.assertEqual(test_need.remainingTimeTillCritical, 0)
        self.assertEqual(test_need.fulfillPercentage, 0)

        startLevel = 0.5
        coolDown = 3
        test_need = Need(startLevel, coolDown, "Test")

        self.assertEqual(test_need.remainingTimeTillCritical, 1.5)
        self.assertEqual(test_need.fulfillPercentage, 0.5)

        startLevel = 1
        coolDown = 0.5
        test_need = Need(startLevel, coolDown, "Test")

        self.assertEqual(test_need.remainingTimeTillCritical, 0.5)
        self.assertEqual(test_need.fulfillPercentage, 1)

    def test_fulfill_need_resets_cooldown(self):
        startLevel = 1
        coolDown = 5
        test_need = Need(startLevel, coolDown, "Test")

        test_need.fulfill()

        self.assertEqual(test_need.remainingTimeTillCritical, 5)
        self.assertEqual(test_need.fulfillPercentage, 1)

    def test_need_degrades_over_time(self):
        startLevel = 1
        coolDown = 5
        test_need = Need(startLevel, coolDown, "Test")

        test_need.update(2)
        test_need.update(3)

        self.assertEqual(test_need.remainingTimeTillCritical, 0)
        self.assertEqual(test_need.fulfillPercentage, 0)

        test_need.fulfill()
        test_need.update(1)

        self.assertEqual(test_need.remainingTimeTillCritical, 4)
        self.assertEqual(test_need.fulfillPercentage, 0.8)

        
if __name__ == '__main__':
    unittest.main()