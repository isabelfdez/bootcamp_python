kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

print("First method:")
print('\n'.join('{} was created by {}'.format(key, value) for key, value in kata.items()))
print("\nSecond method:")
print('\n'.join(f'{key} was created by {value}' for key, value in kata.items()))

