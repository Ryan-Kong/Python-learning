asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

```@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")
```
而在3.5以上的Python更新的书写方法，使用 async def来进行规范
```
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
```

总结：
在3.5当中定义异步I/O处理直接使用async & await进行处理
```
async def Model():
    
    ···
    await 
    ···


```