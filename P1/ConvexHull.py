import numpy as np
import random
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp
dots = []
#for i in range(20):
    #dots.append( [random.randint(0,50)+random.gauss(0,0.5), random.randint(0,50)+random.gauss(0,0.5),random.randint(0,50)+random.gauss(0,0.5)] )
    #dots.append( [random.randint(0,10), random.randint(0,10), random.randint(0,10)] )
    #dots.append( [random.gauss(0.5,0.4), random.gauss(0.5,0.4), random.gauss(0.5,0.3)] )
#print(dots)
dots = [[0.6871724204003699, 0.14061589802146912, 0.49575374071684664], [0.6089032412442505, 0.712211060787988, 0.30919586540262867], [0.7499119954500788, 0.5835718631333289, 0.1618510956263916], [0.23713334649561585, 0.848645563527129, 0.2224979258091498], [1.4168086666522535, 0.0885329162236898, 0.8202538987748775], [0.21124847824245113, 0.3718500239624438, 0.2890634362798201], [0.7002414050057275, 0.5328666311301388, 0.37847836791059597], [0.4249050555927536, 0.5603442820430518, 0.5112425885275045], [0.872755120365583, 0.9608102627140216, 0.20093107787716158], [0.481901424626459, 0.7910094711036344, -0.1190770902390047], [0.6914923077497672, 0.9324838213642904, 0.46493277609212], [-0.21608811694737462, 0.26417830713953716, 0.36913322898306555], [0.5159237805939002, 0.0628980821817074, 0.5287532058097455], [0.844826288278378, 0.8827975764211702, 0.5826090799313767], [0.9798435882863281, 0.6039395037506583, 0.519327205263183], [0.22252863362505793, 0.15320038211516723, 0.11774851691992311], [0.3929299069168425, -0.1380160536092081, 0.5430131788727345], [0.25375626922878236, 0.7552837324090358, 0.05169807948666111], [0.9247314019024715, 0.06477771674128668, 0.05124505311857014], [0.2428248773875572, 1.019084581945287, 0.6680460130181842]]

convex_surface = [ [dots[0], dots[1], dots[2]],  [dots[2], dots[1], dots[0]]] 

del dots[0:3]

dic_2d = {'b': {'a': 6}} # a temp dic
###############################
def dic_update(key1, key2, val):
    if key1 in dic_2d:
        dic_2d[key1].update({key2:val})
    else:
        dic_2d.update({key1:{key2:val}})

###############################
for point in dots:
    temp = []
    for surface in convex_surface:
        edge1 = np.array(surface[1]) - np.array(surface[0])
        edge2 = np.array(surface[2]) - np.array(surface[0])
        # diffrernt from cross product of matrix
        cross_vector = np.array( [edge1[1]*edge2[2]-edge2[1]*edge1[2], edge2[0]*edge1[2]-edge1[0]*edge2[2], edge1[0]*edge2[1]-edge2[0]*edge1[1] ])
        # cross product of vector
        
        # dot product of vector
        vector1 = np.array(point) - np.array(surface[0])
        dot_result1  = np.dot(vector1, cross_vector.T)
        # dot_result1 = vector1[0]*cross_vector[0] + vector1[1]*cross_vector[1] + vector1[2]*cross_vector[2] 
        # dot_result >= 0 : above
        if dot_result1 < 0:
            temp.append(surface)

        dic_update(str(surface[0]), str(surface[1]), bool(dot_result1 >= 0))
        dic_update(str(surface[1]), str(surface[2]), bool(dot_result1 >= 0))
        dic_update(str(surface[2]), str(surface[0]), bool(dot_result1 >= 0))
        #print("sprade ")
    
    for surface in convex_surface:
        if dic_2d[str(surface[0])][str(surface[1])] and (not dic_2d[str(surface[1])][str(surface[0])]):
            temp.append( [surface[0], surface[1], point])

        if dic_2d[str(surface[1])][str(surface[2])] and (not dic_2d[str(surface[2])][str(surface[1])]):
            temp.append( [surface[1], surface[2], point])

        if dic_2d[str(surface[2])][str(surface[0])] and (not dic_2d[str(surface[0])][str(surface[2])]):
            temp.append( [surface[2], surface[0], point])
    convex_surface = temp

#print (convex_surface)

ax0 = a3.Axes3D(pl.figure())

for point in dots:
    x = point[0]
    y = point[1]
    z = point[2]
    ax0.scatter(x, y, z, c='b', marker='o')
    
for surface in convex_surface:
    for dot in surface:
        x = dot[0]
        y = dot[1]
        z = dot[2]
        ax0.scatter(x, y, z, c='r', marker='o')
        
     

ax = a3.Axes3D(pl.figure())
for test in convex_surface:
    test = np.array(test)
    # draw plant
    tri = a3.art3d.Poly3DCollection([test])
    tri.set_color(colors.rgb2hex(sp.rand(3)))
    tri.set_edgecolor('k')
    ax.add_collection3d(tri)
for point in dots:
    x = point[0]
    y = point[1]
    z = point[2]
    ax.scatter(x, y, z, c='r', marker='o')
    

    
pl.show()

        