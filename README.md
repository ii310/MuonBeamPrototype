# Muon Beam Alignment Prototype 

The aim of the project was to model the behavior of charged particles (i.e. muon beams) moving in a magnetic field.
With VPython, it was visually and physically simulated that the particles change direction due to the Lorentz force and reach the target.

# How does the project work?
The simulation is defined by various magnetic field regions;
- The particles move in different ways as they pass through these fields, deflections occur.
- The particles that do not come into contact with the magnetic field move in a linear motion.
- The particles that hit the target box are tracked and the time they remain in the magnetic field is measured.

# Basic Physics Terms and Formulas Used

Lorentz Force: The force formula acting on a moving charged particle in a magnetic field is given below.

F = q (v×B)

In this context, "F" is the acting force (Newton), "q" is the particle's electric charge (Coulomb), "v" is the particle's velocity vector (m/s) and "B" is the magnetic field vector (Tesla) established:
- F : Acting force (Newton)
- q : Particle's electric charge (Coulomb)
- v : Particle's velocity vector (m/s)
- B : Magnetic field vector (Tesla)

The equations of motion update the velocity and position after calculating the force acceleration:

a = F/m
v_new = v + a + Δt
x_new = x + v_new + Δt

Collision Detection: Distance checks on the X, Y and Z axes determine whether the particles hit the target box.

# Installation and Implementation

1. Python 3.8+ must be installed on your computer to run the prototype.
2. You can use the following command to install the VPython library: bash pip install vpython.

# Data Logging (Optional)
You can record each particle’s magnetic field exposure during the simulation by using the following function:

```python
from save_exposure_data import save_exposure_data
save_exposure_data(timestamps, exposure_history)
```
This will create a file called exposure_data.csv containing time and exposure values for each particle

# MATLAB Visualization
To visualize and compare the exposure of particles over time, you can use the following simple MATLAB code
### What does the graph show?

- Each line represents a particle.
- Y-axis: time spent in magnetic fields.
- X-axis: total simulation time.
- Flat line → particle exited the magnetic field.
- Rising line → still inside a magnetic field.
- Helps compare:
  - How long each particle was affected,
  - The impact of initial position,
  - When particles hit the target.
