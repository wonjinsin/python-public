class Foo():
    bar = 'is bar'

    def __init__(self, *args, **kwargs):
        self.bar = kwargs['bar']


foo = Foo(bar='is not bar')
print(foo.bar)
