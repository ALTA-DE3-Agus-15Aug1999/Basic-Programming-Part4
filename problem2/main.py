def draw_xyz(N):
    pattern = ""
    for i in range(1, N*N + 1):
        if i % 3 == 0:
            pattern += "X "
        elif i % 2 == 1:
            pattern += "Y "
        else:
            pattern += "Z "
        if i % N == 0:
            pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """