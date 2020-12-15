class Factorial:
    
    class _Fact_iter:

        def __init__(self):
            self.i = 1
            self.fact = 1

        def __next__(self):
            self.fact *= self.i
            self.i += 1
            return self.fact

    def __iter__(self):
        return Factorial._Fact_iter()

fct = Factorial()

import itertools as it

for i, f in zip(it.count(1), it.islice(fct, 10)):
    print(i, f)
