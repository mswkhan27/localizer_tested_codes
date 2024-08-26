class TriangleType:
    
    @staticmethod
    def display_type_code(n):
        if n:
            return n
    
    @staticmethod
    def is_side_two_equal_three(type_code):
        if type_code >= 0:
            type_code = type_code + 3  
        return type_code
    
    @staticmethod
    def is_side_one_equal_two(type_code):
        if type_code >= 0:
            type_code = type_code + 1
        return type_code
    
    @staticmethod
    def is_side_one_equal_three(type_code):
        if type_code >= 0:
            type_code = type_code + 2
        return type_code
    
    def trityp(self, i, j, k):
        if i == 0 or j == 0 or k == 0:
            type_code = 3
        else:
            type_code = 0
            if i == j:
                type_code = self.is_side_one_equal_two(type_code)
            if i == k:
                type_code = self.is_side_one_equal_three(type_code)
            if j == k:
                type_code = self.is_side_two_equal_three(type_code)
            if type_code == 0:
                if (i + j <= k) or (j + k <= i) or (i + k <= j):
                    type_code = 4
                else:
                    type_code = 1
            elif type_code > 3:
                type_code = 3
            elif (type_code == 1) and (i + j > k):
                type_code = self.display_type_code(2)
            elif (type_code == 2) and (i + k > j):
                type_code = self.display_type_code(2)
            elif (type_code == 3) and (j + k > i):
                type_code = self.display_type_code(2)
            else:
                type_code = self.display_type_code(4)
        
        return type_code
    
    def process_input(self, sides):
        i, j, k = sides
        result = self.trityp(i, j, k)
        print(f"{result}")

triangle = TriangleType()

inputs = [
  (12, 10,10),

]

for sides in inputs:
    triangle.process_input(sides)
