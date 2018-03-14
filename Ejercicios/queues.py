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
    return lam/mu if s is None else lam/s*mu

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



