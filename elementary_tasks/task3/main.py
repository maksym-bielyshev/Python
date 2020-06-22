from elementary_tasks.task3.model import *


def new_triangle():
    triangle_name = input('Enter triangle name: ')
    triangle_first_side = float(input('Enter first side: '))
    triangle_second_side = float(input('Enter second side: '))
    triangle_third_side = float(input('Enter third side: '))
    return Triangle(triangle_name, triangle_first_side, triangle_second_side, triangle_third_side)


def main():
    choice_to_add_new_triangle = 'y'
    all_data = dict()

    while choice_to_add_new_triangle.lower() == 'y':
        triangle = new_triangle()
        all_data[triangle.triangle_name] = triangle.triangle_square
        choice_to_add_new_triangle = input('Do you want to add a new triangle? -> ')

    all_data = {k: v for k, v in sorted(all_data.items(), key=lambda item: item[0], reverse=True)}
    print(all_data)


if __name__ == '__main__':
    main()
