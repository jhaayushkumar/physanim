# PhysAnim

PhysAnim is a Python library designed to make physics simulations and animations effortless.

## 🚀 Key Features
- **Simulation Engine**: Easy-to-use abstract base for various physics systems.
- **Built-in Systems**: Double Pendulum, Spring-Mass, and N-Body Planetary simulations.
- **Theming**: Custom backgrounds, line colors, and motion trails.
- **Interactivity**: Real-time parameter tuning in Jupyter Notebooks.

## 📦 Installation

Basic installation:
```bash
pip install physanim
```

For interactive mode (Jupyter support):
```bash
pip install physanim[interactive]
```

## 🛠 Usage

### Standard Animation
```python
import physanim
from physanim.systems import DoublePendulum

pendulum = DoublePendulum()
physanim.animate(pendulum)
```

### Interactive Mode (Jupyter)
```python
from physanim import interact
from physanim.systems import DoublePendulum

interact(DoublePendulum, L1=(0.5, 3.0), m1=(1.0, 5.0))
```

## 📚 Resources
- **Documentation**: [https://jhaayushkumar.github.io/physanim/](https://jhaayushkumar.github.io/physanim/)
- **PyPI**: [https://pypi.org/project/physanim/](https://pypi.org/project/physanim/)
