# This code performs collision testing of convex 2D polyedra by means
# of the Hyperplane separation theorem, also known as Separating axis theorem (SAT).
#
# For more information visit:
# https://en.wikipedia.org/wiki/Hyperplane_separation_theorem

import numpy


def edgeVector(p0, p1):
    return [p1[0] - p0[0], p1[1] - p0[1]]


def vertices2Edges(vertices):
    return [edgeVector(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]


def project(vertices, axis):
    dots = [numpy.dot(vertex, axis) for vertex in vertices]
    return [min(dots), max(dots)]


def contains(n, range):
    a = range[0]
    b = range[1]
    if b < a:
        a = range[1]
        b = range[0]
    return (n >= a) and (n <= b)


def overlap(a, b):
    return contains(a[0], b) or contains(a[1], b) or contains(b[0], a) or contains(b[1], a)


def SATCheck(verticesA, verticesB):
    edgesA = vertices2Edges(verticesA)
    edgesB = vertices2Edges(verticesB)

    edges = edgesA + edgesB

    axes = [numpy.array([edge[1], -edge[0]]) / numpy.linalg.norm(edge) for edge in edges]

    for i in range(len(axes)):
        projectionA = project(verticesA, axes[i])
        projectionB = project(verticesB, axes[i])
        overlapping = overlap(projectionA, projectionB)
        if not overlapping:
            return False
    return True
