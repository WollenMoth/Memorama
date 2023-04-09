"""Módulo para cargar los sprites"""

from os import listdir
from os.path import join
import pygame
from common import Coordinate


def get_sprites(
    directory: str,
    size: Coordinate,
    scale: Coordinate
) -> list[pygame.Surface]:
    """Obtiene los sprites de un sprite sheet"""
    image = listdir(directory)[0]
    path = join(directory, image)
    sprite_sheet = pygame.image.load(path).convert_alpha()

    sprites = []

    for j in range(0, sprite_sheet.get_height(), size[1]):
        for i in range(0, sprite_sheet.get_width(), size[0]):
            surface = pygame.Surface(size)
            rect = pygame.Rect((i, j), size)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale(surface, scale))

    return sprites
