from fastapi import FastAPI
# import route data
from routes.index import support_data
# instance of creation
app=FastAPI()

app.include_router(support_data)



