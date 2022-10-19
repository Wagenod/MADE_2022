import unittest

from python_advanced.hw05.game import TicTacGame

class TestTicTacGame(unittest.TestCase):
    game = TicTacGame()

    def test_validate_input(self):
        self.game.field = [[1, 0, ""], ["", "", 0], [1, 1, ""]]

        self.assertFalse(self.game.validate_input("1 e"))
        self.assertFalse(self.game.validate_input("e 1"))
        self.assertFalse(self.game.validate_input("-1 2"))
        self.assertFalse(self.game.validate_input("2 0"))
        self.assertFalse(self.game.validate_input("4 1"))
        self.assertFalse(self.game.validate_input("1 4"))
        self.assertFalse(self.game.validate_input("4 -1"))
        self.assertFalse(self.game.validate_input("-1 4"))
        self.assertFalse(self.game.validate_input("1 1"))
        self.assertFalse(self.game.validate_input("1 2"))
        self.assertTrue(self.game.validate_input("1 3"))

    def test_make_step(self):

        self.game.new_game()

        for i in range(1, self.game.field_size - 1):
            for j in range(1, self.game.field_size - 1):
                self.game.make_step(i - 1, j - 1)
                self.assertEqual(self.game.field[i - 1][j - 1], 
                                    (len(self.game.steps)-1)%2)
                if i == self.game.field_size and j == self.game.field_size -2:
                    self.assertEqual(self.game.winner, 'o')
                else:
                    self.assertIsNone(self.game.winner)
    

    def test_check_winner(self):

        #row 1
        inputs = [(1,1),(2,1),(1,2),(2,2), (1,3)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'o')

        #row 2
        inputs = [(3,1),(2,1),(3,2),(2,2), (1, 3), (2,3)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'x')

        #row 3
        inputs = [(1,1),(3,1),(2,2),(3,2), (1,3), (3, 3)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'x')

        #column 1
        inputs = [(1,1),(1,2),(2,1),(2,2), (3,1)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'o')


        #column 2
        inputs = [(1,1),(1,3),(2,3),(1,2), (3,3), (2, 2), (2, 1), (3, 2)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'x')

        #column 3
        inputs = [(1,3),(1,1),(2,3),(2,2), (3,3)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'o')

        #diag 1
        inputs = [(1,1),(1,2),(2,2),(1,3), (3,3)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'o')


        #diag 2
        inputs = [(1,1),(1,3),(2,1),(2,2), (3,3), (3, 1)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'x')

        #draw
        inputs = [(1,1),(1,2),(2,1),(3,1), (2,2), (3, 3), (1, 3), (2, 3), (3, 2)]
        self.game.new_game()
        for x, y in inputs:
            self.game.make_step(x - 1, y - 1)
        self.assertEqual(self.game.winner, 'draw')
    

if __name__ == "__main__":
    unittest.main()