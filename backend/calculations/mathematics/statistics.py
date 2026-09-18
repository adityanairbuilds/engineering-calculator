"""Statistics formulas: probability, distributions, and descriptive statistics."""

import math

from ...models.formula import Formula, Variable

STATISTICS_FORMULAS: list[Formula] = []


def _factorial(num: float) -> int:
    if num < 0 or not float(num).is_integer():
        raise ValueError("Factorial is only defined for non-negative whole numbers.")
    if num > 170:
        # 170! is the largest factorial that still fits in a float; beyond
        # that the loop below would also just run forever for no useful result.
        raise ValueError("n is too large — factorial is only supported up to 170.")
    result = 1
    for i in range(2, int(num) + 1):
        result *= i
    return result


STATISTICS_FORMULAS.append(
    Formula(
        id="probability",
        name="Probability (Classical)",
        category="Mathematics",
        subcategory="Statistics",
        equation="P(A) = favorable / total",
        description="Calculates the probability of an event from its favorable and total outcomes.",
        variables=[
            Variable("PA", "Probability of event A", "dimensionless"),
            Variable("favorable", "Favorable outcomes", "dimensionless"),
            Variable("total", "Total possible outcomes", "dimensionless"),
        ],
        keywords=["probability", "odds", "likelihood", "chance"],
        solve={
            "PA": lambda v: v["favorable"] / v["total"],
            "favorable": lambda v: v["PA"] * v["total"],
            "total": lambda v: v["favorable"] / v["PA"],
        },
    )
)

STATISTICS_FORMULAS.append(
    Formula(
        id="z-score",
        name="Z-Score",
        category="Mathematics",
        subcategory="Statistics",
        equation="z = (x − μ) / σ",
        description="Standardizes a value relative to the mean and standard deviation of its distribution.",
        variables=[
            Variable("z", "Z-score", "dimensionless"),
            Variable("x", "Data value", "dimensionless"),
            Variable("mu", "Mean", "dimensionless"),
            Variable("sigma", "Standard deviation", "dimensionless"),
        ],
        keywords=["z-score", "standard score", "normal distribution", "standardize"],
        solve={
            "z": lambda v: (v["x"] - v["mu"]) / v["sigma"],
            "x": lambda v: v["mu"] + v["z"] * v["sigma"],
            "mu": lambda v: v["x"] - v["z"] * v["sigma"],
            "sigma": lambda v: (v["x"] - v["mu"]) / v["z"],
        },
    )
)


def _permutations(v: dict[str, float]) -> float:
    if v["r"] > v["n"]:
        raise ValueError("r cannot be greater than n.")
    return _factorial(v["n"]) / _factorial(v["n"] - v["r"])


STATISTICS_FORMULAS.append(
    Formula(
        id="permutations",
        name="Permutations",
        category="Mathematics",
        subcategory="Statistics",
        equation="P(n,r) = n! / (n − r)!",
        description="Counts the number of ordered arrangements of r items chosen from n items.",
        variables=[
            Variable("Pnr", "Number of permutations", "dimensionless"),
            Variable("n", "Total items", "dimensionless"),
            Variable("r", "Items arranged", "dimensionless"),
        ],
        keywords=["permutations", "arrangements", "combinatorics", "counting"],
        solve={
            "Pnr": _permutations,
        },
    )
)


def _combinations(v: dict[str, float]) -> float:
    if v["r"] > v["n"]:
        raise ValueError("r cannot be greater than n.")
    return _factorial(v["n"]) / (_factorial(v["r"]) * _factorial(v["n"] - v["r"]))


STATISTICS_FORMULAS.append(
    Formula(
        id="combinations",
        name="Combinations",
        category="Mathematics",
        subcategory="Statistics",
        equation="C(n,r) = n! / (r!(n − r)!)",
        description="Counts the number of ways to choose r items from n items, order not mattering.",
        variables=[
            Variable("Cnr", "Number of combinations", "dimensionless"),
            Variable("n", "Total items", "dimensionless"),
            Variable("r", "Items chosen", "dimensionless"),
        ],
        keywords=["combinations", "choose", "binomial coefficient", "combinatorics"],
        solve={
            "Cnr": _combinations,
        },
    )
)

STATISTICS_FORMULAS.append(
    Formula(
        id="mean",
        name="Mean (from Sum)",
        category="Mathematics",
        subcategory="Statistics",
        equation="μ = Σx / n",
        description="Calculates the arithmetic mean from the sum of all data values and the count. Add up your data by hand first.",
        variables=[
            Variable("mu", "Mean", "dimensionless"),
            Variable("sumX", "Sum of all values (Σx)", "dimensionless"),
            Variable("n", "Number of values", "dimensionless"),
        ],
        keywords=["mean", "average", "central tendency", "arithmetic mean"],
        solve={
            "mu": lambda v: v["sumX"] / v["n"],
            "sumX": lambda v: v["mu"] * v["n"],
            "n": lambda v: v["sumX"] / v["mu"],
        },
    )
)


def _standard_deviation_sigma(v: dict[str, float]) -> float:
    if v["sumSqDev"] < 0:
        raise ValueError("Sum of squared deviations cannot be negative.")
    return math.sqrt(v["sumSqDev"] / v["n"])


