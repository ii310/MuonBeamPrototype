from vpython import *
import csv

timestamps = []
exposures = [[] for _ in range(4)]
t = 0


# Scene adjustments
scene.background = color.black
scene.width = 1400
scene.height = 700
scene.title = "Muon Beam Alignment Prototype"
scene.range = 10
scene.center = vector(5, 0, 0)

# Constants of Physics 
q = 1  #Coulomb = 1.6e-19 (too small to be seen in real world) for toggle the situation coulomb taken as 1
m = 1  # same thing for simplification the mass taken as 1
dt = 0.01 #Time step: advances by this value for each simulation cycle.
B_regions = [(0, 5, 0.5), (10, 12.5, -2)]  #(start_x, end_x, Bz)


for start, end, strength in B_regions:  # Set a start, end, and intensity value for each magnetic field region
    center_x = (start + end) / 2
    size_x = end - start
    box(pos=vector(center_x, 0, 0), size=vector(size_x, 8, 3), color=color.cyan if strength > 0 else color.magenta, opacity=0.2) 
    # The B field is positive shown in blue, if it is negative in shown purple
    

target = box(pos=vector(25, 5, 0), size=vector(0.8, 2, 3), color=color.green, opacity=0.5)


bfields_label = label(text='Multiple B-fields active', pos=vector(6, 8, 0), height=18, color=color.white, box=False, opacity=0)  # Texts showing that there is more than one active magnetic field
hit_label = label(text='', pos=vector(10, 6, 0), height=18, color=color.magenta, box=False, opacity=0) # the text here will be updated when the particle hits the target


initial_ys = [-5, -3, 5, 2] # Particle Launcher Function 
particles = []

for y in initial_ys:
    p = sphere(pos=vector(-5, y, 0), radius=0.2, color=color.red, make_trail=True, trail_type="points", interval=10, trail_radius=0.05)
    p.velocity = vector(5, 0, 0)   # Initial velocity (v) → only in x direction
    p.initial_velocity = vector(5, 0, 0) # First speed record (before entering the magnetic field effect)
    p.field_activated = False # checks if its contact with the magnetic field
    p.magnetic_exposure = 0  # measures how long it stays in a magnetic field
    particles.append(p)


def get_B(x, y): #  Get Field B by Position
    for start, end, strength in B_regions:
        if start <= x <= end and -4 <= y <= 4:
            return vector(0, 0, strength)
    return vector(0, 0, 0)
"""
Determines which magnetic field it is in, based on the given x and y positions
If it is in the magnetic field, it returns the B vector, otherwise the vector is zero
"""


def check_collision(p, target): # Collision Detection
    dx = abs(p.x - target.pos.x)
    dy = abs(p.y - target.pos.y)
    dz = abs(p.z - target.pos.z)
    sx, sy, sz = target.size.x/2, target.size.y/2, target.size.z/2
    return dx <= sx and dy <= sy and dz <= sz

"""
Checks if the particle hits the target box
Collision is determined by distance controls on the x, y, and z axes
"""



while t < 800: # Simulation Cycle
    rate(100)
    
    timestamps.append(round(t * dt, 3))
    for i, p in enumerate(particles):
        exposures[i].append(round(p.magnetic_exposure, 3))

    
    for p in particles:
        B = get_B(p.pos.x, p.pos.y)
        if B != vector(0,0,0):
            F = q * cross(p.velocity, B) # Lorentz Force : F = q (v x B)
            a = F / m                    # Acceleration: a = F / m
            p.velocity += a * dt         # Updating the speed: v = v + a * dt
            p.field_activated = True
            p.magnetic_exposure += dt  # The time spent in the magnetic field is increasing
        else:
            if not p.field_activated:
                p.velocity = p.initial_velocity # If it is not affected by the field, the straight linear motion continues

        p.pos += p.velocity * dt  # Lastly update with position formula: x = x + v*dt
        
        
        if check_collision(p.pos, target):
            p.color = color.magenta
            hit_label.text = f" The particle hit the target\nExposure: {round(p.magnetic_exposure, 3)} s"
    t += 1
    
with open('exposure_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Time', 'P1', 'P2', 'P3', 'P4'])
    for i in range(len(timestamps)):
        writer.writerow([timestamps[i]] + [exposures[j][i] for j in range(4)])

print("The data saved to exposure_data.csv file ")
    
