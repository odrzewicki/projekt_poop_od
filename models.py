from geo_utils import get_coordinates


class Parking:
    def __init__(self, name, location, map_widget):
        self.name = name
        self.location = location
        self.coordinates = get_coordinates(location)
        self.marker = map_widget.set_marker(*self.coordinates, text=self.name)


class Worker:
    def __init__(self, name, parking, location, map_widget):
        self.name = name
        self.parking = parking
        self.location = location
        self.coordinates = get_coordinates(location)
        self.marker = map_widget.set_marker(*self.coordinates, text=self.name)


class User:
    def __init__(self, name, parking, location, map_widget):
        self.name = name
        self.parking = parking
        self.location = location
        self.coordinates = get_coordinates(location)
        self.marker = map_widget.set_marker(*self.coordinates, text=self.name)