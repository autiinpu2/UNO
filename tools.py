import pygame

class Button():
    def __init__(self, x, y, width, height, text, text_color, inactive_color, active_color, font_size=74, border_radius=20, action=None):
        """
        Initializes a new Button instance
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font = pygame.font.Font(None, font_size)
        self.border_radius = border_radius
        self.action = action
    def draw(self, screen):
        """
        Dessine le bouton sur l'écran
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.active_color, self.rect, 0, self.border_radius)
            if pygame.mouse.get_pressed()[0]:
                if self.action:
                    self.action()
        else:
            pygame.draw.rect(screen, self.inactive_color, self.rect, 0, self.border_radius)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class Button_dark_mode():
    def __init__(self, x, y, width, height, state, dark_mode_image, light_mode_image):
        self.rect = pygame.Rect(x, y, width/14.4, height/8.1)
        self.state = state
        self.dark_mode_image = dark_mode_image
        self.light_mode_image = light_mode_image
    
    def update(self, event):
        """
        Met à jour l'état du bouton de mode sombre en fonction de la position de la souris et des événements de la souris.
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = not self.state
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    def draw(self, screen):
        """
        Dessine le bouton de mode sombre sur l'écran.
        Affiche l'image de mode sombre si le bouton est activé, sinon affiche l'image de mode clair.
        """
        if self.state:
            screen.blit(self.dark_mode_image, self.rect)
        else:
            screen.blit(self.light_mode_image, self.rect)
    def get_state(self):
        return self.state

def open_rules():
    """
    Opens the rules of the game
    """
    import webbrowser
    webbrowser.open_new_tab("https://sites.google.com/view/uno-modifie/accueil")

class Background():
    def __init__(self, dark_color, light_color, dark_mode):
        self.dark_color = dark_color
        self.light_color = light_color
        self.dark_mode = dark_mode
        if dark_mode:
            self.color = dark_color  
            self.color_save = light_color
        else:
            self.color = light_color
            self.color_save = dark_color

    def draw(self, screen):
        screen.fill(self.color)
    def transition(self, fps):
        transition_frame = int(fps/5)
        for i in range(transition_frame):
            pass