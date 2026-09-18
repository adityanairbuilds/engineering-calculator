"""Geometry formulas: areas, perimeters, and volumes of common shapes."""

import math

from ...models.formula import Formula, Variable

GEOMETRY_FORMULAS: list[Formula] = []

GEOMETRY_FORMULAS.append(
    Formula(
        id="circle-area",
        name="Area of a Circle",
        category="Mathematics",
        subcategory="Geometry",
        equation="A = πr²",
        description="Calculates the area of a circle from its radius.",
        variables=[
            Variable("A", "Area", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
        ],
        keywords=["circle", "area", "radius"],
        solve={
            "A": lambda v: math.pi * v["r"] ** 2,
            "r": lambda v: math.sqrt(v["A"] / math.pi),
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="circle-circumference",
        name="Circumference of a Circle",
        category="Mathematics",
        subcategory="Geometry",
        equation="C = 2πr",
        description="Calculates the circumference of a circle from its radius.",
        variables=[
            Variable("C", "Circumference", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
        ],
        keywords=["circle", "circumference", "perimeter"],
        solve={
            "C": lambda v: 2 * math.pi * v["r"],
            "r": lambda v: v["C"] / (2 * math.pi),
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="triangle-area",
        name="Area of a Triangle",
        category="Mathematics",
        subcategory="Geometry",
        equation="A = ½bh",
        description="Calculates the area of a triangle from its base and height.",
        variables=[
            Variable("A", "Area", "dimensionless"),
            Variable("b", "Base", "dimensionless"),
            Variable("h", "Height", "dimensionless"),
        ],
        keywords=["triangle", "area", "base", "height"],
        solve={
            "A": lambda v: 0.5 * v["b"] * v["h"],
            "b": lambda v: (2 * v["A"]) / v["h"],
            "h": lambda v: (2 * v["A"]) / v["b"],
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="rectangle-area",
        name="Area of a Rectangle",
        category="Mathematics",
        subcategory="Geometry",
        equation="A = lw",
        description="Calculates the area of a rectangle from its length and width.",
        variables=[
            Variable("A", "Area", "dimensionless"),
            Variable("l", "Length", "dimensionless"),
            Variable("w", "Width", "dimensionless"),
        ],
        keywords=["rectangle", "area", "length", "width"],
        solve={
            "A": lambda v: v["l"] * v["w"],
            "l": lambda v: v["A"] / v["w"],
            "w": lambda v: v["A"] / v["l"],
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="sphere-volume",
        name="Volume of a Sphere",
        category="Mathematics",
        subcategory="Geometry",
        equation="V = (4/3)πr³",
        description="Calculates the volume of a sphere from its radius.",
        variables=[
            Variable("V", "Volume", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
        ],
        keywords=["sphere", "volume", "radius"],
        solve={
            "V": lambda v: (4 / 3) * math.pi * v["r"] ** 3,
            "r": lambda v: math.cbrt((3 * v["V"]) / (4 * math.pi)),
        },
    )
)


def _pythagorean_a(v: dict[str, float]) -> float:
    if v["c"] <= v["b"]:
        raise ValueError("The hypotenuse must be longer than leg b.")
    return math.sqrt(v["c"] ** 2 - v["b"] ** 2)


def _pythagorean_b(v: dict[str, float]) -> float:
    if v["c"] <= v["a"]:
        raise ValueError("The hypotenuse must be longer than leg a.")
    return math.sqrt(v["c"] ** 2 - v["a"] ** 2)


GEOMETRY_FORMULAS.append(
    Formula(
        id="pythagorean-theorem",
        name="Pythagorean Theorem",
        category="Mathematics",
        subcategory="Geometry",
        equation="c = √(a² + b²)",
        description="Finds the hypotenuse of a right triangle from its two legs.",
        variables=[
            Variable("c", "Hypotenuse", "dimensionless"),
            Variable("a", "Leg a", "dimensionless"),
            Variable("b", "Leg b", "dimensionless"),
        ],
        keywords=["pythagorean theorem", "right triangle", "hypotenuse"],
        solve={
            "c": lambda v: math.sqrt(v["a"] ** 2 + v["b"] ** 2),
            "a": _pythagorean_a,
            "b": _pythagorean_b,
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="sphere-surface-area",
        name="Surface Area of a Sphere",
        category="Mathematics",
        subcategory="Geometry",
        equation="A = 4πr²",
        description="Calculates the surface area of a sphere from its radius.",
        variables=[
            Variable("A", "Surface area", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
        ],
        keywords=["sphere", "surface area", "radius"],
        solve={
            "A": lambda v: 4 * math.pi * v["r"] ** 2,
            "r": lambda v: math.sqrt(v["A"] / (4 * math.pi)),
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="cylinder-volume",
        name="Volume of a Cylinder",
        category="Mathematics",
        subcategory="Geometry",
        equation="V = πr²h",
        description="Calculates the volume of a cylinder from its radius and height.",
        variables=[
            Variable("V", "Volume", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
            Variable("h", "Height", "dimensionless"),
        ],
        keywords=["cylinder", "volume", "radius", "height"],
        solve={
            "V": lambda v: math.pi * v["r"] ** 2 * v["h"],
            "r": lambda v: math.sqrt(v["V"] / (math.pi * v["h"])),
            "h": lambda v: v["V"] / (math.pi * v["r"] ** 2),
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="cone-volume",
        name="Volume of a Cone",
        category="Mathematics",
        subcategory="Geometry",
        equation="V = (1/3)πr²h",
        description="Calculates the volume of a cone from its radius and height.",
        variables=[
            Variable("V", "Volume", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
            Variable("h", "Height", "dimensionless"),
        ],
        keywords=["cone", "volume", "radius", "height"],
        solve={
            "V": lambda v: (1 / 3) * math.pi * v["r"] ** 2 * v["h"],
            "r": lambda v: math.sqrt((3 * v["V"]) / (math.pi * v["h"])),
            "h": lambda v: (3 * v["V"]) / (math.pi * v["r"] ** 2),
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="rectangle-perimeter",
        name="Perimeter of a Rectangle",
        category="Mathematics",
        subcategory="Geometry",
        equation="P = 2(l + w)",
        description="Calculates the perimeter of a rectangle from its length and width.",
        variables=[
            Variable("P", "Perimeter", "dimensionless"),
            Variable("l", "Length", "dimensionless"),
            Variable("w", "Width", "dimensionless"),
        ],
        keywords=["rectangle", "perimeter", "length", "width"],
        solve={
            "P": lambda v: 2 * (v["l"] + v["w"]),
            "l": lambda v: v["P"] / 2 - v["w"],
            "w": lambda v: v["P"] / 2 - v["l"],
        },
    )
)

GEOMETRY_FORMULAS.append(
    Formula(
        id="trapezoid-area",
        name="Area of a Trapezoid",
        category="Mathematics",
        subcategory="Geometry",
        equation="A = ½(b₁ + b₂)h",
        description="Calculates the area of a trapezoid from its two parallel bases and height.",
        variables=[
            Variable("A", "Area", "dimensionless"),
            Variable("b1", "Base 1", "dimensionless"),
            Variable("b2", "Base 2", "dimensionless"),
            Variable("h", "Height", "dimensionless"),
        ],
        keywords=["trapezoid", "area", "bases", "height"],
        solve={
            "A": lambda v: 0.5 * (v["b1"] + v["b2"]) * v["h"],
            "h": lambda v: (2 * v["A"]) / (v["b1"] + v["b2"]),
            "b1": lambda v: (2 * v["A"]) / v["h"] - v["b2"],
            "b2": lambda v: (2 * v["A"]) / v["h"] - v["b1"],
        },
    )
)


def _regular_polygon_area(v: dict[str, float]) -> float:
    if v["n"] < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    return 0.25 * v["n"] * v["s"] ** 2 * (1 / math.tan(math.pi / v["n"]))


def _regular_polygon_s(v: dict[str, float]) -> float:
    if v["n"] < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    return math.sqrt((4 * v["A"]) / (v["n"] * (1 / math.tan(math.pi / v["n"]))))


GEOMETRY_FORMULAS.append(
    Formula(
        id="regular-polygon-area",
        name="Area of a Regular Polygon",
        category="Mathematics",
        subcategory="Geometry",
        equation="A = ¼ n s² cot(π/n)",
        description="Calculates the area of a regular polygon from its number of sides and side length.",
        variables=[
            Variable("A", "Area", "dimensionless"),
            Variable("n", "Number of sides", "dimensionless"),
            Variable("s", "Side length", "dimensionless"),
        ],
        keywords=["regular polygon", "polygon area", "n-gon", "hexagon", "pentagon"],
        solve={
            "A": _regular_polygon_area,
            "s": _regular_polygon_s,
        },
    )
)


def _cylinder_surface_area_r(v: dict[str, float]) -> float:
    a = 2 * math.pi
    b = 2 * math.pi * v["h"]
    c = -v["SA"]
    disc = b**2 - 4 * a * c
    if disc < 0:
        raise ValueError("No real solution for these inputs.")
    return (-b + math.sqrt(disc)) / (2 * a)


GEOMETRY_FORMULAS.append(
    Formula(
        id="cylinder-surface-area",
        name="Surface Area of a Cylinder",
        category="Mathematics",
        subcategory="Geometry",
        equation="SA = 2πr² + 2πrh",
        description="Calculates the total surface area of a cylinder (including both circular ends).",
        variables=[
            Variable("SA", "Surface area", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
            Variable("h", "Height", "dimensionless"),
        ],
        keywords=["cylinder", "surface area", "radius", "height"],
        solve={
            "SA": lambda v: 2 * math.pi * v["r"] ** 2 + 2 * math.pi * v["r"] * v["h"],
            "h": lambda v: v["SA"] / (2 * math.pi * v["r"]) - v["r"],
            "r": _cylinder_surface_area_r,
        },
    )
)


def _cone_surface_area_r(v: dict[str, float]) -> float:
    a = math.pi
    b = math.pi * v["l"]
    c = -v["SA"]
    disc = b**2 - 4 * a * c
    if disc < 0:
        raise ValueError("No real solution for these inputs.")
    return (-b + math.sqrt(disc)) / (2 * a)


GEOMETRY_FORMULAS.append(
    Formula(
        id="cone-surface-area",
        name="Surface Area of a Cone",
        category="Mathematics",
        subcategory="Geometry",
        equation="SA = πr² + πrl",
        description="Calculates the total surface area of a cone from its radius and slant height l.",
        variables=[
            Variable("SA", "Surface area", "dimensionless"),
            Variable("r", "Radius", "dimensionless"),
            Variable("l", "Slant height", "dimensionless"),
        ],
        keywords=["cone", "surface area", "radius", "slant height"],
        solve={
            "SA": lambda v: math.pi * v["r"] ** 2 + math.pi * v["r"] * v["l"],
            "l": lambda v: (v["SA"] - math.pi * v["r"] ** 2) / (math.pi * v["r"]),
            "r": _cone_surface_area_r,
        },
    )
)
