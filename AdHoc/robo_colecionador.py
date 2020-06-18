class Robo():
    def __init__(self, positionY, positionX, direction):
        self.direction = direction
        self.positionX = positionX
        self.positionY = positionY

    points = 0

    def next_cell(self, position, value):
        if value != '#':
            if value == '*':
                self.points += 1
                self.change_position(position)

                return 1
            else:
                self.change_position(position)

                return position

        return 0

    def change_position(self, position):
        if self.direction == 'O' or self.direction == 'L':
            self.positionX = position
        else:
            self.positionY = position

    def change_direction(self, instruction):
        if self.direction == 'O':
            if instruction == 'D':
                self.direction = 'N'
            else:
                self.direction = 'S'
        elif self.direction == 'L':
            if instruction == 'D':
                self.direction = 'S'
            else:
                self.direction = 'N'
        elif self.direction == 'N':
            if instruction == 'D':
                self.direction = 'L'
            else:
                self.direction = 'O'
        else:
            if instruction == 'D':
                self.direction = 'O'
            else:
                self.direction = 'L'

def check_index(list, index):
    if len(list) <= index or index < 0:
        return False
    return True


def main(n, m, s):

    count = n
    table = []

    while count > 0:
        row = input()
        row_list = []

        for char in row:
            row_list.append(char)

        table.append(row_list)
        count -= 1

    coord = []

    for index_row in range(len(table)):
        for index_column, value in enumerate(table[index_row]):
            if value.isalpha():
                coord.append(index_row)
                coord.append(index_column)
                coord.append(value)

    robo = Robo(coord[0], coord[1], coord[2])

    instructions = input()

    for instruction in instructions:
        if instruction == 'D' or instruction == 'E':
            robo.change_direction(instruction)
        else:
            if robo.direction == 'N':
                y = robo.positionY - 1
                x = robo.positionX

                if check_index(table, y):
                    value = table[y][x]
                    status = robo.next_cell(y, value)

                    if status == 1:
                        table[y][x] = '.'


            elif robo.direction == 'O':
                y = robo.positionY
                x = robo.positionX - 1

                if check_index(table[y], x):
                    value = table[y][x]
                    status = robo.next_cell(x, value)

                    if status == 1:
                        table[y][x] = '.'


            elif robo.direction == 'L':
                y = robo.positionY
                x = robo.positionX + 1

                if check_index(table[y], x):
                    value = table[y][x]
                    status = robo.next_cell(x, value)

                    if status == 1:
                        table[y][x] = '.'

            else:
                y = robo.positionY + 1
                x = robo.positionX

                if check_index(table, y):
                    value = table[y][x]

                    status = robo.next_cell(y, value)

                    if status == 1:
                        table[y][x] = '.'
    
    print(robo.points)


if __name__ == '__main__':

    while True:
        input_data = input()

        n, m, s = input_data.split(' ')

        n = int(n)
        m = int(m)
        s = int(s)

        if n != 0 and m != 0 and s != 0:
            main(n, m, s)
        else:
            break

