import math

def parse_input(lines: list[str]):
    times = [int(time) for time in lines[0].split(":")[1].split()]
    distances = [int(duration) for duration in  lines[1].split(":")[1].split()]
    
    return times, distances

def calculate_ways_quadratic(time: int, distance: int) -> int:
    def f(x):
        return x * (time - x)
    # we're looking for x * (time - x) - distance = 0, quadratic is : -x^2 + time * x - distance = 0, we solving a simple quadratic formula
    # solutions = (-b +/- sqrt(b**2 - 4ac)) / 2a
    solutions = [
         ( (-time + math.sqrt((time ** 2) - (4 * distance))) // -2 ), # delta = b^2 - 4ac
        ( (-time - math.sqrt((time ** 2) - (4 * distance))) // -2 )  
    ]
    # the interval includes x * (time - x) - distance = 0, you have to add 1 to the first, the last you might have equals, so remove one
    first, last = int(solutions[0] + 1), int(solutions[1])
    
    if f(last) == distance: last = last - 1
    return abs(last - first + 1)

def main():
    file = open("src/input.txt").read().strip()
    times, distances = parse_input(file.split("\n"))
    time, distance = int(''.join(map(str, times))), int(''.join(map(str, distances)))
    
    print("part 1")
    print(math.prod([calculate_ways_quadratic(times[i], distances[i]) for i in range(len(times))]))
    
    print("part 2")
    print(calculate_ways_quadratic(time, distance))