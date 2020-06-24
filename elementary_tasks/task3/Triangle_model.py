class InvalidDataError(Exception):
    pass


class Triangle:
    def __init__(self, name, *sides):
        self.name = name
        self.sides = sides

        self.half_perimeter = sum(sides) / 2
        area_without_pow = self.half_perimeter
        for side in self.sides:
            area_without_pow *= (self.half_perimeter - side)
        self.area = round(pow(area_without_pow, 0.5), 2)

    @classmethod
    def is_valid(cls, *triangle_data):
        """ Is the triangle valid """
        perimeter = sum(triangle_data[1:])
        for side in triangle_data[1:]:
            sum_two_sides = perimeter - side
            if sum_two_sides <= side:
                raise InvalidDataError('Invalid data for creating Triangle.')
        return cls(*triangle_data)


def get_data_from_user():
    while True:
        try:
            triangle_name = (input('Triangle name: '))
            triangle_first_side = float(input('1st side: '))
            triangle_second_side = float(input('2nd side: '))
            triangle_third_side = float(input('3rd side: '))
        except ValueError as error:
            print('Error: {}.'.format(error))
        else:
            return triangle_name, triangle_first_side, triangle_second_side, triangle_third_side


def main():
    choice_to_add_new_triangle = 'y'
    triangles_list = list()

    while choice_to_add_new_triangle == 'y' or choice_to_add_new_triangle == 'yes':
        try:
            triangle_data = get_data_from_user()
            triangle = Triangle.is_valid(*triangle_data)
        except InvalidDataError as error:
            print(error)
            choice_to_add_new_triangle = input('Do you want to add a new triangle? -> ')
        else:
            print('Good!')
            triangles_list.append(triangle)
            choice_to_add_new_triangle = input('Do you want to add a new triangle? -> ')

    if triangles_list:
        result = sorted(triangles_list, key=lambda x: x.area, reverse=True)
        print('========Triangles list========')
        for res in result:
            print('[Triangle {}]: {}cm'.format(res.name, res.area))


if __name__ == '__main__':
    main()
