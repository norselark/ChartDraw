"Optimize angular positions to minimize overlap"

from .utils import dist, is_sorted
from itertools import combinations

OPTIMIZE_STEPS = 30
LEARN_RATE = 0.1
DIST_WEIGHT = 0.4
OVERLAP_WEIGHT = 1 - DIST_WEIGHT
OVERLAP_DIST = 5

def get_overlap_loss(angles):
    return sum(max(0, OVERLAP_DIST - dist(a, b))
               for a, b in combinations(angles, 2))


def get_deviation_loss(angles, targets):
    return (DIST_WEIGHT
            * sum((target - angle) ** 2
                  for target, angle in zip(targets, angles))
            / (2 * len(angles)))


def get_total_loss(angles, targets):
    return get_overlap_loss(angles) + get_deviation_loss(angles, targets)


def optimize(angles):
    new_angles = [ang for ang in angles]
    for step in range(OPTIMIZE_STEPS):
        deltas = list(map(lambda x: 0, angles)) # Initialize to zero
        for i, j in combinations(range(len(angles)), 2):
            ang_i = new_angles[i]
            ang_j = new_angles[j]
            if dist(ang_i, ang_j) < OVERLAP_DIST:
                if is_sorted(ang_i, ang_j):
                    deltas[i] -= OVERLAP_WEIGHT
                    deltas[j] += OVERLAP_WEIGHT
                else:
                    deltas[i] += OVERLAP_WEIGHT
                    deltas[j] -= OVERLAP_WEIGHT
        for i in range(len(angles)):
            # TODO: Something bad will happen if they are close across 0
            deltas[i] -= DIST_WEIGHT * (angles[i] - new_angles[i])
        new_angles = [(ang + LEARN_RATE * delta) % 360
                      for ang, delta in zip(new_angles, deltas)]
    return new_angles
