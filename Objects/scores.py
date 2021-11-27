from Objects.textsprite import Text_sprite


class Scores:
    def __init__(self, screen, score, color=(255, 255, 255), x=30, y=30, text_size=20):
        self.score = score
        self.text = Text_sprite(text='score:', screen=screen, x=x, y=y, color=color, text_size=text_size)
        self.text_score = Text_sprite(text=self.score, screen=screen, x=x + text_size * 7 / 2, y=y, color=color,
                                      text_size=text_size)

    def change_score(self, score):
        self.score = int(score)
        self.text_score.change_text(str(score))

    def draw(self):
        self.text.draw()
        self.text_score.draw()
