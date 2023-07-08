from dataclasses import dataclass
from pprint import pprint
import itertools as it
import more_itertools as m_it
import math as m

@dataclass
class Vec2d():
    x: float
    y: float

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

@dataclass
class Body():
    mass: float
    pos: Vec2d
    vel: Vec2d
    acc: Vec2d

bodies = [Body(1000, Vec2d(0, 0), Vec2d(0, 0), Vec2d(0, 0)), 
          Body(1000, Vec2d(100, 100), Vec2d(0, 0), Vec2d(0, 0)), 
          Body(1000, Vec2d(-100, -100), Vec2d(0, 0), Vec2d(0, 0)),
          Body(10, Vec2d(1000, 1000), Vec2d(0, 0), Vec2d(0, 0))]


bodies = [Body(old_b.mass, old_b.pos + (old_b.vel + new_acc), old_b.vel + new_acc, new_acc) for old_b, new_acc in zip(bodies, [Vec2d(acc.x/b.mass, acc.y/b.mass) for b, acc in zip(bodies, [Vec2d(-sum([df.x for df in dfp]), -sum([df.y for df in dfp])) for dfp in m_it.chunked([Vec2d(f*d[0], f*d[1]) for f, d in zip([a.mass * b.mass / (m.sqrt((a.pos.x - b.pos.x)**2 + (a.pos.y - b.pos.y)**2))**2 for a, b in it.permutations(bodies, 2)], [((ps[0].x - ps[1].x) / m.sqrt(sum([(ps[0].x - ps[1].x)**2, (ps[0].y - ps[1].y)**2])), (ps[0].y - ps[1].y) / m.sqrt(sum([(ps[0].x - ps[1].x)**2, (ps[0].y - ps[1].y)**2]))) for ps in it.permutations([b.pos for b in bodies], 2)])], len(bodies) - 1)])])]
