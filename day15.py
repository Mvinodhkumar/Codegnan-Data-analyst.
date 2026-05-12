'''
Generators
-----------
-->Generators in python is enable lazy evaluation for producing
sequence of values efficiently.
-->They differ from regular functions by execution and resuming
on demand .
-->Generators create iterators that yield values one at a time
using the yield keyword.

Functions vs Generators
------------------------
-->Regular function execute fully upon call and return a single
value,terminating afterward.
-->Generators use yield to produce multiple value lazily,acting
like itertors without building the entire sequence in memory.
def count_(num):
    i = 1
    while i<=num:
        yield i
        i+=1
Gene_ = count_(3)
print(next(Gene_))
print(next(Gene_))
print(next(Gene_))

yield
-------
-->Yield pauses the generator functions saves its state
(local,variable,position).and return the yield value to caller.

Next
------
-->This advances the generator by executing until the next yield
returning that value, subsquent calls resume from there.'''
def message_gen():
    yield ("first message")
    yield ("second message")
gen = message_gen()
print(next(gen))
print(next(gen))
    

















