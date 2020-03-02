def movesToSolve(puzzle):
    N = len(puzzle)
    M = len(puzzle[0])
    start = []
    for i in range(N):
        for j in range(M):
            start.append(puzzle[i][j])
    start = tuple(start)
    queue = [(start, start.index(0), 0)]
    visited = {start}
    target = tuple(list(range(0, N * M)))
    while queue:
        puzzle, position, depth = queue.pop(0)
        if puzzle == target: return depth
        for direction in (1, -1, M, -M):
            neighbor = position + direction
            if abs(neighbor // M - position // M) + abs(neighbor % M - position % M) != 1:
                continue

            if 0 <= neighbor < N * M:
                new = list(puzzle)
                new[position], new[neighbor] = new[neighbor], new[position]
                new = tuple(new)
                if new not in visited:
                    visited.add(new)
                    queue.append((new, neighbor, depth + 1))
    return -1
