from functools import lru_cache

def move_peg(row_state, start, end):
    assert row_state[start] 
    assert not row_state[end] 
    assert start < end

    new_state = [s for s in row_state]
    new_state[start] = False
    new_state[end] = True

    return new_state

__memoize = dict()

def who_wins(row_state, player_turn = 0, prefix = ""):
    global __memoize
    if row_state == [True, False]:
        __memoize[str(row_state)] = player_turn
        return player_turn

    if str(row_state) in __memoize:
        return __memoize[str(row_state)]

    any_moves_possible = False
    for start, start_peg in enumerate(row_state):
        # skip no start pegs
        if not start_peg:
            continue

        for end in range(start+1, len(row_state)):
            # skip full destinations
            if row_state[end]:
                continue

            any_moves_possible = True

            new_state = move_peg(row_state, start, end)
            if who_wins(new_state, 1-player_turn, prefix + " ") == player_turn:
                __memoize[str(row_state)] = player_turn
                return player_turn

    __memoize[str(row_state)] = 1-player_turn
    return 1-player_turn


def for_gabe(n, p):
    n_pegs = p
    n_holes = n-p
    row_state = [True for _ in range(n_pegs)]
    row_state.extend([False for _ in range(n_holes)])
    print(f"{n_pegs+n_holes}, {n_pegs}, {row_state}: {1+who_wins(row_state)}")


if False:
    for n_pegs in range(1, 5):
        for n_holes in range(1, 5):
            row_state = [True for _ in range(n_pegs)]
            row_state.extend([False for _ in range(n_holes)])
            print(f"{n_pegs}, {n_pegs+n_holes}: {1+who_wins(row_state)}")
for_gabe(128, 87)
print("done")
