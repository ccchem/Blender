import bpy
import math
import mathutils


#-----------------------------------------------------------------------


def print_lamps():
	for obj in bpy.data.objects:
		if obj.type == 'LAMP':
			lamp = obj.data
			print(obj.name)            
			print("   Type: " + lamp.type)
			print("   Location: " + repr(obj.location))
			print("   Energy: " + repr(lamp.energy))


#-----------------------------------------------------------------------


def point_at(obj, point):
	vec = obj.location - point
	obj.rotation_euler = vec.to_track_quat('Z', 'Y').to_euler()


#-----------------------------------------------------------------------


def add_spot(name, point):
	bpy.ops.object.lamp_add(type='SPOT', location=(point.x, point.y, point.z))
	
	obj = bpy.context.object
	obj.name = name
	
	point_at(obj, mathutils.Vector((0,0,0)))


