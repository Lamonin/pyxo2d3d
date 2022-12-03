class Field:
    def __init__(self):
        self.field = [[['_'] * 3 for _ in range(3)] for _ in range(3)]

    def __str__(self):
        str_field = str()
        for plane in self.field:
            for line in plane:
                for cell in line:
                    str_field += cell + " "
                str_field += "\n"
            str_field += "\n"
        return str_field

    def __repr__(self):
        return self.__str__()

    def try_set_cell(self, x, y, z, letter):
        if self.try_get_cell(x, y, z) is None or self.field[y][x][z] != '_':
            return False
        self.field[y][x][z] = letter
        return True

    def check_win_for_cell(self, x, y, z):
        for t_x in range(-1, 2):
            for t_y in range(-1, 2):
                for t_z in range(-1, 2):
                    if t_x != 0 or t_y != 0 or t_z != 0:
                        c_x = x + t_x
                        c_y = y + t_y
                        c_z = z + t_z

                        cell = self.try_get_cell(c_x, c_y, c_z)
                        k = 0

                        while cell is not None and self.field[y][x][z] == cell:
                            k += 1
                            c_x += t_x
                            c_y += t_y
                            c_z += t_z
                            cell = self.try_get_cell(c_x, c_y, c_z)

                        if k == 2:
                            return True
        return False

    def try_get_cell(self, x, y, z):
        if x < 0 or y < 0 or z < 0 or x > len(self.field) - 1 or y > len(self.field) - 1 or z > len(self.field) - 1:
            return None
        return self.field[y][x][z]


def play():
    game_field = Field()
    cur_letter = 'X'

    print(game_field)
    print("Ход", cur_letter)
    user_input = input("Введите координаты в формате y,x,z: ")

    while user_input != "exit":
        coord = user_input.split(' ')
        user_y = int(coord[0])
        user_x = int(coord[1])
        user_z = int(coord[2])

        if not game_field.try_set_cell(user_x, user_y, user_z, cur_letter):
            print("Некорректные координаты! Попробуйте снова!")
        else:
            print(game_field)
            if game_field.check_win_for_cell(user_x, user_y, user_z):
                print("Победил X!")
                break
            cur_letter = 'X' if cur_letter == 'O' else 'O'
        print("Ход", cur_letter)
        user_input = input("Введите координаты в формате y,x,z: ")