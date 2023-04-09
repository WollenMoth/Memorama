"""Módulo que contiene la clase Card."""

import pygame
from colors import TURQUOISE, WHITE
from common import Coordinate


class Card:
    """Clase que representa una carta del juego."""

    def __init__(self, image: pygame.Surface, pos: Coordinate):
        self.image = image
        self.pos = pos
        self.rect = pygame.Rect(pos, image.get_size())
        self.status = "closed"

    def __eq__(self, other: "Card") -> bool:
        """Compara dos cartas."""
        return self.image == other.image

    def draw(self, screen: pygame.Surface):
        """Dibuja la carta en la pantalla."""
        if self.status != "closed":
            screen.blit(self.image, self.pos)
        else:
            pygame.draw.rect(screen, WHITE, self.rect)
            pygame.draw.rect(screen, TURQUOISE, self.rect, 2)

    def flip(self):
        """Da la vuelta a la carta."""
        self.status = "open" if self.status == "closed" else "closed"
