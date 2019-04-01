import math
from display import *

def cross_product(a,b):
  return [a[1]*b[2]-a[2]*b[1],
          a[2]*b[0]-a[0]*b[2],
          a[0]*b[1]-a[1]*b[0]]
#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    mag = math.sqrt(vector[0]**2+vector[1]**2+vector[2]**2)
    vector[0] = vector[0]/mag
    vector[1] = vector[1]/mag
    vector[2] = vector[2]/mag

#Return the dot porduct of a . b
def dot_product(a, b):
    return (a[0]*b[0]+a[1]*b[1]+a[2]*b[2])

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = polygons[i]
    p1 = polygons[i+1]
    p2 = polygons[i+2]
    p0_p1 = [p1[0]-p0[0],
             p1[1]-p0[1],
             p1[2]-p0[2]]
    p0_p2 = [p2[0]-p0[0],
             p2[1]-p0[1],
             p2[2]-p0[2]]
    return cross_product(p0_p1,p0_p2)
