from src.utils import Count 

def euclidean_distance(point1, point2):
    sum_of_squares = 0
    for i in range(len(point1)):
        Count.incC(2)
        sum_of_squares += (point1[i] - point2[i]) ** 2
    return math.sqrt(sum_of_squares)