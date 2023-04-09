"""Juego de Memorama"""

import random
from time import sleep
import pygame
from card import Card
from colors import TURQUOISE
from common import Coordinate
from sprites import get_sprites

WIDTH, HEIGHT = 2 * 250, 2 * 320

FPS = 24

IMAGE_SIZE = (249, 320)
CARD_SIZE = (125, 160)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Memorama")


def get_pos(i: int) -> Coordinate:
    """Obtiene la posición de una carta"""
    return (i % 4 * CARD_SIZE[0], i // 4 * CARD_SIZE[1])


def draw(cards: list[Card]) -> None:
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(TURQUOISE)

    for card in cards:
        card.draw(screen)

    pygame.display.flip()


def handle_click(cards: list[Card], click_counter: int) -> int:
    """Maneja el evento de click del mouse"""
    pos = pygame.mouse.get_pos()

    for card in cards:
        if card.status == "closed" and card.rect.collidepoint(pos):
            click_counter += 1
            card.flip()
            break

    draw(cards)

    if click_counter == 2:
        flipped = [c for c in cards if c.status == "open"]

        if flipped[0] == flipped[1]:
            cards.remove(flipped[0])
            cards.remove(flipped[1])
        else:
            flipped[0].flip()
            flipped[1].flip()

        sleep(0.5)
        draw(cards)

    return click_counter


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    sprites = get_sprites("images", IMAGE_SIZE, CARD_SIZE) * 2

    while running:
        random.shuffle(sprites)
        cards = [Card(s, get_pos(i)) for i, s in enumerate(sprites)]

        click_counter = 0

        draw(cards)

        while running and len(cards):
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_counter = handle_click(cards, click_counter)
                    click_counter %= 2

    pygame.quit()


if __name__ == "__main__":
    main()
