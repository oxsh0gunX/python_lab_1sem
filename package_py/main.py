from graphics.circle import area as ca ,circumference as cc
from graphics.rectangle import area as ra ,perimeter as rp

from graphics.graphics_3d.cuboid import surface_area as csa ,edge_perimeter as cep
from graphics.graphics_3d.sphere import surface_area as ssa , volume as sv

print("rectangle with length =10 and breadth = 5 ,area and perimeter are :")
print(ra(10,5))
print(rp(10,5))

print("circle with radius 7 , area and circumference are :")
print(ca(7))
print(cc(7))

print("cuboid with length = 2, breadth = 3, height = 4, area and circumference are :")
print(csa(2,3,4))
print(cep(2,3,4))

print("sphere with radius = 5, surface_area and volume are :")
print(ssa(5))
print(sv(5))
