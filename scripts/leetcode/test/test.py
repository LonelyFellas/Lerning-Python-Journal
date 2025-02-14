import inspect
from typing import TypeVar, Callable
T = TypeVar("T")
AnyFunction = Callable[..., T]
class Test:
    @staticmethod
    def case (fn: AnyFunction[T], expected: T):
        result = fn()
        source = ""

        # 获取 lambda 源码
        try:
            source = inspect.getsource(fn).strip()
        except:
            print("无法获取 lambda 源码")

        is_passed = result == expected
        if is_passed:
            print(f"✅{source} 通过了!")
        else:
            print(f"❌{source} 没有通过了! 实际结果是 {result}")


