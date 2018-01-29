import pygame
import sys
from random import *
import string
#colors
blue = (0,0,255)
light_blue = (155,166,201)
light_grey = (211,211,211)
red = (255,0,0)

'''
name: [color, location, circle size,[friends]]




'''
print(''.join(choice(string.ascii_uppercase + string.digits) for _ in range(5)))

#where future list of friends will be added



people = {
    "Quade": [blue,
            (400,300),10,["Dan"]],

    "Dan": [light_blue,
            (420,320),10,["Quade"]],

    "Dan1": [light_blue,
                (380,280),10,["Quade"]]




}

for _ in range(20):
    wow = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(5))
    people[wow]= [red,
            (randint(50,950),randint(50,950)),10,sample(people.keys(),len(people)-1)]


    


class friend_cirlces():

    def main(self):
        self.pressed = False
        self.display = (1000,1000)
        self.gameDisplay = pygame.display.set_mode(self.display, pygame.RESIZABLE)
        pygame.display.set_caption('Friend Circles')
        self.clock = pygame.time.Clock()
        
        

        while 1:

            self.inputs()


            self.gameDisplay.fill(light_grey)

            #draw the lines
            self.connecting_people()

            self.move_circle()


            



            #goes through dict to show peoples circles
            for key, value in people.items():
                pygame.draw.circle(self.gameDisplay,value[0],value[1],value[2])
            


            pygame.display.update()
            


    def circle_detection(self,location,radius):
        

        current_location = pygame.mouse.get_pos()

        if (location[0] + radius) >current_location[0] and (location[0] - radius) < current_location[0]:
            if (location[1] + radius) >current_location[1] and (location[1] - radius) < current_location[1]:
                return True
            else: return False
        else: return False



    def inputs(self):

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

                if event.type == pygame.MOUSEBUTTONUP:
                    self.pressed = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pressed = True

                if event.type == pygame.VIDEORESIZE:
                    self.gameDisplay = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)



    def connecting_people(self):

        for key, value in people.items():
            for name in value[3]:
                    you = people[key]
                    friend = people[name]
                    pygame.draw.line(self.gameDisplay, red, you[1], friend[1], 1)
                    
        



        




    def draw_circles(self):

        for key, value in people.items():
                
                pygame.draw.circle(gameDisplay,value[0],value[1],value[2])


    def move_circle(self):

        for key, value in people.items():

            if self.pressed and self.circle_detection(people[key][1],people[key][2]):
                    people[key][1] = pygame.mouse.get_pos()
        




Start = friend_cirlces()
Start.main()