import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.stats import norm

# Set the seed for reproducibility
np.random.seed(61)

# Generate 5 random data points from a Gaussian with mean 0 and std 6.0
data = np.random.normal(0, 6.0, 5)

print(f"mean is {np.mean(data)}")


# Define the Gaussian curve function
def gaussian_curve(x, mu, sigma):
    return norm.pdf(x, mu, sigma)


# Define the likelihood function
def likelihood(mu, sigma, data):
    return np.prod(norm.pdf(data, mu, sigma))


# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(0, 0.25)
ax.set_xlabel("X")
ax.set_ylabel("Probability Density")
ax.set_title("Likelihood as Mu Changes")

# Plot the data points
ax.scatter(data, np.zeros_like(data), color="red", zorder=5)
for i, y in enumerate(data):
    ax.annotate(
        f"${y:.2f}$", (y, 0), textcoords="offset points", xytext=(0, 5), ha="center"
    )

# Line for the Gaussian curve
x = np.linspace(-10, 10, 500)
(gaussian_line,) = ax.plot([], [], "b-", lw=2)

# Vertical lines from data points to the Gaussian curve
vlines = [ax.plot([], [], "g--")[0] for _ in data]

# Text to show the likelihood values and total likelihood
likelihood_texts = [ax.text(0, 0, "", fontsize=9, color="black") for _ in data]
total_likelihood_text = ax.text(-5, 0.22, "", fontsize=12, color="blue")


# Initialization function
def init():
    gaussian_line.set_data([], [])
    for vline in vlines:
        vline.set_data([], [])
    for text in likelihood_texts:
        text.set_text("")
    total_likelihood_text.set_text("")
    return [gaussian_line] + vlines + likelihood_texts + [total_likelihood_text]


# Update function
def update(frame):
    mu = -3 + frame * 0.2  # Changing mu from -3 to 3
    sigma = 2.0  # Fixed standard deviation

    # Plot the Gaussian curve
    y_vals = gaussian_curve(x, mu, sigma)
    gaussian_line.set_data(x, y_vals)

    # Plot the vertical lines and annotate likelihood values
    total_likelihood = 1
    for i, (y, vline, text) in enumerate(zip(data, vlines, likelihood_texts)):
        # Gaussian curve height at the data points
        y_gaussian = gaussian_curve(y, mu, sigma)

        # Update vertical lines
        vline.set_data([y, y], [0, y_gaussian])

        # Annotate likelihood values
        text.set_text(f"{y_gaussian:.4f}")
        text.set_position((y, y_gaussian + 0.005))

        # Update total likelihood
        total_likelihood *= y_gaussian

    # Update total likelihood annotation
    total_likelihood_text.set_text(f"Likelihood: {total_likelihood:.3e}, mean: {mu:.2}")

    return [gaussian_line] + vlines + likelihood_texts + [total_likelihood_text]


# Create the animation
# Create the animation object as before
ani = FuncAnimation(
    fig, update, frames=int((3 - (-3)) / 0.2), init_func=init, blit=True, interval=200
)

# Save the animation as a GIF file
# ani.save("likelihood_animation.gif", writer="pillow", fps=5)


# Show the animation
plt.show()


# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(0, 0.45)
ax.set_xlabel("X")
ax.set_ylabel("Probability Density")
ax.set_title("Likelihood as Sigma Changes")

# Plot the data points
ax.scatter(data, np.zeros_like(data), color="red", zorder=5)
for i, y in enumerate(data):
    ax.annotate(
        f"${y:.2f}$", (y, 0), textcoords="offset points", xytext=(0, 5), ha="center"
    )

# Line for the Gaussian curve
x = np.linspace(-10, 10, 500)
(gaussian_line,) = ax.plot([], [], "b-", lw=2)

# Vertical lines from data points to the Gaussian curve
vlines = [ax.plot([], [], "g--")[0] for _ in data]

# Text to show the likelihood values and total likelihood
likelihood_texts = [ax.text(0, 0, "", fontsize=9, color="black") for _ in data]
total_likelihood_text = ax.text(-5, 0.38, "", fontsize=12, color="blue")


# Initialization function
def init2():
    gaussian_line.set_data([], [])
    for vline in vlines:
        vline.set_data([], [])
    for text in likelihood_texts:
        text.set_text("")
    total_likelihood_text.set_text("")
    return [gaussian_line] + vlines + likelihood_texts + [total_likelihood_text]


# Update function
def update2(frame):
    mu = 1.5253  # Fixed mean
    sigma = 1 + frame * 0.1  # Changing sigma from 1 to 10

    # Plot the Gaussian curve
    y_vals = gaussian_curve(x, mu, sigma)
    gaussian_line.set_data(x, y_vals)

    # Plot the vertical lines and annotate likelihood values
    total_likelihood = 1
    for i, (y, vline, text) in enumerate(zip(data, vlines, likelihood_texts)):
        # Gaussian curve height at the data points
        y_gaussian = gaussian_curve(y, mu, sigma)

        # Update vertical lines
        vline.set_data([y, y], [0, y_gaussian])

        # Annotate likelihood values
        text.set_text(f"{y_gaussian:.4f}")
        text.set_position((y, y_gaussian + 0.005))

        # Update total likelihood
        total_likelihood *= y_gaussian

    # Update total likelihood annotation
    total_likelihood_text.set_text(
        f"Likelihood: {total_likelihood:.3e}, std: {sigma:.2}"
    )

    return [gaussian_line] + vlines + likelihood_texts + [total_likelihood_text]


# Create the animation
ani = FuncAnimation(
    fig, update2, frames=int((10 - 1) / 0.2), init_func=init2, blit=True, interval=200
)

# Save the animation as a GIF file
ani.save("likelihood_animation_fixed_mu.gif", writer="pillow", fps=5)

# Save the animation as an AVI file
# ani.save("likelihood_animation_fixed_mu.avi", writer="ffmpeg", fps=10)

# Show the animation
plt.show()
