import matplotlib
matplotlib.use('Agg')
import physanim
from physanim.systems import DoublePendulum, SpringMass, PlanetarySystem
import numpy as np

# 1. Custom Theme Double Pendulum
print("Generating Themed Double Pendulum...")
pendulum = DoublePendulum(t_max=5.0)
cyber_theme = {
    'background_color': '#111111',
    'line_color': '#00ff00', # Neon Green
    'trail_color': '#00ff00',
    'trail_length': 40,
    'grid_color': '#222222'
}
anim = physanim.animate(pendulum, filename='demo_cyberpunk.gif', theme=cyber_theme)


# 2. Spring Mass System
print("Generating Spring Mass System...")
spring = SpringMass(k=50.0, m=1.0, length=2.0, t_max=0.0) # t_max should be > 0, oops fixing in args
spring.t_max = 5.0
anim_spring = physanim.animate(spring, filename='demo_spring.gif')


# 3. Planetary System (3-body Figure 8)
print("Generating Planetary System...")
# Figure-8 Initial conditions (approximate)
p1 = [-0.97000436, 0.24308753]
p2 = [0.97000436, -0.24308753]
p3 = [0.0, 0.0]
v1 = [0.46620368, 0.43236573]
v2 = [0.46620368, 0.43236573]
v3 = [-2*0.46620368, -2*0.43236573]

planets = PlanetarySystem(
    masses=[1, 1, 1],
    positions=[p1, p2, p3],
    velocities=[v1, v2, v3],
    t_max=6.3 # rough period
)
# For planets, we might want to hide the connecting line and just see trails? 
# our simple core.py doesn't strictly support separate trails yet, but let's see what happens.
planet_theme = {
    'background_color': 'black',
    'line_color': 'orange',
    'trail_length': 100,
    'trail_color': 'white'
}
anim_planets = physanim.animate(planets, filename='demo_planets.gif', theme=planet_theme)

print("All demos finished.")
