import numpy as np

def generate_random_numbers(num_points):
    return np.random.rand(num_points)

def calculate_statistics(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    std_dev = np.std(numbers)
    return mean, median, std_dev

if __name__ == "__main__":
    num_points = 1000  # Size of the random number list
    numbers = generate_random_numbers(num_points)
    mean, median, std_dev = calculate_statistics(numbers)
    print(f"Generated {num_points} random numbers")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
