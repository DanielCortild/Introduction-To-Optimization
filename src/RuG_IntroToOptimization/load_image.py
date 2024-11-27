import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def load_image(image_name, size=(256, 256)) :
    img = Image.open(image_name).resize(size)
    X_ref = np.asarray(ImageOps.grayscale(img)).astype('float32')
    return X_ref

class ImagePlotter:
    def __init__(self, a, b):
        # Store image plotter dimensions
        self.a = a
        self.b = b

        # Create figure
        self.fig, self.axs = plt.subplots(a, b, layout='compressed', dpi=100, figsize=(2*b, 2*a))

        # Store whether a position has been plotted
        self.plotted = [[False for j in range(b)] for i in range(a)]

    def plot_image(self, X, title, i, j):
        # Safety checks
        if i >= self.a or j >= self.b:
            raise ValueError(f"Invalid index. i={i} and j={j} should be strictly less than {self.a} and {self.b} respectively.")
        if i < 0 or j < 0:
            raise ValueError(f"Invalid index. i={i} and j={j} should be non-negative.")
        if type(i) != int or type(j) != int:
            raise ValueError(f"Invalid index. i={i} and j={j} should be integers.")

        # Mark position as plotted
        self.plotted[i][j] = True

        # Retrieve axis
        ax = self.axs[j] if self.a == 1 else self.axs[i, j]

        # Plot image
        ax.imshow(X, cmap='gray', vmin=0, vmax=255)

        # Set title
        ax.title.set_text(title)

        # Deactive axis
        ax.set_axis_off()

    def __plot_blank(self, i, j):
        # Retrieve axis
        ax = self.axs[j] if self.a == 1 else self.axs[i, j]

        # Create blank image
        img_blank = np.zeros((256, 256)) + 255

        # Plot blank image
        ax.imshow(img_blank, cmap='gray', vmin=0, vmax=255)

        # Deactive axis
        ax.set_axis_off()

    def show(self):
        # Plot blank images in non-plotted positions
        for i in range(self.a):
            for j in range(self.b):
                if not self.plotted[i][j]:
                    self.__plot_blank(i, j)

        # Show plot
        plt.tight_layout()
        plt.show()
