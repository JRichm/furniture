class furniture:
    def __init__(self, name, height, width, depth, drawers, shelves):
        self.name = name
        self.height = height
        self.width = width
        self.depth = depth
        self.drawers = drawers
        self.shelves = shelves

    def get_info(self):      
        if self.drawers > 0:
            print(self.name, self.drawers, "drawer with", self.shelves, "shelves")
        else:
            print(self.shelves, "shelf", self.name)

        print("H", self.height, "\tW", self.width, "\tD", self.depth, "\n")


furn1 = furniture('alex', 27, 14, 23, 5, 0)
furn2 = furniture('hemnes', 37, 63, 19, 8, 0)
furn3 = furniture('jonaxel', 63, 31, 15, 0, 5)
furn4 = furniture('jonaxel', 27, 9, 20, 0, 3)

furn1.get_info()
furn2.get_info()
furn3.get_info()
furn4.get_info()