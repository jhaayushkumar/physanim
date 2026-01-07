# PhysAnim

Welcome to the official documentation for **PhysAnim**.

PhysAnim is a lightweight Python library for simulating and animating physics systems like pendulums, springs, and planetary orbits.

## Installation

```bash
pip install physanim
```

## Quick Start

```python
import physanim
from physanim.systems import DoublePendulum

# Create a customized double pendulum
pendulum = DoublePendulum(L1=1.0, L2=1.0, m1=1.0, m2=1.0)

# Theming
theme = {
    'background_color': '#222',
    'line_color': 'cyan',
    'trail_color': 'cyan',
    'trail_length': 20
}

# Animate
physanim.animate(pendulum, theme=theme)
```

## Supported Systems

- `DoublePendulum`: Chaotic double pendulum.
- `SpringMass`: Simple harmonic oscillator.
- `PlanetarySystem`: N-body orbital simulation.

## Examples

### Cyberpunk Double Pendulum
![Double Pendulum](docs/assets/demo_cyberpunk.gif)

### Spring Mass System
![Spring Mass](docs/assets/demo_spring.gif)

### Planetary Orbit (Three-Body)
![Planetary System](docs/assets/demo_planets.gif)
