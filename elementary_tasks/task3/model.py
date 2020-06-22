from math import sqrt


class Triangle:
    
    def __init__(self, triangle_name, first_side, second_side, third_side):
        self.triangle_name = triangle_name
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

        self.half_perimeter = (self.first_side + self.second_side + self.third_side)/2
        self.triangle_square = round(sqrt(self.half_perimeter*(self.half_perimeter-self.first_side)*(self.half_perimeter-self.second_side)*(self.half_perimeter-self.third_side)),2)

        # self.triangle_name_and_triangle_square_dict = dict()

    # def square_Heron_formula(self):
    #     triangle_square = round(sqrt(self.half_perimeter*(self.half_perimeter-self.first_side)*(self.half_perimeter-self.second_side)*(self.half_perimeter-self.third_side)),2)
    #     return triangle_square

    # def add_triangle_name_and_triangle_square(self):
    #     self.triangle_name_and_triangle_square_dict[self.triangle_name] = self.triangle_square





