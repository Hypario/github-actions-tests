import unittest
import math
from src import app

class TestCase(unittest.TestCase):
    
    file = open("tests/example.txt").read().strip()
    times, distances = app.parse_input(file.split("\n"))
    
    time, distance = int(''.join(map(str, times))), int(''.join(map(str, distances)))
    
    def test_part1(self):
        result = math.prod([app.calculate_ways_quadratic(self.times[i], self.distances[i]) for i in range(len(self.times))])
        
        assert result == 288
    
    def test_part2(self):
        result = app.calculate_ways_quadratic(self.time, self.distance)
        assert result == 71503