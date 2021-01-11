import pygame
from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invassion")

    ship = Ship(ai_settings, screen)

    # Make a group to store the bullets in
    bullets = Group()

    # Start the main loop for the game.
    while True:

        ship.blitme()

        # Watch for keyboard and mouse input.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()