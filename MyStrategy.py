from model.Car import Car
from model.Game import Game
from model.Move import Move
from model.World import World
import math


class MyStrategy:
	def move(self, me: Car, world: World, game: Game, move: Move):
		
		def log(log_msg):
			print(world.tick, ': ', str(log_msg))
		def dotproduct(v1, v2):
			return sum((a*b) for a, b in zip(v1, v2))
		def length(v):
			return math.sqrt(dotproduct(v, v))
		def angle(v1, v2):
			return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
		def vector_to_polar(v):
			# returns between -Pi to +Pi
			result = []
			result.append(length(v))
			if v[1] > 0:
				result.append(angle([0,1],v))
			else:
				result.append(0 - angle([0,1],v))
			return result

		# need to find all visible tiles
		# in them determine waypoints
		# analyze track and add more 'waypoints'
		# define best racing line through known waypoints
		# define speed / braking

		v_tiles = []
		#for tile in world.tiles_x_y:
			#tile_distance = abs(tile.x-me.x)+abs(tile.y-me.y)
			#if tile_distance < 3:
			#    v_tiles.append(tile)

		if world.tick > game.initial_freeze_duration_ticks + 1:
			#log(world.waypoints)
			target_x = (me.next_waypoint_x + 1 - 1) * 800 + 400
			target_y = (me.next_waypoint_y + 1 - 1) * 800 + 400
			log('target_x:' + str(target_x))
			log('target_y:' + str(target_y))
			log('me_x:' + str(me.x))
			log('me_y:' + str(me.y))

			vN = [1,0]

			v2 = [] # vector to target
			v2.append(target_x-me.x)
			v2.append(target_y-me.y)
			
			v1 = [] # vector of current movement
			v1.append(me.speed_x*10)
			v1.append(me.speed_y*10)

			log(v1)
			log(v2)

			vr1 = vector_to_polar(v1)
			vr2 = vector_to_polar(v2)

			log(vr1)
			log(vr2)

			# d1 = angle(v0, v1)
			# d2 = angle(v0, v2)

			vr1[1] = vr1[1] + me.wheel_turn

			if vr1[1] < vr2[1]:
				move.wheel_turn = 1
			elif vr1[1] > vr2[1]:
				move.wheel_turn = -1
			else:
				move.wheel_turn = 0

			#target_angle = angle(v1,v2) / math.pi * 360;
			# log('angle:' + str(target_angle))

			# a = target_x-me.x
			# b = target_y-me.y
			# c = me.speed_x*10
			# d = me.speed_y*10

			# atanA = math.atan2(a, b)
			# atanB = math.atan2(c, d)
			# diff = atanA - atanB
			# # log(str(atanA))
			# # log(str(atanB))
			# # log(str(diff))
			# # if (diff > math.pi/2):
			# # 	diff = diff - math.pi
			# log(str(diff))

			#if (abs(diff)>0.01):
			# if (diff < 0):
			# 	move.wheel_turn = -1 * math.pow(abs(diff) / math.pi, 1/4)
			# if (diff > 0):
			# 	move.wheel_turn = 1 * math.pow(abs(diff) / math.pi, 1/4)
			# 	if (diff > 0.1):
			# 		#move.brake = True
			# 		move.engine_power = 0.1
			# 	if (diff <= 0.1):
			# 		#move.brake = False
			# 		move.engine_power = 1
			# if (abs(diff)<=0.01):
			# 	move.wheel_turn = 0
			move.engine_power = 0.1
			log(str(me.wheel_turn))

		else:
			# do until game starts
			move.engine_power = 1

		#move.throw_projectile = True
		#move.spill_oil = True

		#if world.tick > game.initial_freeze_duration_ticks:
		#    move.use_nitro = True