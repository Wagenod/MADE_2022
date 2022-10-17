from lib2to3.pygram import Symbols


class TicTacGame:

    TIC_TAC_MAPPING = {0:'o', 1: 'x'} 

    def __init__(self, dim=3) -> None:
        self.__field = [[" ", " ", " "] for _ in range(0, dim)]
        self.last_step = 0 # who done last step 

    def show_board(self):
        for row in self.__field:
            for item in row:
                print(self.TIC_TAC_MAPPING[item], end=" ")
            print("\n")

    def validate_input(self, x, y):
        if self.__field[x][y]:
            return False
        return True

    def show_input_msg(self):
        return 'Your turn {}. \
                Select empty cell position, \
                please'.format(self.TIC_TAC_MAPPING[self.last_step])

    def show_validation_msg():
        print("You selected busy cell. \n \
            Please, select vacant cell again.")
    

    def start_game(self):
        while True:
            game_over = self.check_winner()
            if game_over:
                return self.TIC_TAC_MAPPING[self.last_step]
            
            print('\n =================== \n')
            self.last_step = (self.last_step + 1)%2
            self.show_board()
            pos_x, pos_y = [int(x) - 1 for x in input(self.show_input_msg()).split(" ")]
            
            is_valid = self.validate_input(pos_x, pos_y)
            if not is_valid:
                self.show_validation_msg()
                self.last_step = (self.last_step + 1)%2
            else:
                self.__field[pos_x][pos_y] = self.last_step + 1 # чтобы было 1 и 2 в матрице
            

    def check_winner(self):
        """
        Shifts begin:
        - rows starts with 0
        - cols starts with 0 + dim
        - diags starts with 0 + 2*dim 
        """

        counter = []

        n_items = len(self.__field)
        for i in range(n_items):
            for j in range(n_items):
                item = self.__field[i][j]
                if item:
                    counter[i] += item
                    counter[j + n_items] += item
                    if i == j:
                        counter[2*n_items] += item
                    elif i + j == 2:
                        counter[2*n_items + 1] += item
        
        for el in counter:
            if el == 3 or el == 6:
                return True
        
        return False



if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()