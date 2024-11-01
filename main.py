def mirrored_right_angled_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('*' * i)
height = 5
mirrored_right_angled_triangle(height)
