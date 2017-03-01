"""Script for first-order automated theorem proving.
Resources: The Little Prover by Daniel P. Friedman and Carl Eastlund, 
henceforth referred to as TLP."""

'''def cons(x, y):
    return lambda pair: pair(x, y)

def car(pair):
    return pair(lambda p, q: p)

def cdr(pair):
    return pair(lambda p, q: q)'''

# Using python syntax, might switch to LISP

# Basic functions outlined in TLP
def cons(element, list):
    """Add element to the front of the list."""
    list.insert(0, element)
    return list

def car(list):
    """Return first element of non-empty list."""
    return list[0]

def cdr(list):
    """Return the tail of a non-empty list."""
    return list[1:]

def atom(expr):
    """Return False for non-empty lists and True for everything else."""
    if isinstance(expr, list) and expr:
        return False
    else:
        return True

def equal(expr_a, expr_b):
    """Return True if equal, else False."""
    return expr_a == expr_b

def natp(expr):
    """Return True if natural number, False if not."""
    if isinstance(expr, int) and expr > 0:
        return True
    else:
        return False

def size(list):
    '''Count the conses needed to build a value.'''
    return len(list)


