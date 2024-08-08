"""
Sequence are Iterable:

- Whenever python need to iterate over an object x , it calls iter(x)
    1. the iter check whatever a object implement __iter__ method
    2. if __iter__ not implemented but __getitem__ is , then iter create an iterator and tries to fetch item from index 0
    3. if its failed python raise TypeError

- iter(), func get two argument, iter(a, b) :
    a: the function to iter over for ex
        def d6():
            return randint(1, 6)

    b: a marker value which, when returned by the callable causes the iterator to raise StopIteration

- Python standard interface for an iterator has two method:
    __next__ : return next item in series, raising StopIteration if there are no more
    __iter__ : returns self, this allows iterator to be used where an iterable is excepted

    using the next() method, will fetch the next item in series, if there are no more, the iterator is exhausted
    and once is exhausted, an iterator will always raise StopIteration and to go over again a new iterator ,
    must be build

- Now we are going to implement a standard iterable protocol:
    this second version is classic iterator:
"""
# Second Version : A Classic Iterator

import re, reprlib

RE_WORD = re.compile(r'\w+')


class Sentence_1:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):  # <1>
        return SentenceIterator(self.words)  # <2>


class SentenceIterator:

    def __init__(self, words):
        self.words = words  # <3>
        self.index = 0  # <4>

    def __next__(self):
        try:
            word = self.words[self.index]  # <5>
        except IndexError:
            raise StopIteration()  # <6>
        self.index += 1  # <7>
        return word  # <8>

    def __iter__(self):  # <9>
        return self


"""
we can use generator and forget about defining a SentenceIterator
"""


class Sentence_2:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:  # <1>
            yield word  # <2>


"""
the yield key word make a function a generator, every time that next() call the next yield will be generate(not return)
    for example
        def gen_123():
            yield 1
            yield 2
            yield 3
        
        for i in gen_123():
            print i
        >>> 1
        >>> 2
        >>> 3 
"""

"""
now the __iter__ works but its not LAZY:
    Laziness in program is a good thing, a lazy implementation produce the value in a last possible moment
    this save memory and may avoid wasting CPU cycles too
    
LAZY sentence
"""


class Sentence_3:
    def __init__(self, text):
        self.text = text  # <1>

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):  # <2>
            yield match.group()


"""
Coroutine
"""


def generator():
    while True:
        value = yield
        print(f'Received: {value}')


gen = generator()
next(gen)  # Start the generator
gen.send(10)  # Output: Received: 10
gen.send(20)  # Output: Received: 20
gen.close()  # end the generator

