names = ['garfield', 'snoopy', 'peter griffin', 'ted kaczynski']
sorted_names = sorted(names, key=lambda x: (len(x), x))
print(sorted_names)