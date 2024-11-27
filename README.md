# RuG_IntroToOptimization Package

This repository provides tools for image manipulation and visualization, intended for educational purposes in the field of optimization and computational image processing.

# Installation

To install this package, run the following command:

```bash
pip install RuG_IntroToOptimization
```

# Usage

The following functions and classes are provided through the module:

- `R`: A function that applies blurring to the input image.
- `R_T`: A function that applies the adjoint of the blurring operator to the input image.
- `grad`: A function that computes the discrete gradient of the input image.
- `grad_T`: A function that computes the adjoint of the discrete gradient operator.
- `load_image`: A utility for loading and preprocessing images (resize, grayscale, and array conversion).
- `ImagePlotter`: A class for creating flexible image grids for visualization.

## Description of Functions and Classes

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

### `R_T(image: np.ndarray) -> np.ndarray`

Applies the adjoint of the blurring operator to the input image.

_Parameters_:

- `image` (**np.ndarray**): Input image as a NumPy array.

_Return_:

- `X_blur_T` (**np.ndarray**): Adjoint of the blurring operator applied to input.

### `grad(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]`

Computes the discrete gradient of the input image in the x and y directions.

_Parameters_:

- `image` (**np.ndarray**): Input image as a NumPy array.

_Returns_:

- `X_grad` (**Tuple[np.ndarray]**): Discrete gradient in the x and y direction.

### `grad_T(grad: Tuple[np.ndarray]) -> np.ndarray`

Adjoint of the discrete gradient operator.

_Parameters_:

- `X_grad` (**Tuple[np.ndarray]**): Discrete gradient in the x and y direction.

_Returns_:

- `X_grad_T` (**np.ndarray**): Adjoint discrete gradient operator applied to input.

### `ImagePlotter(rows: int, cols: int)`

A class for creating a grid of images for display. It contains multiples methods.

_Methods_:

- `plot_image(image: np.ndarray, title: str, row: int, col: int)`: Adds an image to the specified grid cell (`row` and `col` are 0-indexed) with a title.
- `show()`: Displays the plotted grid.

## Example Script

To run this example script, you must have a file called `'cat.jpg'` in your file system, at the same location as the script. You may change the filename and path, but the image must remain a `.jpg` file.

```python
from RuG_IntroToOptimization import R, R_T, load_image, ImagePlotter, grad, grad_T

# Load an image
X_ref = load_image('cat.jpg')

# Create an image plotter for a 1x2 grid
plot = ImagePlotter(2, 3)

# Display the original and transformed images
plot.plot_image(X_ref, "Original Image", 0, 0)
plot.plot_image(R(X_ref), "Blurry Image", 0, 1)
plot.plot_image(R_T(X_ref), "Blurry^T Image", 0, 2)
plot.plot_image(grad(X_ref)[0], "Discrete Gradient in X", 1, 0)
plot.plot_image(grad(X_ref)[1], "Discrete Gradient in Y", 1, 1)
plot.plot_image(grad_T(grad(X_ref)), "grad^T(grad(X))", 1, 2)
plot.show()
```

This example produces the following result:

![Resulting Image](https://github.com/DanielCortild/IntroductionToOptimization/blob/main/tests/result.png?raw=true)

Your task will be do deblur the blurred image, and plot the result as above. Obviously, the last three plots are not representative of the original image, but the functions `grad` and `grad_T` will be useful for the implementation.
