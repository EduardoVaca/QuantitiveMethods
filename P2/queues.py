"""
Author: Eduardo Vaca
Queues
"""
import math

def print_dict(d):
    """Prints a dictionary in format
    PARAMS:
    - d : dictionary
    """
    for k,v in d.items():
        print('{}: {}'.format(k, v))

def little_law(lam, mu, w_q):
    """Computes Little Law's formulas
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    - w_q : Expected time of wait in the queue (mean)
    RETURNS:
    - dictionary with Little Law's values
    """
    results = {'lam': lam, 'mu': mu, 'Wq': w_q}
    results['Lq'] = results['lam']*results['Wq']
    results['Ws'] = results['Wq']+1/results['mu']
    results['Ls'] = results['lam']*results['Ws']
    print_dict(results)
    return results

def utility_factor(lam, mu, s=None):
    """Computes utility factor
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    - s : servers available
    RETURNS:
    - utility factor
    """
    return lam/mu if s is None else lam/(s*mu)

def mm1_performance(lam, mu):
    """Computes performance mesures from M/M/1 model
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    RETURNS:
    - Performance measures
    """
    results = {'lam': lam, 'mu': mu}
    results['Ls'] = lam/(mu-lam)
    results['Lq'] = pow(lam,2)/(mu*(mu-lam))
    results['Ws'] = 1/(mu-lam)
    results['Wq'] = lam/(mu*(mu-lam))
    return results

def mm1_prob_queue_len(lam, mu, n):
    """Computes performance probabilities related to queue length from M/M/1 model
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    - n : number of x in queue
    RETURNS:
    - Probabilities
    """
    results = []
    p = utility_factor(lam, mu)
    results.append(('P({})'.format(n), (1-p)*pow(p, n)))
    results.append(('P(Ls>{})'.format(n), pow(p, n+1)))    
    return results

def mm1_prob_queue_wait(lam, mu, t):
    """Computes performance probabilites related to the wait of the queue from M/M/1 model
    - lam : rate of arrivals
    - mu : rate of service
    - t : time on queue
    """
    results = []
    p = utility_factor(lam, mu)
    results.append(('P(Ws > {})'.format(t), math.exp(-1*mu*(1-p)*t)))
    results.append(('P(Wq > {})'.format(t), p*math.exp(-1*mu*(1-p)*t)))
    return results

def mms_performance(lam, mu, s):
    """Computes performance mesures from M/M/S model
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    - s : number of servers to operate
    RETURNS:
    - Performance measures
    """
    results = {'lam': lam, 'mu': mu, 's': s}
    results['Lq'] = (pow(lam/mu, s)*mms_p0(lam, mu, s)*utility_factor(lam, mu, s=s))/(math.factorial(s)*pow(1-utility_factor(lam, mu, s=s), 2))
    results['Wq'] = results['Lq']/lam
    results['Ws'] = results['Wq'] + 1/mu
    results['Ls'] = lam*results['Ws']
    return results


def mms_p0(lam, mu, s):
    """Computes prob of 0 servers
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    - s : number of servers to operate
    RETURNS:
    - Prob of 0 servers
    """
    return 1 / (sum(pow(lam/mu, n)/math.factorial(n) for n in range(s)) + pow(lam/mu, s)/(math.factorial(s)*(1-utility_factor(lam, mu, s=s))))

def mms_pn(lam, mu, s, n_s):
    """Computes prob of n servers
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    - s : number of servers to operate
    - n_s : list of servers to obtain prob
    RETURNS:
    - Prob of n servers
    """
    p0 = mms_p0(lam, mu, s)
    return [(pow(lam/mu, n)*p0)/math.factorial(n) for n in n_s if n >= 0 and n <= s] + [(pow(lam/mu, n)*p0)/(math.factorial(s)*pow(s, n-s)) for n in n_s if n > s]

def mms_costs(lam, mu, s, cs, cw):
    """Method that computes Model M/M/S Costs
    PARAMS:
    - lam : rate of arrivals
    - mu : rate of service
    - s : number of servers to operate
    - cs : cost of each server
    - cw : cost of wait
    """
    perf_results = mms_performance(lam, mu, s)
    results = {'Ccs': cs*s, 'CwLs': cw*perf_results['Ls'], 'Ls': perf_results['Ls']}
    results['CTotal'] = results['Ccs']+results['CwLs']
    return results



