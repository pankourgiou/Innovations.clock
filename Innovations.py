import pygame
import math
import datetime
import random

# List of innovations with year and description
tech_innovations = [
    ("Printing Press (1440)", "Gutenberg revolutionized knowledge distribution."),
    ("Steam Engine (1712)", "Powered the industrial revolution."),
    ("Telephone (1876)", "Invented by Alexander Graham Bell."),
    ("Electric Light (1879)", "Edison lit up the world."),
    ("Airplane (1903)", "Wright brothers took flight."),
    ("Television (1927)", "The world saw moving images."),
    ("Computer (1940s)", "Birth of digital computation."),
    ("Internet (1969)", "ARPANET began a new era."),
    ("Mobile Phone (1973)", "First call from a cell phone."),
    ("GPS (1978)", "Global Positioning System launched."),
    ("World Wide Web (1991)", "Tim Berners-Lee connected us."),
    ("Smartphones (2007)", "iPhone changed everything."),
    ("CRISPR (2012)", "Precise genetic editing."),
    ("AI Boom (2015+)", "Machines started thinking."),
    ("Quantum Supremacy (2019)", "Quantum computers outperform classical."),
    ("Reusable Rockets (2020s)", "SpaceX redefines access to space.")
]

# Setup
pygame.init()
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Technological Innovations Clock")
font = pygame.font.SysFont("consolas", 18)
title_font = pygame.font.SysFont("consolas", 24, bold=True)
clock = pygame.time.Clock()

def draw_clock(surface, center, time_now):
    pygame.draw.circle(surface, (20, 20, 30), center, 250)
    pygame.draw.circle(surface, (0, 120, 255), center, 5)

    for i in range(60):
        angle = math.radians(i * 6)
        x1 = center[0] + 240 * math.sin(angle)
        y1 = center[1] - 240 * math.cos(angle)
        x2 = center[0] + 230 * math.sin(angle)
        y2 = center[1] - 230 * math.cos(angle)
        color = (0, 100, 180) if i % 5 == 0 else (40, 40, 60)
        pygame.draw.line(surface, color, (x1, y1), (x2, y2), 2 if i % 5 == 0 else 1)

    hour = time_now.hour % 12
    minute = time_now.minute
    second = time_now.second

    def draw_hand(length, angle, color, width):
        angle_rad = math.radians(angle)
        x = center[0] + length * math.sin(angle_rad)
        y = center[1] - length * math.cos(angle_rad)
        pygame.draw.line(surface, color, center, (x, y), width)

    hour_angle = (hour + minute / 60) * 30
    minute_angle = (minute + second / 60) * 6
    second_angle = second * 6

    draw_hand(120, hour_angle, (0, 200, 255), 8)
    draw_hand(180, minute_angle, (180, 180, 255), 5)
    draw_hand(200, second_angle, (255, 80, 80), 2)

# Main loop
running = True
last_hour = -1
current_innovation = random.choice(tech_innovations)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    # Change innovation only when hour changes
    if now.hour != last_hour:
        current_innovation = random.choice(tech_innovations)
        last_hour = now.hour

    screen.fill((10, 10, 20))
    draw_clock(screen, (WIDTH // 2, HEIGHT // 2), now)

    # Display innovation info
    title_text = title_font.render(current_innovation[0], True, (0, 200, 255))
    desc_text = font.render(current_innovation[1], True, (200, 200, 255))

    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT - 100))
    screen.blit(desc_text, (WIDTH//2 - desc_text.get_width()//2, HEIGHT - 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
