import matplotlib
matplotlib.use('Agg') # Non-interactive backend
import physanim
from physanim.systems import DoublePendulum
import matplotlib.pyplot as plt
import os

# Create the simulation
pendulum = DoublePendulum(t_max=2.0)

print("Starting animation calculation...")
try:
    # We will try to save to a gif if possible, using pillow if ffmpeg is not there
    # But first let's just create the object to verify physics calculation
    anim = physanim.animate(pendulum, frames=50, interval=50) # No filename = no save = just calculate
    print("Animation object created successfully. Physics logic works.")
    
    # Optional: Try to save a single frame to verify plotting
    anim.save('test_anim.gif', writer='pillow', fps=10)
    print("Animation saved as test_anim.gif")

except Exception as e:
    print(f"Error: {e}")

print("Done.")
