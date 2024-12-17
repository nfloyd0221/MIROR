import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circular Particle Effect")

# Colours
BACKGROUND_COLOR = (0, 0, 0)  # Black background
PARTICLE_COLOR = (0, 255, 255)  # Deep Blue-Green particles

# Particle properties
NUM_PARTICLES = 200  # Number of particles
particles = []

# Center of the circle
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
RADIUS = 200  # Radius of the particle circle

# Function to create particles in a circular formation
def create_particles():
    for _ in range(NUM_PARTICLES):
        angle = random.uniform(0, 2 * math.pi)  # Random angle around the circle
        distance = RADIUS + random.uniform(-10, 10)  # Slight variation in radius
        x = CENTER_X + distance * math.cos(angle)
        y = CENTER_Y + distance * math.sin(angle)
        speed_x = random.uniform(-0.5, 0.5)  # Tiny horizontal movement
        speed_y = random.uniform(-0.5, 0.5)  # Tiny vertical movement
        size = random.randint(2, 4)  # Particle size
        particles.append([x, y, speed_x, speed_y, size, angle, distance])

# Function to update and draw particles
def update_and_draw_particles():
    for particle in particles:
        # Update particle position slightly around its original angle and distance
        particle[5] += random.uniform(-0.01, 0.01)  # Slight wobble in angle
        particle[6] += random.uniform(-0.2, 0.2)  # Slight wobble in distance
        particle[0] = CENTER_X + particle[6] * math.cos(particle[5]) + particle[2]  # x
        particle[1] = CENTER_Y + particle[6] * math.sin(particle[5]) + particle[3]  # y

        # Draw particle
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(particle[0]), int(particle[1])), particle[4])

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

        # Clear screen
        screen.fill(BACKGROUND_COLOR)

        # Update and draw particles
        update_and_draw_particles()

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Run the program
if __name__ == "__main__":
    main()
