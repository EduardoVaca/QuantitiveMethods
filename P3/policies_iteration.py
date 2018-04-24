import numpy as np


def get_matrixes(fo):
    ms = [list(map(float, x.strip().split(','))) for x in fo.readlines()]
    return [ms[:3], ms[3:6], ms[6:9], ms[9:]]

def get_c(p1, r1, p2, r2):
    c1 = []
    c2 = []
    for i in range(3):
        c1.append(sum(p1[i][j]*r1[i][j] for j in range(3)))
    for i in range(3):
        c2.append(sum(p2[i][j]*r2[i][j] for j in range(3)))
    return [c1, c2]
    
def get_matrixes_based_on_policy(policy, p1, r1, p2, r2):
    selected_p, selected_r = [], []
    for i in range(3):
        selected_p.append(p1[i] if policy[i] == 1 else p2[i])
        selected_r.append(r1[i] if policy[i] == 1 else r2[i])
    return [selected_p, selected_r]

def get_c_based_on_policy(policy, c1, c2):
    selected_c = []
    for i in range(3):
        selected_c.append(c1[i] if policy[i] == 1 else c2[i])
    return selected_c

def get_system_of_equations(alpha, p):
    system = []
    for i in range(3):        
        system.append([p[i][j]*(-alpha) for j in range(3)])
    for i in range(3):
        system[i][i] += 1
    return system

def solve_system_of_equations(system, results):
    return np.linalg.solve(np.array(system), np.array(results)).tolist()

def get_policy_performance(p1, p2, c1, c2, system_vars, alpha):
    performance1, performance2 = [], []
    for i in range(3):
        performance1.append(c1[i]+alpha*(sum(p1[i][j]*system_vars[j] for j in range(3))))
    for i in range(3):
        performance2.append(c2[i]+alpha*(sum(p2[i][j]*system_vars[j] for j in range(3))))
    return [performance1, performance2]

def get_improved_policy(performance1, performance2):
    return [1 if performance1[i] > performance2[i] else 2 for i in range(3)]

p1, r1, p2, r2 = get_matrixes(open('matrixes.txt', 'r'))
c1, c2 = get_c(p1, r1, p2, r2)
alpha = float(input('Alpha: '))
current_policy = [int(x) for x in input('Enter start policy (separate values by space): ').strip().split(' ')]
prev_policy = [0, 0, 0]
while prev_policy != current_policy:
    selected_p, selected_r = get_matrixes_based_on_policy(current_policy, p1, r1, p2, r2)
    system_eq = get_system_of_equations(alpha, selected_p)
    selected_c = get_c_based_on_policy(current_policy, c1, c2)
    system_res = solve_system_of_equations(system_eq, selected_c)
    performance1, performance2 = get_policy_performance(p1, p2, c1, c2, system_res, alpha)
    prev_policy = current_policy
    current_policy = get_improved_policy(performance1, performance2)
    print(current_policy)


