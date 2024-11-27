from RuG_IntroToOptimization import R, load_image, ImagePlotter

# Load an image
X_ref = load_image('cat.jpg')

# Create an image plotter for a 1x2 grid
plot = ImagePlotter(1, 2)

# Display the original and transformed images
plot.plot_image(X_ref, "Original Image", 0, 0)
plot.plot_image(R(X_ref), "Blurry Image", 0, 1)
plot.show()
