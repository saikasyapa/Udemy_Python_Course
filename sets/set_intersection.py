from primes_squares import squares_generator,primes_generator

evens =set(range(0,50,2))
odds = set(range(1,50,2))
print(evens)
print(odds)

primes = set(primes_generator(100))
print(f"primes {primes}")
squares = set(squares_generator(100))
print(f"squares {squares}")
print(80 * "*")
print(odds.intersection(squares))
print(evens.intersection(squares)) ### or
print(evens & squares)

### pass an iterable to the method
even_squares = evens.intersection(squares_generator(100))
print(even_squares)