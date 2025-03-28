friends = ['jim', 'joe', 'jane']

print(f"Hello, {friends[0].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[1].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[2].title()}! I would like to invite you to dinner.")

friends.insert(0, 'jill')
friends.insert(2, 'jack')
friends.append('james')

print(friends)

print(f"\nHello, {friends[0].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[1].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[2].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[3].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[4].title()}! I would like to invite you to dinner.")
print(f"Hello, {friends[5].title()}! I would like to invite you to dinner.")