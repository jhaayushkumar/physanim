# PhysAnim

PhysAnim is a Python library for physics simulations and animations.

## Installation

```bash
pip install physanim
```

For Jupyter support:
```bash
pip install physanim[interactive]
```

## Usage

### Simple Animation
```python
import physanim
from physanim.systems import DoublePendulum

sim = DoublePendulum()
physanim.animate(sim)
```

### Interactive Sliders (Jupyter)
```python
from physanim import interact
from physanim.systems import DoublePendulum

interact(DoublePendulum, L1=(0.5, 3.0), m1=(1.0, 5.0))
```

## Links
- **Docs**: [https://jhaayushkumar.github.io/physanim/](https://jhaayushkumar.github.io/physanim/)
- **PyPI**: [https://pypi.org/project/physanim/](https://pypi.org/project/physanim/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
