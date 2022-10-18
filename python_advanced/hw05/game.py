from cmath import inf
from lib2to3.pygram import Symbols


class TicTacGame:

    TIC_TAC_MAPPING = {0:'o', 1: 'x'} 

    def __init__(self, dim=3) -> None:
        self.__field = [[""]*dim for _ in range(0, dim)]
        self.n_steps = 0 # who done last step
        self.winner = None

    def show_board(self):
        print('=======')
        for row in self.__field:
            print("|", end="")
            for item in row:
                print(self.TIC_TAC_MAPPING.get(item, " "), end="|")
            print('\n=======')

    def validate_input(self, x, y):
        if isinstance(self.__field[x][y], int):
            return False
        return True

    def show_input_msg(self):
        return 'Your turn {} \n'.format(self.TIC_TAC_MAPPING[self.n_steps%2])

    def show_validation_err_msg(self):
        print("You selected busy cell. Please, select vacant cell again. \n")
    

    def start_game(self):
        while not self.check_winner() and (self.n_steps < len(self.__field)**2):
            print('\nYour turn {}'.format(self.TIC_TAC_MAPPING[self.n_steps%2]))
            self.show_board()
            pos_x, pos_y = [int(x) - 1 for x in input().split(" ")]
            while not self.validate_input(pos_x, pos_y):
                self.show_validation_err_msg()
                pos_x, pos_y = [int(x) - 1 for x in input().split(" ")]

            self.__field[pos_x][pos_y] = self.n_steps%2
            self.n_steps += 1

        
        if self.winner:
            return self.TIC_TAC_MAPPING[(self.n_steps - 1)%2]
        return "draw"

    def check_winner(self):
        """
        Shifts begin:
        - rows starts with 0
        - cols starts with 0 + dim
        - diags starts with 0 + 2*dim 
        """
        
        n_items = len(self.__field)
        counter = [-n_items**2]*(2*n_items + 2)
        for i in range(n_items):
            for j in range(n_items):
                el = self.__field[i][j]
                if isinstance(el, int):
                    counter[i] += el
                    counter[j + n_items] += el
                    if i == j:
                        counter[2*n_items] += el
                    if (i + j) == 2:
                        counter[2*n_items + 1] += el
        print(counter)
        for el in counter:
            if el == 0 or el == 3:
                self.winner = self.TIC_TAC_MAPPING[el//3]
                return True
        
        return False



if __name__ == "__main__":
    game = TicTacGame()
    winner = game.start_game()
    print(winner)