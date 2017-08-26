import math
import bpy


def add_cylinder(p1, p2, r):
	dx = p2.x - p1.x
	dy = p2.y - p1.y
	dz = p2.z - p1.z    
	dist = math.sqrt(dx*dx + dy*dy + dz*dz)
	
	phi = math.atan2(dy, dx)
	theta = math.acos(dz/dist)

	bpy.ops.mesh.primitive_cylinder_add(
		radius = r, 
		depth = dist,
		location = (dx/2.0 + p1.x, dy/2.0 + p1.y, dz/2.0 + p1.z),
		rotation = (0, theta, phi)
	)

