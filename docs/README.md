Here is a sample README file explaining how to use the program:

---

# Pixel Drawer

This is a simple Python script that allows you to draw pixels on a 32x32 grid using various colors. The grid is represented in the terminal, with colored blocks representing pixels. When you're done drawing, the program generates 8086 assembly code that reproduces your drawing.

## How to use

Run the Python script in your terminal. You will see an empty 32x32 grid. You can set a pixel's color by entering its coordinates (x and y values) and a color code, separated by spaces. Here is an example:

```
Enter x, y and color to set a pixel (x y color), or 'q' to quit: 5 5 7
```

This will set the pixel at coordinates (5,5) to white. The updated grid will be printed to the terminal immediately.

To quit the program and generate the assembly code, simply enter 'q' at the prompt:

```
Enter x, y and color to set a pixel (x y color), or 'q' to quit: q
```

## Color codes

The color codes and their corresponding colors are as follows:

- '0': Black
- '1': Blue
- '2': Green
- '3': Cyan
- '4': Red
- '5': Magenta
- '6': Brown
- '7': White
- '8': Gray
- '9': Light Blue
- 'a': Light Green
- 'b': Light Cyan
- 'c': Light Red
- 'd': Light Magenta
- 'e': Yellow
- 'f': Bright White

Please note that the actual colors displayed may depend on your terminal's color scheme.

---