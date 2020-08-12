#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

class MyPolygon:

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def envelope(self):
        min_x = min(coord[0] for coord in self.coordinates)
        min_y = min(coord[1] for coord in self.coordinates)
        max_x = max(coord[0] for coord in self.coordinates)
        max_y = max(coord[1] for coord in self.coordinates)
        return [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]