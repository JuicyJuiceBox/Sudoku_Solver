from backend import generation as gen


if __name__ == '__main__':
    grid = gen.grid_gen.Grid()
    grid.hash_gen()
    print(grid.hash_check)
