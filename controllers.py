import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_kdown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(settings, screen, ship, bullets)


def check_kup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kdown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_kup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def fire_bullets(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

def get_number_rows(settings, alien_height, ship_height):
    available_space_y = (settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows



def create_alien(screen, settings, aliens, alien_number, row_number):
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
          
def update_aliens(settings, aliens):
    check_fleet_edges(settings, aliens)
    aliens.update()

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1





    


