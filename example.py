class Game:
    def __init__(self):
        self.maze = None
    
    def make2RoomsMaze(self):
        maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
        
        door = Door(room1, room2)
        room1.south = door
        room2.north = door

        maze.addRoom(room1)
        maze.addRoom(room2)

        self.maze = maze

        return maze
        
    def make2RoomsMazeFM(self):
        maze = self.createMaze()
        room1 = self.createRoom(1)
        room2 = self.createRoom(2)
        
        door = self.createDoor(room1, room2)
        room1.south = door
        room2.north = door

        maze.addRoom(room1)
        maze.addRoom(room2)

        self.maze = maze
        
        return maze


    def createMaze(self):
        return Maze()

    def createRoom(self, id):
        return Room(id)

    def createDoor(self, side1, side2):
        return Door(side1, side2)

    def createWall(self):
        return Wall()



class MapElement:
    def __init__(self):
        pass
    
    def enter(self):
        pass

class Maze(MapElement):
    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)
        
    def enter(self):
        if len(self.rooms) > 0:
            self.rooms[0].enter()


class Room(MapElement):
    def __init__(self, id):
        self.north = Wall()
        self.south = Wall()
        self.east = Wall()
        self.west = Wall()
        self.id = id
        
    def enter(self):
        print("Entered room ", self.id)


class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.open = False
        
    def enter(self):
        if self.open:
            print("You go through the open door")
            self.side2.enter()
        else:
            print("The door is closed. You need to open it first.")


class Wall(MapElement):
    def __init__(self):
        pass
    
    def enter(self):
        print("You can't enter a wall, dummy.")

class BombedWall(Wall):
    def __init__(self):
        self.active = False
        
    def enter(self):
        if self.active:
            print("You idiot! You walked straight into a bombed wall and got yourself killed. Moron.")
        else:
            print("You can't enter a wall, dummy.")


game=Game()
game.make2RoomsMaze().rooms[0].south.enter()
game.maze.enter()