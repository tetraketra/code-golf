import      itertools as  it
import more_itertools as mit
import  numpy         as np
import  numpy.random  as npr
grid = np.zeros((4, 4), int)

while (1):
    grid = [(d := input(f"{grid}\nWhich direction would you like to merge the board? [l,r,u,p]|[q]: ")), np.rot90([next(filter(lambda ab: ab[0] == ab[1], mit.windowed(it.islice(it.accumulate(it.repeat(line), lambda x, _: (lambda obj: [*mit.collapse([(m[2][m[1]] if m[0] != m[1] else ((m[2][0], m[2][1]) if m[2][0] != m[2][1] else (m[2][0] + m[2][1], 0))) for m in mit.mark_ends(mit.windowed(mit.collapse(map(lambda x: (x[0], x[1]) if x[0] != x[1] else (x[0] + x[1], 0), mit.chunked(mit.padded([n for n in obj if n], 0, 4), 2))), 2))])])(x)), 1, None), 2)))[0] for line in np.rot90(grid, eval({"l":"0", "r":"2", "u":"1", "d":"-1", "q":"quit()"}[d]))], -{"l":0, "r":2, "u":1, "d":-1}[d])][1]
    grid[grid==0] = npr.permutation([*mit.padded(mit.repeatfunc(lambda: npr.choice([2, 4], p=[0.9, 0.1]), 2), 0, (grid==0).sum())])

# explanation below
































# ==== how it works ====

# line = np.array([0, 2, 2, 4])

# push all to left and do one merge
# line = mit.padded([n for n in line if n], 0, 4)
# line = mit.collapse(map(lambda x: (x[0], x[1]) if x[0] != x[1] else (x[0] + x[1], 0), mit.chunked(line, 2)))
# line = mit.collapse([(m[2][m[1]] if m[0] != m[1] else ((m[2][0], m[2][1]) if m[2][0] != m[2][1] else (m[2][0] + m[2][1], 0))) for m in mit.mark_ends(mit.windowed(line, 2))])
# one_step = lambda obj: [*mit.collapse([(m[2][m[1]] if m[0] != m[1] else ((m[2][0], m[2][1]) if m[2][0] != m[2][1] else (m[2][0] + m[2][1], 0))) for m in mit.mark_ends(mit.windowed(mit.collapse(map(lambda x: (x[0], x[1]) if x[0] != x[1] else (x[0] + x[1], 0), mit.chunked(mit.padded([n for n in obj if n], 0, 4), 2))), 2))])]

# repeat until two same in a row
# line_states = it.islice(it.accumulate(it.repeat(line), lambda x, _: one_step(x)), 1, None)
# line_state_sets = mit.windowed(line_states, 2)
# a = next(filter(lambda ab: ab[0] == ab[1], line_state_sets))[0]
# print(a)


# a = next(filter(lambda ab: ab[0] == ab[1], mit.windowed(it.islice(it.accumulate(it.repeat(IMPORTANT_FILLER), lambda x, _: (lambda obj: [*mit.collapse([(m[2][m[1]] if m[0] != m[1] else ((m[2][0], m[2][1]) if m[2][0] != m[2][1] else (m[2][0] + m[2][1], 0))) for m in mit.mark_ends(mit.windowed(mit.collapse(map(lambda x: (x[0], x[1]) if x[0] != x[1] else (x[0] + x[1], 0), mit.chunked(mit.padded([n for n in obj if n], 0, 4), 2))), 2))])])(x)), 1, None), 2)))[0]
# print(a)