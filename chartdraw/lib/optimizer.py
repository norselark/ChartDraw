"Optimize angular positions to minimize overlap"

from itertools import combinations
from typing import List, Sequence

from .utils import dist, is_sorted

OPTIMIZE_STEPS = 30
LEARN_RATE = 0.1
DIST_WEIGHT = 0.3
OVERLAP_WEIGHT = 1 - DIST_WEIGHT
OVERLAP_DIST = 6


def overlap_loss(angles: Sequence[float]) -> float:
    return sum(max(0, OVERLAP_DIST - dist(a, b))
               for a, b in combinations(angles, 2))


def deviation_loss(angles: Sequence[float], targets: Sequence[float]) -> float:
    assert len(angles) == len(targets)
    return (DIST_WEIGHT
            * sum((target - angle) ** 2
                  for target, angle in zip(targets, angles))
            / (2 * len(angles)))


def deviation_gradient(angle: float, target: float) -> float:
    "Gradient for a single angle"
    if is_sorted(angle, target):
        return -dist(angle, target)
    else:
        return dist(angle, target)


def total_loss(angles: Sequence[float], targets: Sequence[float]) -> float:
    assert len(angles) == len(targets)
    return overlap_loss(angles) + deviation_loss(angles, targets)


def optimize(angles: Sequence[float]) -> List[float]:
    candidate = [ang for ang in angles]
    for _ in range(OPTIMIZE_STEPS):
        deltas = [0. for __ in angles]  # Initialize to zero
        # Compute overlap gradient
        for i, j in combinations(range(len(angles)), 2):
            ang_i = candidate[i]
            ang_j = candidate[j]
            if dist(ang_i, ang_j) < OVERLAP_DIST:
                if is_sorted(ang_i, ang_j):
                    deltas[i] -= OVERLAP_WEIGHT
                    deltas[j] += OVERLAP_WEIGHT
                else:
                    deltas[i] += OVERLAP_WEIGHT
                    deltas[j] -= OVERLAP_WEIGHT
        # Compute deviation gradient
        dev_gradient = [DIST_WEIGHT * deviation_gradient(ang, tgt)
                        for ang, tgt in zip(candidate, angles)]
        for i, g in enumerate(dev_gradient):
            deltas[i] += g
        # Perform update
        candidate = [(ang + LEARN_RATE * delta) % 360
                     for ang, delta in zip(candidate, deltas)]
    return candidate
