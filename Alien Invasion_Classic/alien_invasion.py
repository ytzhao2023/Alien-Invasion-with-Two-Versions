import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    # Initialize the pygame, settings and screen mode.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set the play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Set a instance for storing the statistics.
    stats = GameStats(ai_settings)

    # Set a ship, a group of bullets, a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Set a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set an argument to store the game statistics and set a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, 
                bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
            play_button)

run_game()