import pygame

IMAGE_SIZE = (20, 20)
BLOCK_SIZE = 20
START_X, START_Y = 400, 300


class BodySegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)


class Snake:

    def __init__(self, screen):
        self.head = None
        self.tail = None
        self.screen = screen
        self.create_snake()

        # Head Graphics
        self.h_right = pygame.transform.scale(pygame.image.load("Graphics/head_right.png").convert_alpha(), IMAGE_SIZE)
        self.h_left = pygame.transform.scale(pygame.image.load("Graphics/head_left.png").convert_alpha(), IMAGE_SIZE)
        self.h_up = pygame.transform.scale(pygame.image.load("Graphics/head_up.png").convert_alpha(), IMAGE_SIZE)
        self.h_down = pygame.transform.scale(pygame.image.load("Graphics/head_down.png").convert_alpha(), IMAGE_SIZE)

        # Tail Graphics
        self.t_right = pygame.transform.scale(pygame.image.load("Graphics/tail_right.png").convert_alpha(), IMAGE_SIZE)
        self.t_left = pygame.transform.scale(pygame.image.load("Graphics/tail_left.png").convert_alpha(), IMAGE_SIZE)
        self.t_up = pygame.transform.scale(pygame.image.load("Graphics/tail_up.png").convert_alpha(), IMAGE_SIZE)
        self.t_down = pygame.transform.scale(pygame.image.load("Graphics/tail_down.png").convert_alpha(), IMAGE_SIZE)

        # Body Graphics

        self.b_horizontal = pygame.transform.scale(pygame.image.load
                                                   ("Graphics/body_horizontal.png").convert_alpha(), IMAGE_SIZE)
        self.b_vertical = pygame.transform.scale(pygame.image.load
                                                 ("Graphics/body_vertical.png").convert_alpha(), IMAGE_SIZE)
        self.b_tl = pygame.transform.scale(pygame.image.load("Graphics/body_tl.png").convert_alpha(), IMAGE_SIZE)
        self.b_tr = pygame.transform.scale(pygame.image.load("Graphics/body_tr.png").convert_alpha(), IMAGE_SIZE)
        self.b_bl = pygame.transform.scale(pygame.image.load("Graphics/body_bl.png").convert_alpha(), IMAGE_SIZE)
        self.b_br = pygame.transform.scale(pygame.image.load("Graphics/body_br.png").convert_alpha(), IMAGE_SIZE)

        # Sounds
        self.crunch_sound = pygame.mixer.Sound("Sounds/Sound_crunch.wav")
        self.turn_sound = pygame.mixer.Sound("Sounds/Sound_turn.wav")
        self.game_over_sound = pygame.mixer.Sound("Sounds/Sound_GameOver.wav")

    def extend_snake(self):
        self.append_segment(self.tail.rect.x, self.tail.rect.y)

    def append_segment(self, x, y):
        new_segment = BodySegment(x, y)
        if self.head is None:
            self.head = new_segment
            self.tail = new_segment
        else:
            new_segment.prev = self.tail
            self.tail.next = new_segment
            self.tail = new_segment

    def create_snake(self):
        self.append_segment(START_X, START_Y)
        self.append_segment(START_X - BLOCK_SIZE, START_Y)
        self.append_segment(START_X - BLOCK_SIZE * 2, START_Y)

    def draw_snake(self, direction):

        # Head orientation
        if direction == "up":
            self.screen.blit(self.h_up, self.head.rect)
        elif direction == "down":
            self.screen.blit(self.h_down, self.head.rect)
        elif direction == "left":
            self.screen.blit(self.h_left, self.head.rect)
        else:
            self.screen.blit(self.h_right, self.head.rect)

        current = self.head.next

        while current is not self.tail:
            if current.rect.x == current.prev.rect.x and current.rect.x == current.next.rect.x:
                self.screen.blit(self.b_vertical, current.rect)
            if current.rect.y == current.prev.rect.y and current.rect.y == current.next.rect.y:
                self.screen.blit(self.b_horizontal, current.rect)

            # Body while moving right

            if current.rect.y > current.prev.rect.y and current.rect.x > current.next.rect.x:
                self.screen.blit(self.b_tl, current.rect)
            if current.rect.y < current.prev.rect.y and current.rect.x > current.next.rect.x:
                self.screen.blit(self.b_bl, current.rect)

            # Body while moving left

            if current.rect.y > current.prev.rect.y and current.rect.x < current.next.rect.x:
                self.screen.blit(self.b_tr, current.rect)
            if current.rect.y < current.prev.rect.y and current.rect.x < current.next.rect.x:
                self.screen.blit(self.b_br, current.rect)

            # Body while moving up

            if current.rect.x > current.prev.rect.x and current.rect.y < current.next.rect.y:
                self.screen.blit(self.b_bl, current.rect)
            if current.rect.x < current.prev.rect.x and current.rect.y < current.next.rect.y:
                self.screen.blit(self.b_br, current.rect)

            # Body while moving down

            if current.rect.x < current.prev.rect.x and current.rect.y > current.next.rect.y:
                self.screen.blit(self.b_tr, current.rect)
            if current.rect.x > current.prev.rect.x and current.rect.y > current.next.rect.y:
                self.screen.blit(self.b_tl, current.rect)

            # pygame.draw.rect(self.screen, "green", current.rect)
            current = current.next

        # Tail orientation

        if self.tail.rect.y == self.tail.prev.rect.y and self.tail.rect.x < self.tail.prev.rect.x:
            self.screen.blit(self.t_left, self.tail.rect)
        if self.tail.rect.y == self.tail.prev.rect.y and self.tail.rect.x > self.tail.prev.rect.x:
            self.screen.blit(self.t_right, self.tail.rect)
        if self.tail.rect.x == self.tail.prev.rect.x and self.tail.rect.y < self.tail.prev.rect.y:
            self.screen.blit(self.t_up, self.tail.rect)
        if self.tail.rect.x == self.tail.prev.rect.x and self.tail.rect.y > self.tail.prev.rect.y:
            self.screen.blit(self.t_down, self.tail.rect)

    def move(self, direction):
        if direction == "right":
            current = self.tail
            while current is not self.head:
                current.rect.x = current.prev.rect.x
                current.rect.y = current.prev.rect.y
                current = current.prev
            self.head.rect.x += BLOCK_SIZE

        if direction == "left":
            current = self.tail
            while current is not self.head:
                current.rect.x = current.prev.rect.x
                current.rect.y = current.prev.rect.y
                current = current.prev
            self.head.rect.x -= BLOCK_SIZE

        if direction == "up":
            current = self.tail
            while current is not self.head:
                current.rect.x = current.prev.rect.x
                current.rect.y = current.prev.rect.y
                current = current.prev
            self.head.rect.y -= BLOCK_SIZE

        if direction == "down":
            current = self.tail
            while current is not self.head:
                current.rect.x = current.prev.rect.x
                current.rect.y = current.prev.rect.y
                current = current.prev
            self.head.rect.y += BLOCK_SIZE

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def play_turn_sound(self):
        self.turn_sound.play()

    def play_game_over(self):
        self.game_over_sound.play()

