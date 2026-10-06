import heapq
import random

# 0 = хоосон зай
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def show(board):
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(" ".join(str(x) if x != 0 else "." for x in row))
    print()


# Хоосон зай хаашаа хөдөлж болохыг олох
def get_neighbors(board):
    neighbors = []

    zero = board.index(0)
    row = zero // 3
    col = zero % 3

    directions = [
        (-1, 0),  # дээш
        (1, 0),   # доош
        (0, -1),  # зүүн
        (0, 1)    # баруун
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_board = list(board)

            # Хоосон зай болон нөгөө tile-ийг солино
            new_board[zero], new_board[new_zero] = \
                new_board[new_zero], new_board[zero]

            neighbors.append(tuple(new_board))

    return neighbors


# A* алгоритмын heuristic
# Manhattan Distance
def heuristic(board):
    distance = 0

    for i in range(9):
        tile = board[i]

        if tile != 0:
            goal_index = GOAL.index(tile)

            current_row = i // 3
            current_col = i % 3

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# A* алгоритм
def a_star(start):
    # priority queue
    # (f, g, board)
    queue = []

    g = 0
    h = heuristic(start)
    f = g + h

    heapq.heappush(queue, (f, g, start))

    came_from = {}
    cost_so_far = {start: 0}

    while queue:
        f, g, current = heapq.heappop(queue)

        # Зорилгод хүрсэн
        if current == GOAL:
            path = []

            while current != start:
                path.append(current)
                current = came_from[current]

            path.append(start)

            path.reverse()
            return path

        # Дараагийн боломжит байрлалууд
        for next_board in get_neighbors(current):

            new_cost = g + 1

            if next_board not in cost_so_far or \
                    new_cost < cost_so_far[next_board]:

                cost_so_far[next_board] = new_cost

                h = heuristic(next_board)
                f = new_cost + h

                heapq.heappush(
                    queue,
                    (f, new_cost, next_board)
                )

                came_from[next_board] = current

    return None


# Puzzle-г санамсаргүй хутгах
def shuffle(board):
    board = list(board)

    for _ in range(30):
        neighbors = get_neighbors(tuple(board))
        board = list(random.choice(neighbors))

    return tuple(board)


# -------------------------a
# MAIN PROGRAM
# -------------------------

board = shuffle(GOAL)

print("Эхний puzzle:")
show(board)

print("A* алгоритмаар бодож байна...")

solution = a_star(board)

if solution:
    print("Шийдэл олдлоо!")
    print("Нийт нүүдэл:", len(solution) - 1)
    print()

    for i, step in enumerate(solution):
        print("Алхам", i)
        show(step)

else:
    print("Шийдэл олдсонгүй.")