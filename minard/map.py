from matplotlib import pyplot as plt

class AbstractDisplayble(object):
    def draw(self):
        raise NotImplementedError

    def display(self):
        plt.show()

class MinardSegment(object):
    def __init__(self, orentation, width, length, front_coord):
        self.orientation = orentation
        self.width = width
        self.length = length
        self.front_coord = front_coord

    def draw(self):
        pass # TODO: Get axes here, draw rectangle

class MinardPartition(object):
    pass

class MinardPath(object):
    def __init__(self, segments):
        self.segments = segments

    def draw(self):
        for s in self.segments:
            s.draw()

def make_map_from_data(counts):
    pass