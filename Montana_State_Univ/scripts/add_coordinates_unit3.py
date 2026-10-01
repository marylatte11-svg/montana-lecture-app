"""
add_coordinates_unit3.py
Adds coordinate grid data to all Unit 3 slides that involve quadratic functions.
Patches montanaSlidesData.js directly by replacing slide objects.
Strategy: Parse each function from slide content and add appropriate parabola data.
"""
import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

# ─────────────────────────────────────────────────────────────
# COORDINATE DATA: Each entry = (lectureId, slideNum, coordinate_dict)
# Based on the actual quadratic functions in each slide
# ─────────────────────────────────────────────────────────────

COORDINATE_ADDITIONS = {

    # ── L31: Intro to Quadratic Functions ──────────────────────────
    # Slide 3: f(x) = -x^2 + 3x + 8  → opens down, vertex at (1.5, 10.25)
    (31, 3): {
        "xMin": -3, "xMax": 6, "yMin": -5, "yMax": 14,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": -1, "b": 3, "c": 8, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": 1.5, "y": 10.25, "color": "#ffd700", "label": "V(1.5,10.25)"},
            {"x": 0, "y": 8, "color": "#00ff88", "label": "(0,8)"},
            {"x": -2, "y": 0, "color": "#ff6b6b", "label": "(-2,0)"},
            {"x": 4, "y": 0, "color": "#ff6b6b", "label": "(4,0)"}
        ],
        "axisOfSymmetry": 1.5
    },
    # Slide 4: f(x) = 2x^2 - 7  → opens up, vertex at (0, -7)
    (31, 4): {
        "xMin": -3, "xMax": 3, "yMin": -9, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 2, "b": 0, "c": -7, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 0, "y": -7, "color": "#ffd700", "label": "V(0,-7)"},
            {"x": 1.87, "y": 0, "color": "#ff6b6b", "label": "(1.87,0)"},
            {"x": -1.87, "y": 0, "color": "#ff6b6b", "label": "(-1.87,0)"}
        ],
        "axisOfSymmetry": 0
    },
    # Slide 7: Parabola Direction — opening up (a>0) vs down (a<0)
    (31, 7): {
        "xMin": -4, "xMax": 4, "yMin": -10, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": 1, "b": 0, "c": 0, "color": "#00d4ff", "strokeWidth": 3, "label": "a>0 opens up"},
            {"a": -1, "b": 0, "c": 0, "color": "#ff9500", "strokeWidth": 3, "label": "a<0 opens down"}
        ],
        "points": [
            {"x": 0, "y": 0, "color": "#ffd700", "label": "Vertex"}
        ]
    },

    # ── L32: Vertex & Intercepts from graphs ────────────────────────
    # Slide 1: Anatomy of a parabola — generic upward parabola
    (32, 1): {
        "xMin": -4, "xMax": 4, "yMin": -6, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -2, "c": -3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": -4, "color": "#ffd700", "label": "Vertex"},
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 0, "y": -3, "color": "#00ff88", "label": "y-int"}
        ],
        "axisOfSymmetry": 1
    },
    # Slide 2: f(x) = x^2 - 9  (intercepts)
    (32, 2): {
        "xMin": -5, "xMax": 5, "yMin": -12, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": 0, "c": -9, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 0, "y": -9, "color": "#ffd700", "label": "V(0,-9)"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
            {"x": -3, "y": 0, "color": "#ff6b6b", "label": "(-3,0)"}
        ],
        "axisOfSymmetry": 0
    },
    # Slide 3: f(x) = x^2 - 9 vertex
    (32, 3): {
        "xMin": -5, "xMax": 5, "yMin": -12, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": 0, "c": -9, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 0, "y": -9, "color": "#ffd700", "label": "V(0,-9)"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
            {"x": -3, "y": 0, "color": "#ff6b6b", "label": "(-3,0)"},
            {"x": 0, "y": -9, "color": "#ffd700", "label": "min=-9"}
        ],
        "axisOfSymmetry": 0
    },
    # Slide 4: f(x)=x^2-9 domain/range
    (32, 4): {
        "xMin": -5, "xMax": 5, "yMin": -12, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": 0, "c": -9, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 0, "y": -9, "color": "#ffd700", "label": "min y=-9"},
        ],
        "axisOfSymmetry": 0
    },
    # Slide 5: f(x) = -2(x+1)^2 + 8  → vertex form → vertex (-1, 8)
    (32, 5): {
        "xMin": -5, "xMax": 3, "yMin": -5, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": -2, "b": -4, "c": 6, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": -1, "y": 8, "color": "#ffd700", "label": "V(-1,8)"},
        ],
        "axisOfSymmetry": -1
    },
    # Slide 6: f(x) = -2(x+1)^2 + 8 vertex & axis
    (32, 6): {
        "xMin": -5, "xMax": 3, "yMin": -5, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": -2, "b": -4, "c": 6, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": -1, "y": 8, "color": "#ffd700", "label": "V(-1,8) MAX"},
            {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
            {"x": -3, "y": 0, "color": "#ff6b6b", "label": "(-3,0)"}
        ],
        "axisOfSymmetry": -1
    },
    # Slide 7: max value and range
    (32, 7): {
        "xMin": -5, "xMax": 3, "yMin": -5, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": -2, "b": -4, "c": 6, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": -1, "y": 8, "color": "#ffd700", "label": "max=8"},
        ],
        "axisOfSymmetry": -1
    },

    # ── L33: Function Evaluation ─────────────────────────────────────
    # Slide 7: negative base trap — show -x^2 vs (-x)^2
    (33, 7): {
        "xMin": -4, "xMax": 4, "yMin": -12, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": -1, "b": 0, "c": 0, "color": "#ff6b6b", "strokeWidth": 3, "label": "-x^2"},
            {"a": 1, "b": 0, "c": 0, "color": "#00d4ff", "strokeWidth": 2, "dashed": True, "label": "(-x)^2=x^2"}
        ],
        "points": [{"x": 0, "y": 0, "color": "#ffd700", "label": "origin"}]
    },

    # ── L34: Vertex Formula ──────────────────────────────────────────
    # Slide 2: f(x) = x^2 + 6x - 4  → vertex (-3, -13)
    (34, 2): {
        "xMin": -7, "xMax": 2, "yMin": -15, "yMax": 10,
        "xTicks": 1, "yTicks": 3,
        "curves": [{"a": 1, "b": 6, "c": -4, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": -3, "y": -13, "color": "#ffd700", "label": "V(-3,-13)"},
            {"x": 0, "y": -4, "color": "#00ff88", "label": "(0,-4)"}
        ],
        "axisOfSymmetry": -3
    },
    # Slide 3: f(x) = (1/2)x^2 - 3x + 5  → vertex (3, 0.5)
    (34, 3): {
        "xMin": -1, "xMax": 7, "yMin": -1, "yMax": 10,
        "xTicks": 1, "yTicks": 1,
        "curves": [{"a": 0.5, "b": -3, "c": 5, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 3, "y": 0.5, "color": "#ffd700", "label": "V(3,0.5)"},
            {"x": 0, "y": 5, "color": "#00ff88", "label": "(0,5)"}
        ],
        "axisOfSymmetry": 3
    },
    # Slide 4: Why x=-b/2a works — midpoint of roots
    (34, 4): {
        "xMin": -2, "xMax": 6, "yMin": -6, "yMax": 6,
        "xTicks": 1, "yTicks": 1,
        "curves": [{"a": 1, "b": -4, "c": 3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": 0, "color": "#ff6b6b", "label": "r1"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "r2"},
            {"x": 2, "y": -1, "color": "#ffd700", "label": "V(midpoint)"}
        ],
        "axisOfSymmetry": 2
    },
    # Slide 6: f(x) = -2x^2 + 8x - 3  → vertex (2, 5)
    (34, 6): {
        "xMin": -1, "xMax": 5, "yMin": -6, "yMax": 8,
        "xTicks": 1, "yTicks": 1,
        "curves": [{"a": -2, "b": 8, "c": -3, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": 5, "color": "#ffd700", "label": "V(2,5)"},
            {"x": 0, "y": -3, "color": "#00ff88", "label": "(0,-3)"},
            {"x": 0.42, "y": 0, "color": "#ff6b6b", "label": "(0.42,0)"},
            {"x": 3.58, "y": 0, "color": "#ff6b6b", "label": "(3.58,0)"}
        ],
        "axisOfSymmetry": 2
    },
    # Slide 7: Visualizing vertex on grid
    (34, 7): {
        "xMin": -4, "xMax": 6, "yMin": -8, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -2, "c": -3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": -4, "color": "#ffd700", "label": "V(1,-4)"},
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "(-1,0)"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
            {"x": 0, "y": -3, "color": "#00ff88", "label": "(0,-3)"}
        ],
        "axisOfSymmetry": 1
    },

    # ── L35: Vertex Form Examples ────────────────────────────────────
    # Slide 1: f(x) = -3(x-4)^2 + 7 → vertex (4,7), opens down
    (35, 1): {
        "xMin": 0, "xMax": 8, "yMin": -5, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": -3, "b": 24, "c": -41, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": 4, "y": 7, "color": "#ffd700", "label": "V(4,7)"},
            {"x": 2.47, "y": 0, "color": "#ff6b6b", "label": "(2.47,0)"},
            {"x": 5.53, "y": 0, "color": "#ff6b6b", "label": "(5.53,0)"}
        ],
        "axisOfSymmetry": 4
    },
    # Slide 2: f(x) = 5(x-1)^2 + 3 → vertex (1,3), no x-intercepts
    (35, 2): {
        "xMin": -2, "xMax": 4, "yMin": -1, "yMax": 25,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 5, "b": -10, "c": 8, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": 3, "color": "#ffd700", "label": "V(1,3)"},
            {"x": 0, "y": 8, "color": "#00ff88", "label": "(0,8)"}
        ],
        "axisOfSymmetry": 1
    },
    # Slide 3: f(x) = -6(x+2)^2 - 9 → vertex (-2,-9), opens down, no x-intercepts
    (35, 3): {
        "xMin": -5, "xMax": 1, "yMin": -20, "yMax": 2,
        "xTicks": 1, "yTicks": 4,
        "curves": [{"a": -6, "b": -24, "c": -33, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": -2, "y": -9, "color": "#ffd700", "label": "V(-2,-9)"},
            {"x": 0, "y": -33, "color": "#00ff88", "label": "y-int"}
        ],
        "axisOfSymmetry": -2
    },
    # Slide 4: f(x) = 2x^2 - 7 → vertex (0,-7)
    (35, 4): {
        "xMin": -3, "xMax": 3, "yMin": -9, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 2, "b": 0, "c": -7, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 0, "y": -7, "color": "#ffd700", "label": "V(0,-7)"},
            {"x": 1.87, "y": 0, "color": "#ff6b6b", "label": "(1.87,0)"},
            {"x": -1.87, "y": 0, "color": "#ff6b6b", "label": "(-1.87,0)"}
        ],
        "axisOfSymmetry": 0
    },
    # Slide 5: Comprehensive f(x) = -(x-2)^2 + 9 → vertex (2,9), opens down
    (35, 5): {
        "xMin": -2, "xMax": 6, "yMin": -5, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": -1, "b": 4, "c": 5, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": 9, "color": "#ffd700", "label": "V(2,9)"},
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "(-1,0)"},
            {"x": 5, "y": 0, "color": "#ff6b6b", "label": "(5,0)"},
            {"x": 0, "y": 5, "color": "#00ff88", "label": "(0,5)"}
        ],
        "axisOfSymmetry": 2
    },
    # Slide 6: Graph interrogation of same function
    (35, 6): {
        "xMin": -2, "xMax": 6, "yMin": -5, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": -1, "b": 4, "c": 5, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": 9, "color": "#ffd700", "label": "MAX (2,9)"},
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "(-1,0)"},
            {"x": 5, "y": 0, "color": "#ff6b6b", "label": "(5,0)"}
        ],
        "axisOfSymmetry": 2
    },

    # ── L36: Square Root Property ────────────────────────────────────
    # Slide 3: x^2 = 16 → x = ±4  (show y = x^2 and y = 16)
    (36, 3): {
        "xMin": -6, "xMax": 6, "yMin": -5, "yMax": 25,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 1, "b": 0, "c": 0, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 4, "y": 16, "color": "#ff6b6b", "label": "(4,16)"},
            {"x": -4, "y": 16, "color": "#ff6b6b", "label": "(-4,16)"},
            {"x": 0, "y": 0, "color": "#ffd700", "label": "V(0,0)"}
        ]
    },
    # Slide 4: 2x^2 + 2 = 10 → x^2 = 4 → x = ±2  f(x) = 2x^2 + 2
    (36, 4): {
        "xMin": -4, "xMax": 4, "yMin": -2, "yMax": 15,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 2, "b": 0, "c": 2, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": 10, "color": "#ff6b6b", "label": "(2,10)"},
            {"x": -2, "y": 10, "color": "#ff6b6b", "label": "(-2,10)"},
            {"x": 0, "y": 2, "color": "#ffd700", "label": "V(0,2)"}
        ]
    },
    # Slide 5: f(x) = x^2 - 16 → x-intercepts ±4, vertex (0,-16)
    (36, 5): {
        "xMin": -6, "xMax": 6, "yMin": -18, "yMax": 10,
        "xTicks": 1, "yTicks": 4,
        "curves": [{"a": 1, "b": 0, "c": -16, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 4, "y": 0, "color": "#ff6b6b", "label": "(4,0)"},
            {"x": -4, "y": 0, "color": "#ff6b6b", "label": "(-4,0)"},
            {"x": 0, "y": -16, "color": "#ffd700", "label": "V(0,-16)"}
        ],
        "axisOfSymmetry": 0
    },
    # Slide 6: g(x) = 3x^2 - 27 → intercepts ±3, vertex (0,-27)
    (36, 6): {
        "xMin": -5, "xMax": 5, "yMin": -30, "yMax": 10,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 3, "b": 0, "c": -27, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
            {"x": -3, "y": 0, "color": "#ff6b6b", "label": "(-3,0)"},
            {"x": 0, "y": -27, "color": "#ffd700", "label": "V(0,-27)"}
        ],
        "axisOfSymmetry": 0
    },
    # Slide 7: x^2 = -9 → no real solution (floats above x-axis)
    (36, 7): {
        "xMin": -4, "xMax": 4, "yMin": -2, "yMax": 20,
        "xTicks": 1, "yTicks": 4,
        "curves": [{"a": 1, "b": 0, "c": 9, "color": "#ff6b6b", "strokeWidth": 3}],
        "points": [
            {"x": 0, "y": 9, "color": "#ffd700", "label": "V(0,9)"}
        ]
    },

    # ── L37: Binomial Square Root Property ──────────────────────────
    # Slide 2: (x-3)^2 = 25 → x=8 or x=-2
    (37, 2): {
        "xMin": -4, "xMax": 10, "yMin": -5, "yMax": 35,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 1, "b": -6, "c": 9, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 8, "y": 25, "color": "#ff6b6b", "label": "(8,25)"},
            {"x": -2, "y": 25, "color": "#ff6b6b", "label": "(-2,25)"},
            {"x": 3, "y": 0, "color": "#ffd700", "label": "V(3,0)"}
        ],
        "axisOfSymmetry": 3
    },
    # Slide 3: f(x) = (x+2)^2 - 9 → vertex (-2,-9), intercepts 1 and -5
    (37, 3): {
        "xMin": -7, "xMax": 4, "yMin": -12, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": 4, "c": -5, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": -2, "y": -9, "color": "#ffd700", "label": "V(-2,-9)"},
            {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
            {"x": -5, "y": 0, "color": "#ff6b6b", "label": "(-5,0)"},
            {"x": 0, "y": -5, "color": "#00ff88", "label": "(0,-5)"}
        ],
        "axisOfSymmetry": -2
    },
    # Slide 4: 2(x-4)^2 = 32 → (x-4)^2=16 → x=8 or x=0
    (37, 4): {
        "xMin": -1, "xMax": 10, "yMin": -5, "yMax": 40,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 2, "b": -16, "c": 32, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 8, "y": 32, "color": "#ff6b6b", "label": "x=8"},
            {"x": 0, "y": 32, "color": "#ff6b6b", "label": "x=0"},
            {"x": 4, "y": 0, "color": "#ffd700", "label": "V(4,0)"}
        ],
        "axisOfSymmetry": 4
    },
    # Slide 5: (x-2)^2 = 7 → x = 2 ± √7 ≈ 4.65 or -0.65
    (37, 5): {
        "xMin": -2, "xMax": 6, "yMin": -5, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -4, "c": -3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 4.65, "y": 0, "color": "#ff6b6b", "label": "(2+√7,0)"},
            {"x": -0.65, "y": 0, "color": "#ff6b6b", "label": "(2-√7,0)"},
            {"x": 2, "y": -7, "color": "#ffd700", "label": "V(2,-7)"}
        ],
        "axisOfSymmetry": 2
    },

    # ── L38: Factoring ───────────────────────────────────────────────
    # Slide 2: x^2 - 5x + 6 = 0 → roots x=2, x=3
    (38, 2): {
        "xMin": -1, "xMax": 5, "yMin": -5, "yMax": 8,
        "xTicks": 1, "yTicks": 1,
        "curves": [{"a": 1, "b": -5, "c": 6, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": 0, "color": "#ff6b6b", "label": "(2,0)"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
            {"x": 2.5, "y": -0.25, "color": "#ffd700", "label": "V(2.5,-0.25)"},
            {"x": 0, "y": 6, "color": "#00ff88", "label": "(0,6)"}
        ],
        "axisOfSymmetry": 2.5
    },
    # Slide 3: f(x) = x^2 + 2x - 8 → roots -4, 2; vertex (-1,-9)
    (38, 3): {
        "xMin": -6, "xMax": 4, "yMin": -12, "yMax": 8,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": 2, "c": -8, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": -4, "y": 0, "color": "#ff6b6b", "label": "(-4,0)"},
            {"x": 2, "y": 0, "color": "#ff6b6b", "label": "(2,0)"},
            {"x": -1, "y": -9, "color": "#ffd700", "label": "V(-1,-9)"},
            {"x": 0, "y": -8, "color": "#00ff88", "label": "(0,-8)"}
        ],
        "axisOfSymmetry": -1
    },
    # Slide 4: 2x^2 - 8x = 0 → GCF → x=0 or x=4; vertex (2,-8)
    (38, 4): {
        "xMin": -1, "xMax": 6, "yMin": -10, "yMax": 6,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 2, "b": -8, "c": 0, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 0, "y": 0, "color": "#ff6b6b", "label": "(0,0)"},
            {"x": 4, "y": 0, "color": "#ff6b6b", "label": "(4,0)"},
            {"x": 2, "y": -8, "color": "#ffd700", "label": "V(2,-8)"}
        ],
        "axisOfSymmetry": 2
    },
    # Slide 5: 4x^2 - 25 = 0 → x = ±5/2 = ±2.5
    (38, 5): {
        "xMin": -4, "xMax": 4, "yMin": -30, "yMax": 10,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 4, "b": 0, "c": -25, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 2.5, "y": 0, "color": "#ff6b6b", "label": "(2.5,0)"},
            {"x": -2.5, "y": 0, "color": "#ff6b6b", "label": "(-2.5,0)"},
            {"x": 0, "y": -25, "color": "#ffd700", "label": "V(0,-25)"}
        ],
        "axisOfSymmetry": 0
    },

    # ── L39: Advanced Factoring ──────────────────────────────────────
    # Slide 1: 2x^2 + 7x + 3 = 0 → roots x=-3, x=-1/2
    (39, 1): {
        "xMin": -5, "xMax": 2, "yMin": -5, "yMax": 15,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 2, "b": 7, "c": 3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": -3, "y": 0, "color": "#ff6b6b", "label": "(-3,0)"},
            {"x": -0.5, "y": 0, "color": "#ff6b6b", "label": "(-0.5,0)"},
            {"x": -1.75, "y": -3.125, "color": "#ffd700", "label": "V(-1.75,-3.13)"}
        ],
        "axisOfSymmetry": -1.75
    },
    # Slide 2: g(x) = 3x^2 - 10x - 8 → roots x=4, x=-2/3
    (39, 2): {
        "xMin": -2, "xMax": 6, "yMin": -18, "yMax": 12,
        "xTicks": 1, "yTicks": 4,
        "curves": [{"a": 3, "b": -10, "c": -8, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 4, "y": 0, "color": "#ff6b6b", "label": "(4,0)"},
            {"x": -0.67, "y": 0, "color": "#ff6b6b", "label": "(-2/3,0)"},
            {"x": 1.67, "y": -16.33, "color": "#ffd700", "label": "V(1.67,-16.3)"}
        ],
        "axisOfSymmetry": 1.67
    },
    # Slide 3: -x^2 + 4x - 3 = 0 → opens down, roots x=1, x=3; vertex (2,1)
    (39, 3): {
        "xMin": -1, "xMax": 5, "yMin": -5, "yMax": 4,
        "xTicks": 1, "yTicks": 1,
        "curves": [{"a": -1, "b": 4, "c": -3, "color": "#ff9500", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
            {"x": 2, "y": 1, "color": "#ffd700", "label": "V(2,1)"}
        ],
        "axisOfSymmetry": 2
    },
    # Slide 4: Exactly one x-intercept — tangent vertex: f(x) = x^2 - 4x + 4 = (x-2)^2
    (39, 4): {
        "xMin": -1, "xMax": 5, "yMin": -1, "yMax": 10,
        "xTicks": 1, "yTicks": 1,
        "curves": [{"a": 1, "b": -4, "c": 4, "color": "#00ff88", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": 0, "color": "#ffd700", "label": "V(2,0) tangent!"}
        ],
        "axisOfSymmetry": 2
    },
    # Slide 5: Three possibilities — show all 3 cases
    (39, 5): {
        "xMin": -4, "xMax": 4, "yMin": -5, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": 1, "b": 0, "c": -4, "color": "#00d4ff", "strokeWidth": 2, "label": "2 intercepts"},
            {"a": 1, "b": 0, "c": 0, "color": "#ffd700", "strokeWidth": 2, "label": "1 intercept"},
            {"a": 1, "b": 0, "c": 4, "color": "#ff6b6b", "strokeWidth": 2, "label": "0 intercepts"}
        ]
    },
    # Slide 6: Factored form to graph: f(x) = (x-1)(x-5) = x^2 - 6x + 5
    (39, 6): {
        "xMin": -1, "xMax": 7, "yMin": -6, "yMax": 8,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -6, "c": 5, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
            {"x": 5, "y": 0, "color": "#ff6b6b", "label": "(5,0)"},
            {"x": 3, "y": -4, "color": "#ffd700", "label": "V(3,-4)"}
        ],
        "axisOfSymmetry": 3
    },
    # Slide 7: 3x^2 - 12 = 0 → x = ±2
    (39, 7): {
        "xMin": -4, "xMax": 4, "yMin": -15, "yMax": 10,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 3, "b": 0, "c": -12, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": 0, "color": "#ff6b6b", "label": "(2,0)"},
            {"x": -2, "y": 0, "color": "#ff6b6b", "label": "(-2,0)"},
            {"x": 0, "y": -12, "color": "#ffd700", "label": "V(0,-12)"}
        ],
        "axisOfSymmetry": 0
    },

    # ── L40: Completing the Square ───────────────────────────────────
    # Slide 3: x^2 + 6x = 7 → (x+3)^2 = 16 → x = 1 or -7
    (40, 3): {
        "xMin": -9, "xMax": 4, "yMin": -12, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": 6, "c": -7, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
            {"x": -7, "y": 0, "color": "#ff6b6b", "label": "(-7,0)"},
            {"x": -3, "y": -16, "color": "#ffd700", "label": "V(-3,-16)"}
        ],
        "axisOfSymmetry": -3
    },
    # Slide 4: x^2 - 8x - 5 = 0 → x = 4 ± √21 ≈ 8.58 or -0.58
    (40, 4): {
        "xMin": -2, "xMax": 10, "yMin": -25, "yMax": 10,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 1, "b": -8, "c": -5, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 8.58, "y": 0, "color": "#ff6b6b", "label": "(8.58,0)"},
            {"x": -0.58, "y": 0, "color": "#ff6b6b", "label": "(-0.58,0)"},
            {"x": 4, "y": -21, "color": "#ffd700", "label": "V(4,-21)"}
        ],
        "axisOfSymmetry": 4
    },
    # Slide 5: 2x^2 + 8x - 10 = 0 → x = 1 or -5
    (40, 5): {
        "xMin": -7, "xMax": 4, "yMin": -20, "yMax": 10,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 2, "b": 8, "c": -10, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
            {"x": -5, "y": 0, "color": "#ff6b6b", "label": "(-5,0)"},
            {"x": -2, "y": -18, "color": "#ffd700", "label": "V(-2,-18)"}
        ],
        "axisOfSymmetry": -2
    },
    # Slide 6: Converting general to vertex form: x^2 - 4x + 1 → (x-2)^2 - 3
    (40, 6): {
        "xMin": -1, "xMax": 5, "yMin": -5, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -4, "c": 1, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 2, "y": -3, "color": "#ffd700", "label": "V(2,-3)"},
            {"x": 0.27, "y": 0, "color": "#ff6b6b", "label": "(2-√3,0)"},
            {"x": 3.73, "y": 0, "color": "#ff6b6b", "label": "(2+√3,0)"}
        ],
        "axisOfSymmetry": 2
    },

    # ── L41 additions (non-graph slides) ────────────────────────────
    # Slide 1: Quadratic Formula intro — generic parabola
    (41, 1): {
        "xMin": -4, "xMax": 4, "yMin": -6, "yMax": 8,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -2, "c": -3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 1, "y": -4, "color": "#ffd700", "label": "Vertex"}
        ],
        "axisOfSymmetry": 1
    },
    # Slide 7: f(x) = 3x^2 - 5x + 7 (evaluation — show the parabola for context)
    (41, 7): {
        "xMin": -1, "xMax": 4, "yMin": -1, "yMax": 40,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 3, "b": -5, "c": 7, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 0.83, "y": 4.92, "color": "#ffd700", "label": "V(0.83,4.92)"},
            {"x": 4, "y": 35, "color": "#ff6b6b", "label": "f(4)=35"},
            {"x": 0, "y": 7, "color": "#00ff88", "label": "f(0)=7"}
        ],
        "axisOfSymmetry": 0.83
    },
    # Slide 8: Summary — show multiple parabolas
    (41, 8): {
        "xMin": -5, "xMax": 15, "yMin": -15, "yMax": 10,
        "xTicks": 2, "yTicks": 5,
        "curves": [
            {"a": 1, "b": -17, "c": 72, "color": "#00d4ff", "strokeWidth": 2, "label": "1A"},
            {"a": 1, "b": -5, "c": -7, "color": "#ff9500", "strokeWidth": 2, "label": "1B"},
        ],
        "points": [
            {"x": 8, "y": 0, "color": "#ff6b6b", "label": "x=8"},
            {"x": 9, "y": 0, "color": "#ff6b6b", "label": "x=9"}
        ]
    },

    # ── L42 additions ────────────────────────────────────────────────
    # Slide 1: Discriminant intro — show three cases
    (42, 1): {
        "xMin": -4, "xMax": 4, "yMin": -6, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": 1, "b": 0, "c": -4, "color": "#00d4ff", "strokeWidth": 2, "label": "Δ>0"},
            {"a": 1, "b": 0, "c": 0, "color": "#ffd700", "strokeWidth": 2, "label": "Δ=0"},
            {"a": 1, "b": 0, "c": 4, "color": "#ff6b6b", "strokeWidth": 2, "label": "Δ<0"}
        ]
    },
    # Slide 6: f(x) = 3x^2 - 5x + 7 evaluation
    (42, 6): {
        "xMin": -1, "xMax": 4, "yMin": 0, "yMax": 40,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 3, "b": -5, "c": 7, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 4, "y": 35, "color": "#ff6b6b", "label": "f(4)=35"},
            {"x": 0, "y": 7, "color": "#00ff88", "label": "f(0)=7"}
        ]
    },
    # Slide 7: f(x) = 3x^2 - 5x + 7 composition
    (42, 7): {
        "xMin": -1, "xMax": 4, "yMin": 0, "yMax": 40,
        "xTicks": 1, "yTicks": 5,
        "curves": [{"a": 3, "b": -5, "c": 7, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 2.47, "y": 13, "color": "#ff6b6b", "label": "f(x)=13"},
            {"x": -0.81, "y": 13, "color": "#ff6b6b", "label": "f(x)=13"}
        ]
    },
    # Slide 8: Summary three cases
    (42, 8): {
        "xMin": -4, "xMax": 6, "yMin": -6, "yMax": 12,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": 1, "b": -5, "c": 4, "color": "#00d4ff", "strokeWidth": 2, "label": "Δ>0 (2 roots)"},
            {"a": 1, "b": -6, "c": 9, "color": "#00ff88", "strokeWidth": 2, "label": "Δ=0 (1 root)"},
            {"a": 1, "b": 2, "c": 5, "color": "#ff6b6b", "strokeWidth": 2, "label": "Δ<0 (no roots)"}
        ],
        "points": [
            {"x": 1, "y": 0, "color": "#00d4ff", "label": "x=1"},
            {"x": 4, "y": 0, "color": "#00d4ff", "label": "x=4"},
            {"x": 3, "y": 0, "color": "#00ff88", "label": "x=3"}
        ]
    },

    # ── L43 additions ────────────────────────────────────────────────
    # Slide 1: Section 3.6 intro — show all four functions
    (43, 1): {
        "xMin": -7, "xMax": 12, "yMin": -15, "yMax": 15,
        "xTicks": 2, "yTicks": 5,
        "curves": [
            {"a": 1, "b": 6, "c": 0, "color": "#00d4ff", "strokeWidth": 2, "label": "g(x)"},
            {"a": 1, "b": -15, "c": 50, "color": "#ff9500", "strokeWidth": 2, "label": "f(x)"},
        ]
    },
    # Slide 7: Method summary — generic examples
    (43, 7): {
        "xMin": -4, "xMax": 6, "yMin": -10, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": 1, "b": 6, "c": 0, "color": "#00d4ff", "strokeWidth": 2, "label": "GCF"},
            {"a": 1, "b": -15, "c": 50, "color": "#ff9500", "strokeWidth": 2, "label": "Factor"},
        ]
    },
    # Slide 8: Recap table with all 4 parabolas
    (43, 8): {
        "xMin": -7, "xMax": 12, "yMin": -15, "yMax": 15,
        "xTicks": 2, "yTicks": 5,
        "curves": [
            {"a": 1, "b": 6, "c": 0, "color": "#00d4ff", "strokeWidth": 2},
            {"a": -2, "b": 5, "c": 6, "color": "#ff9500", "strokeWidth": 2},
            {"a": 1, "b": -15, "c": 50, "color": "#00ff88", "strokeWidth": 2},
        ],
        "points": [
            {"x": 0, "y": 0, "color": "#ff6b6b", "label": "(0,0)"},
            {"x": -6, "y": 0, "color": "#ff6b6b", "label": "(-6,0)"}
        ]
    },

    # ── L44 additions ────────────────────────────────────────────────
    # Slide 1: Graphing intro — 5-point method diagram
    (44, 1): {
        "xMin": -4, "xMax": 4, "yMin": -6, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -2, "c": -3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": -4, "color": "#ffd700", "label": "Vertex"},
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 0, "y": -3, "color": "#00ff88", "label": "y-int"},
            {"x": 2, "y": -3, "color": "#00ff88", "label": "symmetric"}
        ],
        "axisOfSymmetry": 1
    },
    # Slide 6: f(x) = x^2-6x+4 and g(x) = -2x+25
    (44, 6): {
        "xMin": -5, "xMax": 14, "yMin": -10, "yMax": 35,
        "xTicks": 2, "yTicks": 5,
        "curves": [
            {"a": 1, "b": -6, "c": 4, "color": "#00d4ff", "strokeWidth": 3, "label": "f(x)"},
            {"a": 0, "b": -2, "c": 25, "color": "#ff9500", "strokeWidth": 2, "dashed": True, "label": "g(x)"}
        ],
        "points": [
            {"x": 4, "y": -4, "color": "#ffd700", "label": "f(4)?"},
            {"x": 0, "y": 4, "color": "#00d4ff", "label": "(0,4)"}
        ]
    },
    # Slide 7: f(x+5) composition visualization
    (44, 7): {
        "xMin": -5, "xMax": 8, "yMin": -10, "yMax": 35,
        "xTicks": 1, "yTicks": 5,
        "curves": [
            {"a": 1, "b": -6, "c": 4, "color": "#00d4ff", "strokeWidth": 2, "label": "f(x)"},
            {"a": 1, "b": 4, "c": -1, "color": "#ff9500", "strokeWidth": 3, "label": "f(x+5)"}
        ],
        "points": [
            {"x": 3, "y": -5, "color": "#ffd700", "label": "V f(x)"},
            {"x": -2, "y": -5, "color": "#ff9500", "label": "V f(x+5)"}
        ]
    },
    # Slide 8: f(x) = g(x) intersection
    (44, 8): {
        "xMin": -5, "xMax": 14, "yMin": -10, "yMax": 35,
        "xTicks": 2, "yTicks": 5,
        "curves": [
            {"a": 1, "b": -6, "c": 4, "color": "#00d4ff", "strokeWidth": 3, "label": "f(x)"},
            {"a": 0, "b": -2, "c": 25, "color": "#ff9500", "strokeWidth": 2, "dashed": True, "label": "g(x)"}
        ],
        "points": [
            {"x": -3, "y": 31, "color": "#ff6b6b", "label": "(-3,31)"},
            {"x": 7, "y": 11, "color": "#ff6b6b", "label": "(7,11)"}
        ]
    },

    # ── L45 additions ────────────────────────────────────────────────
    # Slide 1: Comprehensive intro — show parabola and line together
    (45, 1): {
        "xMin": -4, "xMax": 8, "yMin": -10, "yMax": 15,
        "xTicks": 1, "yTicks": 5,
        "curves": [
            {"a": 1, "b": -4, "c": -5, "color": "#00d4ff", "strokeWidth": 3, "label": "parabola"},
            {"a": 0, "b": 2, "c": -1, "color": "#ff9500", "strokeWidth": 2, "dashed": True, "label": "line"}
        ],
        "points": [
            {"x": 2, "y": -9, "color": "#ffd700", "label": "Vertex"},
        ]
    },
    # Slide 2: Domain/Range — 4 parabolas side by side
    (45, 2): {
        "xMin": -7, "xMax": 5, "yMin": -12, "yMax": 12,
        "xTicks": 1, "yTicks": 4,
        "curves": [
            {"a": 1, "b": 6, "c": 5, "color": "#00d4ff", "strokeWidth": 2, "label": "g: min=-4"},
            {"a": -2, "b": 4, "c": 6, "color": "#ff9500", "strokeWidth": 2, "label": "h: max=8"},
        ],
        "points": [
            {"x": -3, "y": -4, "color": "#00d4ff", "label": "min"},
            {"x": 1, "y": 8, "color": "#ff9500", "label": "max"}
        ]
    },
    # Slide 5: Grand Review — master decision tree
    (45, 5): {
        "xMin": -4, "xMax": 8, "yMin": -12, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": 1, "b": -4, "c": -5, "color": "#00d4ff", "strokeWidth": 3},
        ],
        "points": [
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "(-1,0)"},
            {"x": 5, "y": 0, "color": "#ff6b6b", "label": "(5,0)"},
            {"x": 2, "y": -9, "color": "#ffd700", "label": "V(2,-9)"}
        ],
        "axisOfSymmetry": 2
    },
    # Slide 6: Formula card — visual reference
    (45, 6): {
        "xMin": -3, "xMax": 5, "yMin": -6, "yMax": 8,
        "xTicks": 1, "yTicks": 2,
        "curves": [{"a": 1, "b": -2, "c": -3, "color": "#00d4ff", "strokeWidth": 3}],
        "points": [
            {"x": 1, "y": -4, "color": "#ffd700", "label": "V=(-b/2a, f(-b/2a))"},
            {"x": -1, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 3, "y": 0, "color": "#ff6b6b", "label": "x-int"},
            {"x": 0, "y": -3, "color": "#00ff88", "label": "y-int=(0,c)"}
        ],
        "axisOfSymmetry": 1
    },
    # Slide 8: Graduation — show final parabola
    (45, 8): {
        "xMin": -4, "xMax": 4, "yMin": -5, "yMax": 10,
        "xTicks": 1, "yTicks": 2,
        "curves": [
            {"a": -1, "b": 0, "c": 9, "color": "#ff9500", "strokeWidth": 3},
            {"a": 1, "b": -2, "c": -3, "color": "#00d4ff", "strokeWidth": 2}
        ],
        "points": [
            {"x": 0, "y": 9, "color": "#ffd700", "label": "Go MSU!"}
        ]
    },
}

