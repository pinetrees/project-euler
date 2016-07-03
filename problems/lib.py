def get_prime_factors_of(value):
    factors = []
    i = 2
    while i <= value:
        if value % i == 0:
            factors.append(i)
            value = value / i
        else:
            i += 1
    return factors

def is_prime(value):
    i = 2
    while i < value:
        if value % i == 0:
            return False
        i += 1
    return True

def get_lcm(a, b, *args):
    prime_factors = [get_prime_factors_of(a), get_prime_factors_of(b)]
    ds = []
    for factor_set in prime_factors:
        d = {}
        for el in factor_set:
            if el in d:
                d[el] += 1
            else:
                d[el] = 1
        ds.append(d)
    m_dict = {}
    for d in ds:
        for key, value in d.iteritems():
            if key not in m_dict or value > m_dict[key]:
                    m_dict[key] = value
    lcm = 1
    for key, value in m_dict.iteritems():
        lcm *= key**value
    
    for el in args:
        lcm = get_lcm(lcm, el)
    return lcm

