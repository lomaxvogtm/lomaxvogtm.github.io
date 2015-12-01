__author__ = 'Madeleine'
import tkinter as tk


class Elevator():

    def __init__(self, canvas, num_floors, width, height, vspace, hspace):
        self.num_floors = num_floors
        self.width = width
        self.height = height
        self.vspace = vspace
        self.hspace = hspace
        self.canvas = canvas
        self.position = 0
        self.passengers = []
        self.list = []
        self.root = root

    def draw_elevator(self):
        self.canvas.delete("all")
        for i in range(self.num_floors):
            if self.position <= 3:
                if (self.num_floors-i-1) == self.position:
                    self.canvas.create_rectangle(self.hspace, self.vspace+i*(self.height+self.vspace),
                                                 self.hspace+self.width, (i+1)*(self.height+self.vspace),
                                                 fill='red', outline='black')
                else:
                    self.canvas.create_rectangle(self.hspace, self.vspace+i*(self.height+self.vspace),
                                                 self.hspace+self.width, (i+1)*(self.height+self.vspace),
                                                 fill='grey', outline='black')


class Building:
    width = 20
    height = 30
    hspace = 10
    vspace = 5
    num_floors = 4

    def __init__(self, root):
        self.list_pass = []
        self.root = root
        self.direction = 1
        self.canvas = tk.Canvas(root, height=(Building.num_floors*Building.height) +
                                             ((Building.num_floors+1)*Building.vspace), width=(2*Building.hspace) +
                                                                                              Building.width, bg='grey')
        self.canvas.grid(row=0, column=0)
        outline = tk.Frame(root)
        outline.grid(row=0, column=1)
        self.elevator = Elevator(self.canvas, Building.num_floors, Building.width,
                                 Building.height, Building.vspace, Building.hspace)
        self.elevator.passengers = []
        for i in range(Building.num_floors):
            self.elevator.passengers.append(tk.StringVar())
            entry = tk.Entry(outline, textvariable=self.elevator.passengers[i])
            entry.grid(row=i, column=1)
        self.controller()

    def controller(self):
        def pick_up_passengers():
            for passenger in x:
                try:
                    floor = int(passenger)-1
                    if floor > Building.num_floors-1:
                        x.remove(passenger)
                    if floor < 0:
                        x.remove(passenger)
                    if floor == self.elevator.position:
                        x.remove(passenger)
                    if self.direction == -1 and floor < self.elevator.position:
                        self.list_pass.append(floor)
                        x.remove(passenger)
                    if self.direction == 1 and floor > self.elevator.position:
                        self.list_pass.append(floor)
                        x.remove(passenger)
                except ValueError:
                    x.remove(passenger)
        def drop_off_passengers():
            for passenger in self.list_pass:
                if int(passenger) == self.elevator.position:
                    self.list_pass.remove(passenger)
        self.elevator.draw_elevator()

        x = self.elevator.passengers[self.elevator.position].get()
        x = x.split(',')
        pick_up_passengers()
        drop_off_passengers()
        x= ','.join(x)
        self.elevator.passengers[self.elevator.position].set(x)
        print(x, self.list_pass, self.elevator.position)

        if self.elevator.position == Building.num_floors-1:
            self.direction = -1
        elif self.elevator.position == 0:
            self.direction = 1
        # Get passengers from current floor
        self.elevator.position += self.direction
        self.root.after(2000, self.controller)



root = tk.Tk()
draw = Building(root)
root.mainloop()

#cosmetic stuff
#passengers on elevator list
#delay/error when picking up passengers
#