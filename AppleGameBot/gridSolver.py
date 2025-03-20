def dfs(i, j, path, current_sum, grid, rows, cols, directions) :
    if len(path) >= 2 and current_sum == 10 :
        return path
    if current_sum > 10 :
        return None

    for di, dj in directions :
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != -1 and (ni, nj) not in path :
            new_val = grid[ni][nj]
            result = dfs(ni, nj, path + [(ni, nj)], current_sum + new_val, grid, rows, cols, directions)
            if result is not None :
                return result
        ni2, nj2 = i + 2*di, j + 2*dj
        mi, mj = i + di, j + dj
        if 0 <= ni2 < rows and 0 <= nj2 < cols and grid[ni2][nj2] != -1:
            if grid[mi][mj] == -1 and (ni2, nj2) not in path :
                new_val = grid[ni2][nj2]
                result = dfs(ni2, nj2, path + [(ni2, nj2)], current_sum + new_val, grid, rows, cols, directions)
                if result is not None :
                    return result
    return None

def solve_grid(grid) :
    group_bboxes = []
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    
    found_group = True
    while found_group:
        found_group = False
        for i in range(rows) :
            for j in range(cols) :
                if grid[i][j] != -1:
                    result = dfs(i, j, [(i, j)], grid[i][j], grid, rows, cols, directions)
                    if result is not None :
                        bbox = ((min(r for r, c in result), min(c for r, c in result)),
                                (max(r for r, c in result), max(c for r, c in result)))
                        bbox_sum = 0
                        valid = True
                        for r in range(bbox[0][0], bbox[1][0] + 1) :
                            for c in range(bbox[0][1], bbox[1][1] + 1) :
                                if grid[r][c] != -1 :
                                    bbox_sum += grid[r][c]
                                    if bbox_sum > 10 :
                                        valid = False
                                        break
                            if not valid:
                                break
                        if valid and bbox_sum == 10 :
                            group_bboxes.append(bbox)
                            for r in range(bbox[0][0], bbox[1][0] + 1) :
                                for c in range(bbox[0][1], bbox[1][1] + 1) :
                                    grid[r][c] = -1
                            found_group = True
                            break
            if found_group:
                break
    return group_bboxes

def find_groups(grid) :
    rows, cols = len(grid), len(grid[0])
    found_groups = set()
    for i in range(rows) :
        for j in range(cols) :
            if grid[i][j] != -1 :
                dfs([(i, j)], grid[i][j])
    return [list(g) for g in found_groups]

def remove_group(grid, group) :
    for i, j in group:
        grid[i][j] = -1

def get_bounding_box(group) :
    rows = [i for i, j in group]
    cols = [j for i, j in group]
    return ((min(rows), min(cols)), (max(rows), max(cols)))

def print_grid(grid) :
    for row in grid:
        for i in range(0, len(row), 1) :
            if (row[i] == -1) :
                row[i] = 0
        print(" ".join(f"{val:2d}" for val in row))
"""
if __name__ == '__main__' :
    grid = generate_grid()
    print_grid(grid)
    print("")
    
    total_removals = solve_grid(grid)
    print_grid(grid)

    print("")
    print(f"{total_removals}")
"""