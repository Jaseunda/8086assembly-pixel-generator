from colorama import Fore, Style, init
init(autoreset=True)

pixel_grid = [[' ' for _ in range(32)] for _ in range(32)]

COLOR_CODES = {
    '0': Fore.BLACK + '◼',      # Black
    '1': Fore.BLUE + '◼',       # Blue
    '2': Fore.GREEN + '◼',      # Green
    '3': Fore.CYAN + '◼',       # Cyan
    '4': Fore.RED + '◼',        # Red
    '5': Fore.MAGENTA + '◼',    # Magenta
    '6': Fore.YELLOW + '◼',     # Brown
    '7': Fore.WHITE + '◼',      # White
    '8': Fore.LIGHTBLACK_EX + '◼',  # Gray
    '9': Fore.LIGHTBLUE_EX + '◼',   # Light Blue
    'a': Fore.LIGHTGREEN_EX + '◼',  # Light Green
    'b': Fore.LIGHTCYAN_EX + '◼',   # Light Cyan
    'c': Fore.LIGHTRED_EX + '◼',    # Light Red
    'd': Fore.LIGHTMAGENTA_EX + '◼',  # Light Magenta
    'e': Fore.LIGHTYELLOW_EX + '◼',  # Yellow
    'f': Fore.LIGHTWHITE_EX + '◼',   # Bright White
}

def print_grid(grid):
    for row in grid:
        for pixel in row:
            print(pixel, end='')
        print()

def set_pixel(x, y, color):
    if 0 <= x < 32 and 0 <= y < 32:
        pixel_grid[y][x] = COLOR_CODES.get(color, ' ')
    else:
        print("Invalid coordinates. Please enter numbers between 0 and 31.")

def generate_assembly_code(grid):
    assembly_code = []

    assembly_code.append("""
mov ax, 0013h
int 10h
""")

    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            if pixel != ' ':
                color_code = list(COLOR_CODES.keys())[list(COLOR_CODES.values()).index(pixel)]
                assembly_code.append(f"""
mov ah, 0Ch
mov al, {color_code}h
mov cx, {x}
mov dx, {y}
int 10h
""")

    assembly_code.append("""
mov ax, 0003h
int 10h
""")
    return "\n".join(assembly_code)

while True:
    print_grid(pixel_grid)

    user_input = input("Enter x, y and color to set a pixel (x y color), or 'q' to quit: ")
    if user_input.lower() == 'q':
        assembly_code = generate_assembly_code(pixel_grid)
        print(assembly_code)
        break

    try:
        x, y, color = user_input.split()
        x, y = int(x), int(y)
        set_pixel(x, y, color)
    except ValueError:
        print("Invalid input. Please enter two numbers and a color code separated by spaces, or 'q' to quit.")
