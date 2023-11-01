from typing import Dict, Any
from pilot.model.cache import Cache


class InMemoryCache(Cache):
    def __init__(self) -> None:
        "Initialize that stores things in memory."
        self._cache: Dict[str, Any] = {}

    def create(self, key: str) -> bool:
        pass

    def clear(self):
        return self._cache.clear()

    def __setitem__(self, key: str, value: str) -> None:
        self._cache[key] = value

    def __getitem__(self, key: str) -> str:
        return self._cache[key]

    def __contains__(self, key: str) -> bool:
        return self._cache.get(key, None) is not None


# 上面这两段代码，我不太理解这里面的类的继承，子类如何继承并实现父类的方法，冲突了怎么办？调用的时候那会调用的是子类的还是父类的？

# 文心一言4.0回复
"""
在Python中，类的继承是一种机制，允许一个类（称为子类或派生类）继承另一个类（称为父类或基类）的属性和方法。
通过继承，子类可以重用父类的代码，并且可以添加或覆盖父类的行为。

在上面的代码中，InMemoryCache类是Cache类的子类。Cache类定义了一些抽象方法，如create, clear, __getitem__, __setitem__, 和__contains__。
这些方法在Cache类中没有具体的实现（create方法有一个空的实现，但这是一个特殊的情况），子类需要提供这些方法的具体实现。

当子类继承父类时，它会自动继承父类的所有属性和方法。然后，子类可以提供这些方法的具体实现。如果子类提供了父类方法的实现，那么会覆盖父类的方法。
这就是所谓的"方法覆盖"或"方法重写"。

例如，在上面的代码中，InMemoryCache类提供了clear, __getitem__, __setitem__, 和__contains__方法的实现。
这些实现覆盖了Cache类中的相应方法。因此，如果你创建一个InMemoryCache的实例并调用这些方法，将会调用InMemoryCache类中的实现，而不是Cache类中的。

对于create方法，由于InMemoryCache类并没有提供具体的实现，如果你尝试调用这个方法，将会使用Cache类中的实现，如果Cache类也没有实现，那么会抛出一个NotImplementedError。

至于冲突的问题，一般来说，如果子类的方法和父类的方法有相同的名字和参数列表，那么子类的方法会覆盖父类的方法。
这就是解决冲突的方式。子类可以根据自己的需要重写父类的方法，以提供更具体的实现。当然，如果子类需要调用父类的方法，可以使用super()函数来调用。
例如，如果你在InMemoryCache的create方法中调用super().create(key)，那么将会调用Cache类的create方法。

总的来说，子类会继承父类的方法和属性，然后可以根据需要重写或添加新的方法和属性。在调用时，会优先调用子类的实现，如果没有子类的实现，则会调用父类的实现。
如果父类和子类都有相同的实现，那么子类的实现会覆盖父类的。
"""
