import xo2d
import unittest


class XO2DCase(unittest.TestCase):
    def setUp(self):
        self.game_field = xo2d.Field()

    def test_check_win_1(self):
        self.game_field.try_set_cell(0, 0, "X")
        self.game_field.try_set_cell(1, 0, "X")
        self.game_field.try_set_cell(2, 0, "X")

        result = self.game_field.check_win_for_cell(0, 0)
        result = result and self.game_field.check_win_for_cell(1, 0)
        result = result and self.game_field.check_win_for_cell(2, 0)

        self.assertEqual(result, True)

    def test_check_win_2(self):
        self.game_field.try_set_cell(0, 0, "X")
        self.game_field.try_set_cell(1, 1, "X")
        self.game_field.try_set_cell(2, 2, "X")

        result = self.game_field.check_win_for_cell(0, 0)
        result = result and self.game_field.check_win_for_cell(1, 1)
        result = result and self.game_field.check_win_for_cell(2, 2)

        self.assertEqual(result, True)

    def test_check_win_3(self):
        self.game_field.try_set_cell(2, 0, "X")
        self.game_field.try_set_cell(1, 1, "X")
        self.game_field.try_set_cell(0, 2, "X")

        result = self.game_field.check_win_for_cell(2, 0)
        result = result and self.game_field.check_win_for_cell(1, 1)
        result = result and self.game_field.check_win_for_cell(0, 2)

        self.assertEqual(result, True)
