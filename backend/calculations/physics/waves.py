"""Wave formulas: wave speed, sound, Doppler effect, interference, oscillation, optics."""

import math

from ...models.formula import Formula, Variable

WAVES_FORMULAS: list[Formula] = []

WAVES_FORMULAS.append(
    Formula(
        id="wave-speed",
        name="Wave Speed",
        category="Physics",
        subcategory="Waves",
        equation="v = fλ",
        description="Calculates wave speed from frequency and wavelength.",
        variables=[
            Variable("v", "Wave speed", "m/s"),
            Variable("f", "Frequency", "Hz"),
            Variable("lambda", "Wavelength", "m"),
        ],
        keywords=["wave speed", "frequency", "wavelength", "wave", "sound", "light"],
        solve={
            "v": lambda v: v["f"] * v["lambda"],
            "f": lambda v: v["v"] / v["lambda"],
            "lambda": lambda v: v["v"] / v["f"],
        },
    )
)

WAVES_FORMULAS.append(
    Formula(
        id="sound-intensity",
        name="Sound Intensity",
        category="Physics",
        subcategory="Waves",
        equation="I = P / A",
        description="Calculates sound (or wave) intensity from power and the area it is spread over.",
        variables=[
            Variable("I", "Intensity", "W/m²"),
            Variable("P", "Power", "W"),
            Variable("A", "Area", "m²"),
        ],
        keywords=["sound", "intensity", "power", "area", "wave"],
        solve={
            "I": lambda v: v["P"] / v["A"],
            "P": lambda v: v["I"] * v["A"],
            "A": lambda v: v["P"] / v["I"],
        },
    )
)


def _decibel_db(v: dict[str, float]) -> float:
    if v["I"] <= 0 or v["I0"] <= 0:
        raise ValueError("Intensities must be positive.")
    return 10 * math.log10(v["I"] / v["I0"])


WAVES_FORMULAS.append(
    Formula(
        id="decibel",
        name="Decibel Scale",
        category="Physics",
        subcategory="Waves",
        equation="dB = 10 log₁₀(I / I₀)",
        description="Calculates sound level in decibels from intensity relative to a reference intensity.",
        variables=[
            Variable("dB", "Sound level", "dB"),
            Variable("I", "Sound intensity", "W/m²"),
            Variable("I0", "Reference intensity (typically 10⁻¹²)", "W/m²"),
        ],
        keywords=["decibel", "sound level", "logarithm", "intensity", "wave", "loudness"],
        solve={
            "dB": _decibel_db,
            "I": lambda v: v["I0"] * 10 ** (v["dB"] / 10),
            "I0": lambda v: v["I"] / 10 ** (v["dB"] / 10),
        },
    )
)

WAVES_FORMULAS.append(
    Formula(
        id="doppler-effect",
        name="Doppler Effect",
        category="Physics",
        subcategory="Waves",
        equation="f_obs = f(v + v_o) / (v - v_s)",
        description="Calculates the observed frequency when a source and/or observer are moving relative to each other. Use a positive v_o (observer velocity) if the observer moves toward the source, negative if away; positive v_s (source velocity) if the source moves toward the observer, negative if away.",
        variables=[
            Variable("fObserved", "Observed frequency", "Hz"),
            Variable("f", "Source frequency", "Hz"),
            Variable("v", "Wave speed in medium", "m/s"),
            Variable("vObserver", "Observer velocity (+ toward source)", "m/s"),
            Variable("vSource", "Source velocity (+ toward observer)", "m/s"),
        ],
        keywords=["doppler", "doppler effect", "frequency", "motion", "wave", "sound", "observed frequency"],
        solve={
            "fObserved": lambda v: (v["f"] * (v["v"] + v["vObserver"])) / (v["v"] - v["vSource"]),
            "f": lambda v: (v["fObserved"] * (v["v"] - v["vSource"])) / (v["v"] + v["vObserver"]),
            "v": lambda v: (v["fObserved"] * v["vSource"] + v["f"] * v["vObserver"]) / (v["fObserved"] - v["f"]),
            "vObserver": lambda v: (v["fObserved"] * (v["v"] - v["vSource"]) - v["f"] * v["v"]) / v["f"],
            "vSource": lambda v: v["v"] - (v["f"] * (v["v"] + v["vObserver"])) / v["fObserved"],
        },
    )
)


