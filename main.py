import generation

if __name__ == '__main__':
    grid = generation.grid_gen.Sudoku()
    grid.hash_gen()
    grid.mark_gen()
    grid.print_grid()
    grid.fill_grid()

