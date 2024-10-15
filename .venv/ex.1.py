def sorted_squares(digits):
    squares = [x ** 2 for x in digits]
    squares.sort()
    return squares
digits = [5, 2, 3]

sorted_squares_out = sorted_squares(digits)
print(sorted_squares_out)

