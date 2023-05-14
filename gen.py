pixel_grid = [[' ' for _ in range(32)] for _ in range(32)]

def print_grid(grid):
    for row in grid:
        for pixel in row:
            print(pixel, end='')
        print()

def set_pixel(x, y, color):
    if 0 <= x < 32 and 0 <= y < 32:
        pixel_grid[y][x] = color
    else:
        print("Invalid coordinates. Please enter numbers between 0 and 31.")

while True:
    print_grid(pixel_grid)

    user_input = input("Enter x, y and color to set a pixel (x y color), or 'q' to quit: ")
    if user_input.lower() == 'q':
        break

    try:
        x, y, color = user_input.split()
        x, y = int(x), int(y)
        set_pixel(x, y, color)
    except ValueError:
        print("Invalid input. Please enter two numbers and a color symbol separated by spaces, or 'q' to quit.")
