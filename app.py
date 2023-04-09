"""Juego de Memorama"""

import random
import pygame
from card import Card
from colors import WHITE
from sprites import get_sprites

WIDTH, HEIGHT = 2 * 250, 2 * 320

FPS = 24

IMAGE_SIZE = (249, 320)
CARD_SIZE = (125, 160)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Memorama")

sprites = get_sprites("images", IMAGE_SIZE, CARD_SIZE) * 2
cards = [Card(s) for s in sprites]
random.shuffle(cards)


def draw() -> None:
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(WHITE)

    for i, card in enumerate(cards):
        x = i % 4
        y = i // 4
        card.draw(screen, (x * CARD_SIZE[0], y * CARD_SIZE[1]))

    pygame.display.flip()


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
