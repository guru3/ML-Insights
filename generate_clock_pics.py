import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def create_clock(angle1, angle2, angle3, filename):
	plt.figure(figsize=(10,10))
	background_color = 'red'
	hours_color = 'blue'
	minutes_color = 'green'
	seconds_color = 'orange'

	circle = plt.Circle((0,0), radius=1.0, fc=background_color)
	plt.gca().add_patch(circle)

	circle_origin = plt.Circle((0,0), radius=0.95, fc='white')
	plt.gca().add_patch(circle_origin)

	circle_origin = plt.Circle((0,0), radius=0.05, fc=background_color)
	plt.gca().add_patch(circle_origin)

	(x,y)= (np.sin(np.deg2rad(angle1)), np.cos(np.deg2rad(angle1)) )
	hour_line = plt.Line2D((0,0.6*x), (0,0.6*y), lw=16, color=hours_color)
	plt.gca().add_line(hour_line)

	(x,y)= (np.sin(np.deg2rad(angle2)), np.cos(np.deg2rad(angle2)) )
	hour_line = plt.Line2D((0,0.75*x), (0,0.75*y), lw=9, color=minutes_color)
	plt.gca().add_line(hour_line)

	(x,y)= (np.sin(np.deg2rad(angle3)), np.cos(np.deg2rad(angle3)) )
	hour_line = plt.Line2D((0,0.9*x), (0,0.9*y), lw=5, color=seconds_color)
	plt.gca().add_line(hour_line)

	plt.axis('scaled')
	plt.axis('off')
	plt.savefig(filename, bbox_inches='tight', dpi=40)
	plt.close('all')

def main():
	if not os.path.exists('./clocks'):
		os.mkdir('./clocks')
		
	sparse = False
	if len(sys.argv) > 1:
		sparse = int(sys.argv[1])
	
	if sparse:
		minute_sparsity = 5
		second_sparsity = 10
	else:
		minute_sparsity = 1
		second_sparsity = 1

	for hour in range(0,12):
		for minute in range(0,60, minute_sparsity):
			for second in range(0,60, second_sparsity):
				hour_angle = 30*( hour + minute/60 + second/3600) 
				minute_angle = 6*( minute + second/60)
				second_angle = 6*second
				filename = './clocks/clock_{}_{}_{}.jpg'.format(hour, minute, second)
				create_clock(hour_angle, minute_angle, second_angle, filename)

main()
