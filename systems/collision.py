def check_collision(player, platforms):
    on_ground = False
    
    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            if (player.vel_y >= 0 and 
                player.rect.bottom <= platform.rect.top + 30 and 
                player.rect.bottom > platform.rect.top - 5):
                player.rect.bottom = platform.rect.top
                player.vel_y = 0
                on_ground = True
            elif (player.vel_y <= 0 and 
                  player.rect.top >= platform.rect.bottom - 20 and 
                  player.rect.top < platform.rect.bottom + 5):
                player.rect.top = platform.rect.bottom
                player.vel_y = 0
    
    return on_ground