def _interference_double_slit_theta(v: dict[str, float]) -> float:
    ratio = (v["n"] * v["lambda"]) / v["d"]
    if ratio < -1 or ratio > 1:
        raise ValueError("nλ/d must be between -1 and 1.")
    return math.asin(ratio) * (180 / math.pi)


WAVES_FORMULAS.append(
    Formula(
        id="interference-double-slit",
        name="Double Slit Interference",
        category="Physics",
        subcategory="Waves",
        equation="d sin(θ) = nλ",
        description="Calculates the condition for constructive interference (bright fringes) in a double slit experiment.",
        variables=[
            Variable("d", "Slit separation", "m"),
            Variable("theta", "Angle to the bright fringe", "°"),
            Variable("n", "Fringe order (integer)", "dimensionless"),
            Variable("lambda", "Wavelength", "m"),
        ],
        keywords=["interference", "double slit", "diffraction", "wavelength", "light", "fringe"],
        solve={
            "d": lambda v: (v["n"] * v["lambda"]) / math.sin((v["theta"] * math.pi) / 180),
            "theta": _interference_double_slit_theta,
            "n": lambda v: (v["d"] * math.sin((v["theta"] * math.pi) / 180)) / v["lambda"],
            "lambda": lambda v: (v["d"] * math.sin((v["theta"] * math.pi) / 180)) / v["n"],
        },
    )
)


def _harmonic_motion_omega(v: dict[str, float]) -> float:
    ratio = v["x"] / v["A"]
    if ratio < -1 or ratio > 1:
        raise ValueError("x/A must be between -1 and 1.")
    return (math.acos(ratio) - (v["phi"] * math.pi) / 180) / v["t"]


def _harmonic_motion_t(v: dict[str, float]) -> float:
    ratio = v["x"] / v["A"]
    if ratio < -1 or ratio > 1:
        raise ValueError("x/A must be between -1 and 1.")
    return (math.acos(ratio) - (v["phi"] * math.pi) / 180) / v["omega"]


def _harmonic_motion_phi(v: dict[str, float]) -> float:
    ratio = v["x"] / v["A"]
    if ratio < -1 or ratio > 1:
        raise ValueError("x/A must be between -1 and 1.")
    return (math.acos(ratio) - v["omega"] * v["t"]) * (180 / math.pi)


WAVES_FORMULAS.append(
    Formula(
        id="harmonic-motion",
        name="Simple Harmonic Motion",
        category="Physics",
        subcategory="Waves",
        equation="x = A cos(ωt + φ)",
        description="Describes the displacement of an object undergoing simple harmonic motion over time. Inverse solves return the principal-value solution.",
        variables=[
            Variable("x", "Displacement", "m"),
            Variable("A", "Amplitude", "m"),
            Variable("omega", "Angular frequency", "rad/s"),
            Variable("t", "Time", "s"),
            Variable("phi", "Phase constant", "°"),
        ],
        keywords=["harmonic motion", "oscillation", "amplitude", "frequency", "wave", "shm", "phase"],
        solve={
            "x": lambda v: v["A"] * math.cos(v["omega"] * v["t"] + (v["phi"] * math.pi) / 180),
            "A": lambda v: v["x"] / math.cos(v["omega"] * v["t"] + (v["phi"] * math.pi) / 180),
            "omega": _harmonic_motion_omega,
            "t": _harmonic_motion_t,
            "phi": _harmonic_motion_phi,
        },
    )
)


