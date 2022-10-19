import random


class TicTacGame:

    TIC_TAC_MAPPING = {0:'o', 1: 'x'} 

    def __init__(self, size=3) -> None:
        self.field_size = size
        self.new_game()

    def new_game(self):
        self.__field = [[""]*self.field_size for _ in range(0, self.field_size)]
        #len(self.steps) = 0 # who done last step
        self.winner = None
        self.winner_counter = [-self.field_size**2]*(2*self.field_size + 2)
        self.steps = []
        self.game_over = False

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, vals):
        if vals:
            self.__field = vals
        else:
            self.__field = [[""]*self.field_size for _ in range(0, self.field_size)]
        
    def show_board(self):
        #print('=======')
        sep_coef = self.field_size*2
        print('='*sep_coef)
        for row in self.field:
            print("|", end="")
            for item in row:
                print(self.TIC_TAC_MAPPING.get(item, " "), end="|")
            print('\n', '='*sep_coef)
    

    def make_step(self, x, y):
        self.field[x][y] = len(self.steps)%2
        self.steps.append((x, y))
        self.check_winner()


    def validate_input(self, input_str):
        x, y = input_str.split(" ")
        try:
            x, y = int(x), int(y)
        except ValueError as err:
            print("Field indexes must be int ! {}".format(err.args))
            return False
        
        if x*y <= 0:
            print("Indexes can`t be <= 0.")
            return False
        
        if x > self.field_size or y > self.field_size:
            print("Indexes can`t be grather than {}.".format(self.field_size))
            return False

        if isinstance(self.field[x - 1][y - 1], int):
            print("You chose busy cell. Please, select vacant cell.")
            return False
        
        return True
   

    def start_game(self):
        while self.winner is None and (len(self.steps) < self.field_size**2):
            print('\nYour turn player {}'.format(self.TIC_TAC_MAPPING[len(self.steps)%2]))
            self.show_board()

            input_cmd = input()
            while not self.validate_input(input_cmd):
                input_cmd = input()
            x, y = [int(pos) - 1 for pos in input_cmd.split(" ")]
            
            self.make_step(x, y)
        return self.winner


    def check_winner(self):
        """
        Shifts begin:
        - rows starts with 0
        - cols starts with 0 + dim
        - diags starts with 0 + 2*dim 
        """

        i, j = self.steps[-1]
        el = self.field[i][j]
        if isinstance(el, int):
            delta = el + self.field_size
            self.winner_counter[i] += delta
            self.winner_counter[j + self.field_size] += delta
            if i == j:
                self.winner_counter[2*self.field_size] += delta
            if (i + j) == 2:
                self.winner_counter[2*self.field_size + 1] += delta

        for el in self.winner_counter:
            if el == 0 or el == 3:
                self.winner = self.TIC_TAC_MAPPING[el//3]
                return True
        
        if len(self.steps) == self.field_size**2:
            self.winner = "draw"
            return True

        return False



if __name__ == "__main__":
    game = TicTacGame()
    winner = game.start_game()
    print(winner)