import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def get_number_rows(ai_settings, ship_height, alien_height):
    # Calculate how many rows aliens can be draw in the screen.
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - 
        ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    # Calculate how many aliens can be draw in one row.
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Set an alien and add it into the current row.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)



def create_fleet(ai_settings, screen, ship, aliens, level):
    """Set a fleet of aliens."""
    # Set an alien and calculate how many aliens can be draw in one row.
    # The space between aliens equal to the width of an alien.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    max_number_rows = get_number_rows(ai_settings, ship.rect.height, 
        alien.rect.height)
    number_rows = min(max_number_rows, level)

    # Set a group of aliens.
    # for row_number in range(number_rows):
    #     for alien_number in range(number_aliens_x):
    #        create_alien(ai_settings, screen, aliens, alien_number, 
    #            row_number)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

        
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to press the key."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

        
def fire_bullet(ai_settings, screen, ship, bullets):
    """If the rest bullets in screen are lower than allowed, 
    then shoot one bullet."""
    # Set a bullet, and add it into group bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
     """Respond to release the key."""
     if event.key == pygame.K_RIGHT:
        ship.moving_right = False
     elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keyborad and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)    
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)


def update_bullets(ai_settings, screen, ship, aliens, bullets, stats):
    """Update the location of bullets, and delete disappeared bullets."""
    # Update the location of bullets.
    bullets.update()
    
    # Delete disappeared bullets.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, 
        stats)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, 
        stats):
    """Respond to the collisions of bullets and aliens"""
    # Check whether bullets shot the aliens, if so, delete both of them.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
    # Delete the rest bullets and set a new group of aliens.
        stats.level += 1
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens, stats.level)

            
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update the image on screen and shift to new screen."""
    # Redraw the screen in everyloops.
    screen.fill(ai_settings.bg_color)

    # Redraw all of bullets behind the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()    

    ship.blitme()
    aliens.draw(screen)

    # Make the screen mode to be seen.
    pygame.display.flip()


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to the ship hit by the ship."""
    if stats.ships_left > 0:
        # Minus one from ship_left.
        stats.ships_left -= 1
        stats.level = 1

        # Clear the group of alien and bullet.
        aliens.empty()
        bullets.empty()

        # Set a new group of alien, 
        # and put ship in the middle position at the bottom of screent.
        create_fleet(ai_settings, screen, ship, aliens, stats.level)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check whether any aliens move to the bottom of screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Dispose the case like ship hit by aliens.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def check_fleet_edges(ai_settings, aliens):
    """Measures respond to aliens move to the edges."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Move all the aliens down and change their direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1    


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if aliens move to the edges and update all aliens location."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Check whether any aliens move to the bottom of screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    
    # Check the collisions of aliens and the ship.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