def _pendulum_period_t(v: dict[str, float]) -> float:
    if v["L"] / v["g"] < 0:
        raise ValueError("L/g is negative — no real period.")
    return 2 * math.pi * math.sqrt(v["L"] / v["g"])


WAVES_FORMULAS.append(
    Formula(
        id="pendulum-period",
        name="Simple Pendulum Period",
        category="Physics",
        subcategory="Waves",
        equation="T = 2π√(L / g)",
        description="Calculates the period of a simple pendulum for small oscillation angles.",
        variables=[
            Variable("T", "Period", "s"),
            Variable("L", "Pendulum length", "m"),
            Variable("g", "Gravitational acceleration", "m/s²"),
        ],
        keywords=["pendulum", "period", "oscillation", "simple harmonic motion", "gravity"],
        solve={
            "T": _pendulum_period_t,
            "L": lambda v: v["g"] * (v["T"] / (2 * math.pi)) ** 2,
            "g": lambda v: v["L"] / (v["T"] / (2 * math.pi)) ** 2,
        },
    )
)


def _mass_spring_period_t(v: dict[str, float]) -> float:
    if v["m"] / v["k"] < 0:
        raise ValueError("m/k is negative — no real period.")
    return 2 * math.pi * math.sqrt(v["m"] / v["k"])


WAVES_FORMULAS.append(
    Formula(
        id="mass-spring-period",
        name="Mass-Spring Period",
        category="Physics",
        subcategory="Waves",
        equation="T = 2π√(m / k)",
        description="Calculates the period of oscillation of a mass on an ideal spring.",
        variables=[
            Variable("T", "Period", "s"),
            Variable("m", "Mass", "kg"),
            Variable("k", "Spring constant", "N/m"),
        ],
        keywords=["spring", "period", "oscillation", "simple harmonic motion", "mass-spring system"],
        solve={
            "T": _mass_spring_period_t,
            "m": lambda v: v["k"] * (v["T"] / (2 * math.pi)) ** 2,
            "k": lambda v: v["m"] / (v["T"] / (2 * math.pi)) ** 2,
        },
    )
)


def _snells_law_theta2(v: dict[str, float]) -> float:
    ratio = (v["n1"] * math.sin((v["theta1"] * math.pi) / 180)) / v["n2"]
    if ratio < -1 or ratio > 1:
        raise ValueError("Total internal reflection — no real refraction angle.")
    return math.asin(ratio) * (180 / math.pi)


def _snells_law_theta1(v: dict[str, float]) -> float:
    ratio = (v["n2"] * math.sin((v["theta2"] * math.pi) / 180)) / v["n1"]
    if ratio < -1 or ratio > 1:
        raise ValueError("No real angle of incidence for these values.")
    return math.asin(ratio) * (180 / math.pi)


WAVES_FORMULAS.append(
    Formula(
        id="snells-law",
        name="Snell's Law",
        category="Physics",
        subcategory="Optics",
        equation="n₁ sin(θ₁) = n₂ sin(θ₂)",
        description="Relates the angles of incidence and refraction as light passes between two media of different refractive index.",
        variables=[
            Variable("n1", "Refractive index of medium 1", "dimensionless"),
            Variable("theta1", "Angle of incidence", "°"),
            Variable("n2", "Refractive index of medium 2", "dimensionless"),
            Variable("theta2", "Angle of refraction", "°"),
        ],
        keywords=["snell", "snell's law", "refraction", "optics", "light", "refractive index"],
        solve={
            "theta2": _snells_law_theta2,
            "theta1": _snells_law_theta1,
            "n1": lambda v: (v["n2"] * math.sin((v["theta2"] * math.pi) / 180)) / math.sin((v["theta1"] * math.pi) / 180),
            "n2": lambda v: (v["n1"] * math.sin((v["theta1"] * math.pi) / 180)) / math.sin((v["theta2"] * math.pi) / 180),
        },
    )
)
