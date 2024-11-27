# RuG_IntroToOptimization Package

This repository provides tools for image manipulation and visualization, intended for educational purposes in the field of optimization and computational image processing.

# Installation

To install this package, run the following command:

```bash
pip install RuG_IntroToOptimization
```

# Usage

## Importing the Module

The following functions and classes are provided through the module:

- `R`: A function that applies a transformation (e.g., blurring) to the input image.
- `load_image`: A utility for loading and preprocessing images (resize, grayscale, and array conversion).
- `ImagePlotter`: A class for creating flexible image grids for visualization.

## Functions

### `load_image(filename: str) -> np.ndarray`

Loads an image, resizes it, converts it to grayscale, and returns the processed image as a NumPy array.
_Parameters_:

- `filename` (**str**): The path to the image file.

_Returns_:

- `X_ref` (**np.ndarray**): Processed image array.

### `R(image: np.ndarray) -> np.ndarray`

Applies a blurring effect or other specified transformation to the input image.
_Parameters_:

- `image` (**np.ndarray**): Input image as a NumPy array.

_Returns_:

- `X_blur` (**np.ndarray**): Transformed image array.

### `ImagePlotter(rows: int, cols: int)`

A class for creating a grid of images for display.
_Methods_:

- `plot_image(image: np.ndarray, title: str, row: int, col: int)`: Adds an image to the specified grid cell (`row` and `col` are 0-indexed) with a title.
- `show()`: Displays the plotted grid.

## Example Script

To run this example script, you must have a file called `'cat.jpg'` in your file system, at the same location as the script. You may change the filename and path, but the image must remain a `.jpg` file.

```python
from RuG_IntroToOptimization import R, load_image, ImagePlotter

# Load an image
X_ref = load_image('cat.jpg')

# Create an image plotter for a 1x2 grid
plot = ImagePlotter(1, 2)

# Display the original and transformed images
plot.plot_image(X_ref, "Original Image", 0, 0)
plot.plot_image(R(X_ref), "Blurry Image", 0, 1)
plot.show()
```

This example produces the following result:

![Resulting Image](https://github.com/DanielCortild/IntroductionToOptimization/blob/main/tests/result.png?raw=true)

Your task will be do deblur the blurred image, and plot the result as above.
