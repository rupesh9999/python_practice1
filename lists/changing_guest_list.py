friends = ['jim', 'joe', 'jane']

print(f"Hello, {friends[0].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[1].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[2].title()}! I would like to invite you to dinner.")

print(f"\n{friends[2].title()} can't make it to dinner.")

friends[2] = 'jill'

print(f"\nHello, {friends[0].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[1].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[2].title()}! I would like to invite you to dinner.")
