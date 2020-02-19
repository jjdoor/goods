count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")

letters=['a','b','c']
del letters[1]
print(letters)

class Ball:
    def __init__(self,color,size,direction):
        self.color = color
        self.size  = size
        self.direction = direction
    def bounce(self):
        if self.direction=="down":
            self.direction = "up"
myball = Ball("red","small","down")
print(myball.size)
print(myball)