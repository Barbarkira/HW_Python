import numpy as np

def rand_mean(N: int) -> float:
    random_vector = np.random.rand(N)
    mean_value = np.mean(random_vector)
    return mean_value

mean_value_of_array_size_10 = rand_mean(10)
print(f"Mean value of random array of size 10: {mean_value_of_array_size_10}")

def print_checkerboard():
    checkerboard = np.zeros((8, 8), dtype=int)
    checkerboard[1::2, ::2] = 1
    checkerboard[::2, 1::2] = 1

    for row in checkerboard:
        print(' '.join(map(str, row)))

print("Checkerboard pattern:")
print_checkerboard()


#### 3. Print the minimum and maximum representable value for each numpy scalar type
def min_max_repr():
    print("NumPy Scalar Types Min and Max Values:")

    for dtype in [np.int8, np.int16, np.int32, np.int64]:
        min_val = np.iinfo(dtype).min
        max_val = np.iinfo(dtype).max
        print(f"{dtype.__name__}: Min = {min_val}, Max = {max_val}")

    for dtype in [np.float32, np.float64]:
        min_val = np.finfo(dtype).min
        max_val = np.finfo(dtype).max
        print(f"{dtype.__name__}: Min = {min_val}, Max = {max_val}")

min_max_repr()


#### 4. How to get the n largest values of an array?
def n_largest(n: int) -> np.ndarray:
    A = np.arange(10000)
    np.random.shuffle(A)
    indices = np.argpartition(A, -n)[-n:]
    largest_values = A[indices]
    largest_values.sort()
    return largest_values
result = n_largest(5)
print(f"The 5 largest values are: {result}")

def compute_in_place():
    A = np.ones(3) * 1
    B = np.ones(3) * 2

    A += B

    A *= -0.5

    print(f"Final result in A: {A}")
compute_in_place()