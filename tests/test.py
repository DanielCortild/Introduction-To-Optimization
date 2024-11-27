from RuG_IntroToOptimization import R, R_T, load_image, ImagePlotter, grad, grad_T

# Load an image
X_ref = load_image('cat.jpg')

# Create an image plotter for a 2x3 grid
plot = ImagePlotter(2, 3)

# Display the original and transformed images
plot.plot_image(X_ref, "Original Image", 0, 0)
plot.plot_image(R(X_ref), "Blurry Image", 0, 1)
plot.plot_image(R_T(X_ref), "Blurry^T Image", 0, 2)
plot.plot_image(grad(X_ref)[0], "Discrete Gradient in X", 1, 0)
plot.plot_image(grad(X_ref)[1], "Discrete Gradient in Y", 1, 1)
plot.plot_image(grad_T(grad(X_ref)), "grad^T(grad(X))", 1, 2)
plot.show()
