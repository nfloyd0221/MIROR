import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)  # Enable transparency
pygame.display.set_caption("Pulsing Circular Particle Effect")

# Particle colour
PARTICLE_COLOR = (42, 32, 135, 255)  # Purple-blue particles with full opacity (RGBA)

# Particle properties
NUM_PARTICLES = 200  # Number of particles
particles = []

# Center of the circle
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
BASE_RADIUS = 200  # Base radius of the circle
PULSE_SPEED = 0.01  # Speed of the pulsing effect
pulse_offset = 0  # Tracks the current pulse offset

# Function to create particles in a circular formation
def create_particles():
    for _ in range(NUM_PARTICLES):
        angle = random.uniform(0, 2 * math.pi)  # Random angle around the circle
        distance = BASE_RADIUS + random.uniform(-10, 10)  # Slight variation in radius
        size = random.randint(2, 4)  # Particle size
        speed = random.uniform(-0.1, 0.1)  # Slower movement
        particles.append([angle, distance, size, speed])

# Function to update and draw particles
def update_and_draw_particles():
    global pulse_offset
    pulse_offset += PULSE_SPEED

    # Calculate the current pulsing radius
    pulse_radius = BASE_RADIUS + 20 * math.sin(pulse_offset)

    for particle in particles:
        # Slightly adjust particle's angle for slow movement
        particle[0] += particle[3]

        # Calculate particle's position based on pulsing radius
        x = CENTER_X + (pulse_radius + random.uniform(-5, 5)) * math.cos(particle[0])
        y = CENTER_Y + (pulse_radius + random.uniform(-5, 5)) * math.sin(particle[0])

        # Draw particle
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(x), int(y)), particle[2])

# Main loop
def main():
    clock = pygame.time.Clock()
    create_particles()

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # **Do not clear the screen** - Particles build on top of each other

        # Update and draw particles
        update_and_draw_particles()

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Run the program
if __name__ == "__main__":
    main()
