def unify(x, y, theta={}):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.startswith('?'):
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.startswith('?'):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) == 0 and len(y) == 0:
            return theta
        elif len(x) == 0 or len(y) == 0:
            return None
        else:
            return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

# Example usage:
facts = [
    ("likes", "John", "pizza"),
    ("likes", "Mary", "pizza"),
    ("likes", "Alice", "?x"),
    ("dislikes", "Bob", "apples")
]

query = ("likes", "?person", "pizza")

for fact in facts:
    substitution = unify(query, fact)
    if substitution is not None:
        print("Substitution:", substitution)
