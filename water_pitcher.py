import sys
import heapq
import functools
from math import ceil, gcd

inf = sys.maxsize

def calc_heuristic(state, target, max_pitcher):
    diff = ceil(abs(target - state[-1][0]) * 2 // max_pitcher)
    return diff


# Iterates through the pitchers to find out every possible state from the currrent state
def get_next_state(state):
    for i, pitchers_i in enumerate(state):
        for j, pitchers_j in enumerate(state):
            if (i != j) and (pitchers_j[1] > pitchers_j[0]) and pitchers_i[0] > 0:
                next_state = list(state)
                next_state[i] = (max([pitchers_i[0] + pitchers_j[0] - pitchers_j[1], 0]), pitchers_i[1])
                next_state[j] = (min([pitchers_i[0] + pitchers_j[0], pitchers_j[1]]), pitchers_j[1])
                yield tuple(next_state)


def print_path(prev_state, state, f_n_dict, g_n_dict, h_n_dict):
    if prev_state[state] != -1:
        print_path(prev_state, prev_state[state], f_n_dict, g_n_dict, h_n_dict)
        
    print(">>> State at the last seach step:")
    print(state)


def A_star(pitchers, target):
    if target % functools.reduce(gcd, pitchers) != 0:
        return -1
    max_pitcher = max(pitchers)
    state = tuple([(inf, inf)] + [(0, capacity) for capacity in pitchers] + [(0, inf)])
    
    
    f_n_dict = {}
    g_n_dict = {}
    h_n_dict = {}
    prev_state = {state: -1}
    
    
    h_n_dict[state] = calc_heuristic(state, target, max_pitcher)
    g_n_dict[state] = 0
    f_n_dict[state] = h_n_dict[state] + g_n_dict[state]
    
    
    closed_set = set()
    open_set = []
    heapq.heapify(open_set)
    heapq.heappush(open_set, (f_n_dict[state], h_n_dict[state], state))
    state_no = 0
    while len(open_set) > 0:
        _, _, curr = heapq.heappop(open_set)
        
        print(f">>> Current state: {curr}")
        print("Distances at the current state:")
        print("g(n) = ", g_n_dict[curr], "\nh(n) = ", h_n_dict[curr], "\nf(n) = ", f_n_dict[curr])
        
        if curr[-1][0] == target:
            print('>>> Target reached! \nNumber of states evaluated: ', state_no)
            print_path(prev_state, curr, f_n_dict, g_n_dict, h_n_dict)
            
            return g_n_dict[curr]
        
        
        closed_set.add(curr)
        for next_state in get_next_state(curr):
            if not next_state in closed_set:
                g_tentative = g_n_dict[curr] + 1
                if g_tentative < g_n_dict.get(next_state, inf):
                    try:
                        idx = open_set.index((f_n_dict.get(next_state), h_n_dict.get(next_state), next_state))
                        open_set[idx] = open_set[-1]
                        open_set.pop()
                        heapq.heapify(open_set)
                    except:
                        pass
                    g_n_dict[next_state] = g_tentative
                    h_n_dict[next_state] = calc_heuristic(next_state, target, max_pitcher)
                    f_n_dict[next_state] = g_n_dict[next_state] + h_n_dict[next_state]
                    prev_state[next_state] = curr
                    
                    heapq.heappush(open_set, (f_n_dict[next_state], h_n_dict[next_state], next_state))
        state_no = state_no + 1


if __name__ == '__main__':
    file = open("input.txt", "r")
    pitchers = list(map(int, file.readline().split(',')))
    target = int(file.readline())
    file.close()
    print("The lowest number of steps required:", A_star(pitchers, target))