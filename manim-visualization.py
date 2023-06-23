# Import the necessary libraries
from manim import *  # Manim is a mathematical animation library
import numpy as np  # Numpy is a library for numerical computations

# Define a class for the boat wake animation


class BoatWake(Scene):  # Scene is a class from Manim that represents a scene in an animation
    def construct(self):  # construct is a method that defines what happens when the scene is played
        # Create a Text object for the title of the animation
        # Text is a class from Manim for creating text
        title = Text("Boat Wake Animation")
        # Set the color of the title to yellow
        # YELLOW is a constant from Manim representing the color yellow
        title.set_color(YELLOW)
        # Set the stroke (outline) of the title to black
        # BLACK is a constant from Manim representing the color black
        title.set_stroke(color=BLACK, width=1)
        # Display the title
        # Write is a class from Manim for animating the writing of text
        self.play(Write(title))
        # Wait for 5 seconds
        self.wait(5)  # wait is a method from Scene that pauses the animation
        # Fade out the title
        # FadeOut is a class from Manim for animating a fade out
        self.play(FadeOut(title))

        # Create the Axes object for the animation
        axes = Axes(
            # x_range is a list [start, end, step] defining the range and step of the x-axis
            x_range=[0, 10, 1],
            # y_range is a list [start, end, step] defining the range and step of the y-axis
            y_range=[-5, 5, 1],
            x_length=9,  # x_length is the length of the x-axis
            y_length=6,  # y_length is the length of the y-axis
            # axis_config is a dictionary for configuring the appearance of the axes
            axis_config={"color": BLUE},
        )
        # Display the axes
        # Write is used here to animate the drawing of the axes
        self.play(Write(axes))

        # Define variables for the animation
        wavelength = 0.1  # wavelength is the distance between points in the wave
        # num_shapes is the number of shapes in the wave, calculated as the ceiling of 1 divided by the wavelength
        num_shapes = np.ceil(1 / wavelength)
        power = 1 / 2  # power is a variable used in the calculation of the wave
        alpha = 0  # alpha is a variable used in the calculation of the wave

        # Loop over a range of angles
        # np.arange is a function from Numpy that returns an array of evenly spaced values within a given interval
        for angle in np.arange(0, np.pi/2, 0.01):
            # Loop over the number of shapes
            # range is a built-in Python function that returns a sequence of numbers
            for n in range(1, int(num_shapes)+1):
                # Calculate the y-coordinate of the point on the line
                y2 = self.point_on_line(axes.x_length, angle, n)
                # Create a Line object for the upper half of the wave
                # Line is a class from Manim for creating lines
                line1 = Line([self.delta_x(angle, n), 0, 0], [
                             axes.x_length, y2, 0], color=ORANGE, stroke_width=0.8)
                # Create a Line object for the lower half of the wave
                # ORANGE is a constant from Manim representing the color orange
                line2 = Line([self.delta_x(angle, n), 0, 0], [
                             axes.x_length, -y2, 0], color=ORANGE, stroke_width=0.8)
                # Display the lines
                # Create is a class from Manim for animating the creation of an object
                self.play(Create(line1), Create(line2), run_time=0.1)
            # Increment alpha
            alpha += 0.01

        # Wait for 3 seconds
        self.wait(3)

    # lambda_max is a method that calculates the maximum wavelength

    def lambda_max(self):
        return 9 * 0.1

    # lambda_ is a method that calculates the wavelength as a function of alpha
    def lambda_(self, alpha):
        return self.lambda_max() * np.power(np.sin(alpha), 1 / 0.5)

    # Define a function to calculate the change in x
    def delta_x(self, alpha, n):
        return n * self.lambda_(alpha) / np.sin(alpha)

    # Define a function to calculate the point on the line
    def point_on_line(self, x, alpha, n):
        return x * np.tan(alpha) - n * self.lambda_(alpha) / np.cos(alpha)

# This code creates an animation of a boat wake using the Manim library. 
# It first displays a title, then creates an axes system. 
# It then loops over a range of angles and for each angle, 
# it creates a number of lines that represent the wake of the boat. 
# The position of these lines is calculated using the delta_x and point_on_line functions. 
# The lambda_ function is used to calculate the wavelength of the wake, 
# and the lambda_max function is used to calculate the maximum wavelength.

########### Our Research Workspace: https://github.com/7Wdev/PHYSICS-RESEARCH-LPS ###########

# The Kelvin wake pattern is a wave pattern created by an object moving through a fluid, typically a boat moving through water.
# This pattern is named after Lord Kelvin, who first explained the physics behind it.

# When a boat moves through water, it creates waves that propagate outwards from the path of the boat.
# These waves form a distinct pattern known as a wake, which consists of two parts: the transverse waves and the divergent waves.

# The transverse waves form a series of straight lines parallel to the path of the boat.
# The divergent waves form a series of V-shaped lines that spread out from the path of the boat.
# The angle between the divergent waves is always approximately 39.2 degrees, regardless of the speed of the boat.
# This is known as Kelvin's angle.

# The physics behind the Kelvin wake pattern can be explained by the principles of wave interference and diffraction.
# As the boat moves through the water, it creates a series of wavefronts that propagate outwards.
# These wavefronts interfere with each other, creating a pattern of constructive and destructive interference.
# The points of constructive interference form the visible lines of the wake.

# The mathematics behind the Kelvin wake pattern involves the calculation of the wavelength and the position of the waves.
# The wavelength is calculated using the formula lambda = lambda_max * sin(alpha)^(1/2), where lambda_max is the maximum wavelength, alpha is the angle of the wave, and 1/2 is the power.
# The position of the waves is calculated using the formulas delta_x = n * lambda / sin(alpha) and y = x * tan(alpha) - n * lambda / cos(alpha), 
# where n is the number of waves, x is the position along the x-axis, and y is the position along the y-axis.
# These formulas are used in the lambda_, delta_x, and point_on_line functions in the code.

# To gain a more detailed understanding of the physics behind Kelvin wakes, you can refer to resources on fluid dynamics and wave interference. Some recommended resources include:
# - "Fluid Mechanics" by Frank M. White: This textbook provides a comprehensive introduction to fluid mechanics, covering topics such as fluid properties, flow behavior, 
# and wave propagation. It includes chapters on wave interference and the formation of wakes.
# - "Introduction to Wave Phenomena" by Akira Hirose: This book focuses specifically on wave phenomena, including wave propagation, wave interference, and diffraction. 
# It covers the mathematical principles and physical concepts behind wave behavior, making it a valuable resource for understanding Kelvin wakes.
# These resources delve into the mathematical equations and physical principles that govern the formation of Kelvin wakes. They cover topics such as wave propagation, 
# wave interference, and the interaction of waves with boundaries. By studying these resources, you can gain a deeper understanding of the physics behind Kelvin wakes and how they 
# are formed in fluid dynamics.