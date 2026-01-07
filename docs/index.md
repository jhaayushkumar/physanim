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

## 🎮 Interactive Mode

PhysAnim supports real-time parameter tuning within Jupyter Notebooks using `interact()`.

```python
from physanim import interact
from physanim.systems import DoublePendulum

# Create sliders for gravity, length, and masses
interact(DoublePendulum, g=(9.0, 10.0), L1=(0.5, 2.0), m1=(1.0, 5.0))
```
Note: Requires `pip install physanim[interactive]` and a Jupyter environment.

## Supported Systems

- `DoublePendulum`: Chaotic double pendulum.
- `SpringMass`: Simple harmonic oscillator.
- `PlanetarySystem`: N-body orbital simulation.

## Examples

### Cyberpunk Double Pendulum
![Double Pendulum](assets/demo_cyberpunk.gif)

### Spring Mass System
![Spring Mass](assets/demo_spring.gif)

### Planetary Orbit (Three-Body)
![Planetary System](assets/demo_planets.gif)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jhaayushkumar/physanim/blob/main/LICENSE) file for details.
