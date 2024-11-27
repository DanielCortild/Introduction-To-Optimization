from RuG_IntroToOptimization import R, load_image, ImagePlotter, grad, grad_T

# Load an image
X_ref = load_image('cat.jpg')

# Create an image plotter for a 1x2 grid
plot = ImagePlotter(1, 5)

# Display the original and transformed images
plot.plot_image(X_ref, "Original Image", 0, 0)
plot.plot_image(R(X_ref), "Blurry Image", 0, 1)
plot.plot_image(grad(X_ref)[0], "Discrete Gradient in X", 0, 2)
plot.plot_image(grad(X_ref)[1], "Discrete Gradient in Y", 0, 3)
plot.plot_image(grad_T(grad(X_ref)), "grad^T(grad(X))", 0, 4)
plot.show()
