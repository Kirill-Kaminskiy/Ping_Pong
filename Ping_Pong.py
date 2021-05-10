from superwires import games, color
import random

games.init(screen_width=1400, screen_height=800, fps=50)


class Rectangle(games.Sprite):
    image = games.load_image("rectangle (2).png", transparent=False)

    def __init__(self):
        super(Rectangle, self).__init__(image = Rectangle.image, x = games.mouse.x,
                                        y = games.screen.height)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        elif self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        for ball in self.overlapping_sprites:
            ball.change_direction()


class Ball(games.Sprite):
    image = games.load_image("photoeditorsdk-export (2).png")
    speed = 3

    def __init__(self):
        super(Ball, self).__init__(image=Ball.image, x = games.screen.width/2, y = games.screen.height/2,
                                   dx=Ball.speed,
                                   dy=Ball.speed)

    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            self.delete()
            self.end_game()

    def change_direction(self):
        self.dy = -self.dy

    def delete(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=2 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

def main():
    background_image = games.load_image("background.jpg", transparent=False)
    games.screen.background = background_image

    the_Rectnagle = Rectangle()
    the_Ball = Ball()

    games.screen.add(the_Rectnagle)
    games.screen.add(the_Ball)

    games.mouse.is_visible = False
    games.mouse.event_grab = True
    games.screen.mainloop()


if __name__ == '__main__':
    main()