STATISTICS_FORMULAS.append(
    Formula(
        id="standard-deviation",
        name="Standard Deviation (Population)",
        category="Mathematics",
        subcategory="Statistics",
        equation="σ = √(Σ(x − μ)² / n)",
        description="Calculates population standard deviation from the sum of squared deviations from the mean. Compute Σ(x − μ)² by hand first.",
        variables=[
            Variable("sigma", "Standard deviation", "dimensionless"),
            Variable("sumSqDev", "Sum of squared deviations, Σ(x−μ)²", "dimensionless"),
            Variable("n", "Number of values", "dimensionless"),
        ],
        keywords=["standard deviation", "spread", "population standard deviation", "dispersion"],
        solve={
            "sigma": _standard_deviation_sigma,
            "sumSqDev": lambda v: v["sigma"] ** 2 * v["n"],
            "n": lambda v: v["sumSqDev"] / v["sigma"] ** 2,
        },
    )
)

STATISTICS_FORMULAS.append(
    Formula(
        id="population-variance",
        name="Variance (Population)",
        category="Mathematics",
        subcategory="Statistics",
        equation="σ² = Σ(x − μ)² / n",
        description="Calculates population variance from the sum of squared deviations from the mean. Compute Σ(x − μ)² by hand first.",
        variables=[
            Variable("sigma2", "Variance", "dimensionless"),
            Variable("sumSqDev", "Sum of squared deviations, Σ(x−μ)²", "dimensionless"),
            Variable("n", "Number of values", "dimensionless"),
        ],
        keywords=["variance", "population variance", "spread", "dispersion"],
        solve={
            "sigma2": lambda v: v["sumSqDev"] / v["n"],
            "sumSqDev": lambda v: v["sigma2"] * v["n"],
            "n": lambda v: v["sumSqDev"] / v["sigma2"],
        },
    )
)

STATISTICS_FORMULAS.append(
    Formula(
        id="weighted-mean",
        name="Weighted Mean",
        category="Mathematics",
        subcategory="Statistics",
        equation="x̄ = Σ(w·x) / Σw",
        description="Calculates a weighted average from the sum of weight×value products and the sum of weights. Compute both sums by hand first.",
        variables=[
            Variable("xbar", "Weighted mean", "dimensionless"),
            Variable("sumWX", "Sum of weight×value products, Σ(wx)", "dimensionless"),
            Variable("sumW", "Sum of weights, Σw", "dimensionless"),
        ],
        keywords=["weighted mean", "weighted average"],
        solve={
            "xbar": lambda v: v["sumWX"] / v["sumW"],
            "sumWX": lambda v: v["xbar"] * v["sumW"],
            "sumW": lambda v: v["sumWX"] / v["xbar"],
        },
    )
)

STATISTICS_FORMULAS.append(
    Formula(
        id="expected-value-discrete",
        name="Expected Value (Discrete, Two Outcomes)",
        category="Mathematics",
        subcategory="Statistics",
        equation="E(X) = x₁P(x₁) + x₂P(x₂)",
        description="Calculates the expected value of a discrete random variable with two possible outcomes; extend the same pattern by hand for more outcomes.",
        variables=[
            Variable("Ex", "Expected value", "dimensionless"),
            Variable("x1", "Outcome 1 value", "dimensionless"),
            Variable("p1", "Probability of outcome 1", "dimensionless"),
            Variable("x2", "Outcome 2 value", "dimensionless"),
            Variable("p2", "Probability of outcome 2", "dimensionless"),
        ],
        keywords=["expected value", "discrete random variable", "probability distribution"],
        solve={
            "Ex": lambda v: v["x1"] * v["p1"] + v["x2"] * v["p2"],
            "x1": lambda v: (v["Ex"] - v["x2"] * v["p2"]) / v["p1"],
            "x2": lambda v: (v["Ex"] - v["x1"] * v["p1"]) / v["p2"],
        },
    )
)


def _binomial_probability(v: dict[str, float]) -> float:
    if v["k"] > v["n"]:
        raise ValueError("k cannot exceed n.")
    if v["p"] < 0 or v["p"] > 1:
        raise ValueError("p must be between 0 and 1.")
    combos = _factorial(v["n"]) / (_factorial(v["k"]) * _factorial(v["n"] - v["k"]))
    return combos * v["p"] ** v["k"] * (1 - v["p"]) ** (v["n"] - v["k"])


STATISTICS_FORMULAS.append(
    Formula(
        id="binomial-probability",
        name="Binomial Probability",
        category="Mathematics",
        subcategory="Statistics",
        equation="P(X=k) = C(n,k) pᵏ(1 − p)ⁿ⁻ᵏ",
        description="Calculates the probability of exactly k successes in n independent trials with success probability p.",
        variables=[
            Variable("P", "Probability of exactly k successes", "dimensionless"),
            Variable("n", "Number of trials", "dimensionless"),
            Variable("k", "Number of successes", "dimensionless"),
            Variable("p", "Probability of success per trial", "dimensionless"),
        ],
        keywords=["binomial probability", "binomial distribution", "bernoulli trials"],
        solve={
            "P": _binomial_probability,
        },
    )
)
