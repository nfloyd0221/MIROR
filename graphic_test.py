import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen (adjust resolution as needed)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Particle Effect Test")

# Colours
BACKGROUND_COLOR = (0, 0, 0)  # Black background
PARTICLE_COLOR = (0, 255, 255)  # Deep Blue-Green particles

# Particle properties
NUM_PARTICLES = 100  # Number of particles
particles = []

# Function to create particles
def create_particles():
    for _ in range(NUM_PARTICLES):
        x = random.uniform(0, SCREEN_WIDTH)
        y = random.uniform(0, SCREEN_HEIGHT)
        speed_x = random.uniform(-1, 1)
        speed_y = random.uniform(-1, 1)
        size = random.randint(2, 6)
        particles.append([x, y, speed_x, speed_y, size])

# Function to update and draw particles
def update_and_draw_particles():
    for particle in particles:
        # Update position
        particle[0] += particle[2]  # x += speed_x
        particle[1] += particle[3]  # y += speed_y

        # Respawn if out of bounds
        if particle[0] < 0 or particle[0] > SCREEN_WIDTH or particle[1] < 0 or particle[1] > SCREEN_HEIGHT:
            particle[0] = random.uniform(0, SCREEN_WIDTH)
            particle[1] = random.uniform(0, SCREEN_HEIGHT)

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
