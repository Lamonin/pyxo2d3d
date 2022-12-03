class Field:
    def __init__(self):
        self.field = [['_'] * 3 for _ in range(3)]

    def __str__(self):
        str_field = str()
        for line in self.field:
            for cell in line:
                str_field += str(cell) + " "
            str_field += "\n"
        return str_field

    def __repr__(self):
        return self.__str__()

    def try_set_cell(self, x, y, letter):
        if self.try_get_cell(x, y) is None or self.field[y][x] != '_':
            return False
        self.field[y][x] = letter
        return True

    def check_win_for_cell(self, x, y):
        for t_x in range(-1, 2):
            for t_y in range(-1, 2):
                if t_x != 0 or t_y != 0:
                    c_x = x + t_x
                    c_y = y + t_y

                    cell = self.try_get_cell(c_x, c_y)
                    k = 0

                    while cell is not None and self.field[y][x] == cell:
                        k += 1
                        c_x += t_x
                        c_y += t_y
                        cell = self.try_get_cell(c_x, c_y)

                    if k == 2:
                        return True
        return False

    def try_get_cell(self, x, y):
        if x < 0 or y < 0 or x > len(self.field) - 1 or y > len(self.field) - 1:
            return None
        return self.field[y][x]


def play():
    game_field = Field()
    cur_letter = 'X'

    print(game_field)
    print("Ход", cur_letter)
    user_input = input("Введите координаты в формате x,y: ")

    while user_input != "exit":
        coord = user_input.split(' ')
        user_x = int(coord[0])
        user_y = int(coord[1])

        if not game_field.try_set_cell(user_x, user_y, cur_letter):
            print("Некорректные координаты! Попробуйте снова!")
        else:
            print(game_field)
            if game_field.check_win_for_cell(user_x, user_y):
                print("Победил X!")
                break
            cur_letter = 'X' if cur_letter == 'O' else 'O'
        print("Ход", cur_letter)
        user_input = input("Введите координаты в формате x,y: ")