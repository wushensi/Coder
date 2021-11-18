#fastapi_pathParm_numVerify
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

from typing import Optional

from fastapi import Path, Query

# 路径参数、数值校验
#@app.get("/items_pathParm_NumVerify/{item_id}")
#async def read_items(
#    item_id: int = Path(..., title="The ID of the item to get"),
#    q: Optional[str] = Query(None, alias="item-query"),
#):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results

#@app.get("/items_pathParm_NumVerify/{item_id}")
#async def read_items(
#    item_id: int = Path(..., title="The ID of the item to get"),
#    q: Optional[str] = Query(None, alias="item-query"),
#):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results
# 默认参数 必选参数 顺序无关 以下Q是必选参数
'''
{"detail":[{"loc":["query","q"],"msg":"field required","type":"value_error.missing"}]}
'''
# 必选参数
#@app.get("/items_pathParm_NumVerify/{item_id}")
#async def read_items(
#    q: str, item_id: int = Path(..., title="The ID of the item to get")
#):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results
'''
如果你想不使用 Query 声明没有默认值的查询参数 q，同时使用 Path 声明路径参数 item_id，并使它们的顺序与上面不同，
Python 对此有一些特殊的语法。传递 * 作为函数的第一个参数。Python 不会对该 * 做任何事情，但是它将知道之后的所有
参数都应作为关键字参数（键值对），也被称为 kwargs，来调用。即使它们没有默认值。
'''
# 必选参数 q
#@app.get("/items_pathParm_NumVerify/{item_id}")
#async def read_items(
#    *,item_id: int = Path(..., title="The ID of the item to get"), q: str
#):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results
# 数值的校验 大于等于 
'''
{"detail":[{"loc":["path","item_id"],"msg":"ensure this value is greater than or equal to 1","type":"value_error.number.not_ge","ctx":{"limit_value":1}}]}
'''
#@app.get("/items_pathParm_NumVerify/{item_id}")
#async def read_items(*, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results

'''
{"detail":[{"loc":["path","item_id"],"msg":"ensure this value is less than or equal to 1000","type":"value_error.number.not_le","ctx":{"limit_value":1000}}]}
'''
#@app.get("/items_pathParm_NumVerify/{item_id}")
#async def read_items(
#    *,
#    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
#    q: str,
#):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results

@app.get("/items_pathParm_NumVerify/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size":size})
    return results