print(f"Total new coordinate entries to add: {len(COORDINATE_ADDITIONS)}")

# ─────────────────────────────────────────────────────────────
# Now patch montanaSlidesData.js
# ─────────────────────────────────────────────────────────────

with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size before: {len(content):,} bytes")

def to_js_value(obj, depth=0):
    pad = "  " * depth
    ipad = "  " * (depth + 1)
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        items = [f'{ipad}"{k}": {to_js_value(v, depth+1)}' for k, v in obj.items()]
        return "{\n" + ",\n".join(items) + "\n" + pad + "}"
    elif isinstance(obj, list):
        if not obj:
            return "[]"
        items = [ipad + to_js_value(item, depth+1) for item in obj]
        return "[\n" + ",\n".join(items) + "\n" + pad + "]"
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, str):
        escaped = obj.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '')
        return f'"{escaped}"'
    elif obj is None:
        return "null"
    else:
        return str(obj)

# For each lecture/slide pair, find the slide in the JS and add coordinate field
added = 0
skipped = 0

for (lid, slide_num), coord_data in COORDINATE_ADDITIONS.items():
    # Find the lecture variable section
    var_name = f"SLIDES_MONTANA_L{lid:02d}"
    section_start = content.find(f"export const {var_name}")
    if section_start == -1:
        print(f"  SKIP: {var_name} not found")
        skipped += 1
        continue
    
    # Find section end (next export const or end of file)
    next_export = content.find("export const", section_start + 10)
    section_end = next_export if next_export != -1 else len(content)
    
    section = content[section_start:section_end]
    
    # Check if this slide already has coordinate
    # Find the slide with num: slide_num
    slide_pattern = f'"num": {slide_num},'
    slide_pos = section.find(slide_pattern)
    if slide_pos == -1:
        print(f"  SKIP: L{lid} Slide {slide_num} not found in {var_name}")
        skipped += 1
        continue
    
    # Check if coordinate already exists near this slide
    # Find the next slide or end of this slide's object
    next_slide_pos = section.find('"num": ', slide_pos + 10)
    if next_slide_pos == -1:
        next_slide_pos = len(section)
    
    slide_region = section[slide_pos:next_slide_pos]
    
    if '"coordinate"' in slide_region:
        skipped += 1
        continue  # already has coordinate
    
    # Find the closing } of this slide object (before the next { for next slide)
    # The slide objects are indented, find the closing of the slide
    # Look for "script": "..." then the closing },
    # Strategy: find the last field's closing quote before the next slide
    
    # Find insertion point: before the closing } of the slide
    # The slide object ends with the last field, then },
    # We'll insert "coordinate": {...} before the closing }
    
    # Find the position in the full content
    abs_slide_pos = section_start + slide_pos
    abs_next_slide = section_start + next_slide_pos
    
    # Find the closing }, of the current slide object (last } before next slide start)
    # Work backwards from next_slide_pos in the full content
    search_region = content[abs_slide_pos:abs_next_slide]
    
    # Find the last occurrence of "}," or "}" that closes a slide
    # The slide's last field is typically "script" or "pitfall"
    # Find the very last field close: look for the pattern \n  }, or \n  }
    last_close = search_region.rfind('\n  },')
    if last_close == -1:
        last_close = search_region.rfind('\n  }')
        if last_close == -1:
            print(f"  WARN: Cannot find closing for L{lid} Slide {slide_num}")
            skipped += 1
            continue
        insert_before = abs_slide_pos + last_close
    else:
        insert_before = abs_slide_pos + last_close
    
    # Build coordinate JS
    coord_js = to_js_value(coord_data, 2)
    insertion = f',\n    "coordinate": {coord_js}'
    
    # Find the actual insert point - before the closing } of the slide
    # We need to find where the last field ends
    # Let's find the last field end in the slide region
    # Better approach: find "script": value end, then insert before the }
    
    # Find the last }" or ], that ends a field value before the slide closing }
    # Actually, let's just find the position to insert
    
    # Find insert position: right before the closing },\n of the slide
    # The pattern is: ...last_field_value"\n  }
    # Insert coordinate before \n  }
    
    content = content[:insert_before] + insertion + content[insert_before:]
    added += 1
    # print(f"  Added coordinate to L{lid} Slide {slide_num}")

print(f"\nAdded: {added} coordinate grids")
print(f"Skipped: {skipped} (already have coordinate or not found)")
print(f"File size after: {len(content):,} bytes")

with open(data_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Now run validate_katex.js and npm run build")
