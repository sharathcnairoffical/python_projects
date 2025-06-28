import json
from typing import Union
from vectorEmbedding import  process_request
from fastapi import FastAPI


from data_transfer_object import MovieRequest
app = FastAPI()

@app.get("/test/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/test/insert-vector-db")
async def callVectorDbForInsertion():
    test_movie = MovieRequest("Inception", "A mind-bending thriller where dreams are real.")
    results,error = await process_request(test_movie)
    if error!= "":
        return json.dump({'error':error})
    else:
        return json.dump({'Data':results})

