# Computational Xmas Tree

This repo contains the code for my take on [the computational illumination of a Christmas Tree](https://github.com/GSD6338/XmasTree) for ["My 500-LED xmas tree got into Harvard."](https://www.youtube.com/watch?v=WuMRJf6B5Q4) submission.

It is based on the work by [Matt Parker](https://www.youtube.com/channel/UCSju5G2aFaWMqn-_0YBtq5A) from [@standupmaths](https://github.com/standupmaths/), and his video ["I wired my tree with 500 LED lights and calculated their 3D coordinates"](https://www.youtube.com/watch?v=TvlpIojusBE).

## Todo

[ ] Newton Fractal Animation
    [x] Polynomial
        [x] Polynomial from Roots
    [ ] Voronoi Diagram
        [x] Complex Number Magnitude
    [ ] Coloring
    [ ] Newton's Method
[ ] Command Line Input
    [ ] File Input
    [ ] File Output

## Usage

```s
$ python -m xmastree
```

### Testing

```s
$ python -m unittest discover -vs test
```

## Project Structure

```s
├── LICENSE
├── README.md
├── coords_2021.csv
└── xmastree
    ├── __init__.py
    ├── __main__.py
    ├── datatypes.py
    ├── fileio.py
    ├── mathutils
    │   ├── __init__.py
    │   ├── polynomial.py
    │   └── utils.py
    └── transform.py
```
