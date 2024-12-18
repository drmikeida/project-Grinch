import pyxel
class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        self.x = 75
        self.y = 55
        self.score = 0
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2
        self.peach_x = 10
        self.peach_y = 10
        self.peach_dx = 1
        self.peach_dy = 1
        self.game_over = False
        self.game_started = False
        pyxel.run(self.update, self.draw)
    def update(self):
        if not self.game_started:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.game_started = True
        elif not self.game_over:
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= 2
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += 2
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 2
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 2
          
            if (abs(self.x - self.sprite_x) < 10 and abs(self.y - self.sprite_y) < 10):
                self.score += 1
                self.sprite_x = pyxel.rndi(10, 150)
                self.sprite_y = pyxel.rndi(10, 110)
            self.sprite_x += self.sprite_dx
            self.sprite_y += self.sprite_dy
            if self.sprite_x <= 0 or self.sprite_x >= 160:
                self.sprite_dx *= -1
            if self.sprite_y <= 0 or self.sprite_y >= 120:
                self.sprite_dy *= -1
            self.peach_x += self.peach_dx
            self.peach_y += self.peach_dy
            if self.peach_x <= 0 or self.peach_x >= 160:
                self.peach_dx *= -1
            if self.peach_y <= 0 or self.peach_y >= 120:
                self.peach_dy *= -1
          
            if (abs(self.x - self.peach_x) < 10 and abs(self.y - self.peach_y) < 10):
                self.game_over = True
                
    def draw(self):
        if not self.game_started:
            self.start_screen()
        elif not self.game_over:
            pyxel.cls(7)  
           
            for i in range(0, 160, 10):
                for j in range(0, 120, 10):
                    pyxel.pset(i, j, 9)
            pyxel.rect(self.x, self.y, 10, 10, 11)
            
            pyxel.blt(self.sprite_x, self.sprite_y, 0, 24, 40, 16, 16)
            pyxel.circ(self.peach_x, self.peach_y, 5, 15)
            pyxel.text(5, 5, f"Score: {self.score}", 0) 
        else:
            pyxel.cls(7)  
            pyxel.text(50, 50, "Game Over!", 8)
            pyxel.text(50, 60, f"Score: {self.score}", 8)
    def start_screen(self):
        pyxel.cls(7)  
        pyxel.text(50, 50, "Press Space to Start", 0)  
App()