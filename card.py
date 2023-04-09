"""Módulo que contiene la clase Card."""

import pygame
from colors import TURQUOISE
from common import Coordinate


class Card:
    """Clase que representa una carta del juego."""

    def __init__(self, image: pygame.Surface):
        self.image = image
        self.status = "closed"

    def draw(self, screen: pygame.Surface, dest: Coordinate):
        """Dibuja la carta en la pantalla."""
        if self.status != "closed":
            screen.blit(self.image, dest)
        else:
            rect = (dest, self.image.get_size())
            pygame.draw.rect(screen, TURQUOISE, rect, 2)

    def flip(self):
        """Da la vuelta a la carta."""
        self.status = "open" if self.status == "closed" else "closed"
