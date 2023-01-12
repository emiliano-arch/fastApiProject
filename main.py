from fastapi import FastAPI

from Suma import Suma

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/prueba/{uno}")
async def Sumar(uno: int):
    return {f"Tu suma de {uno} + n es: " f"{Suma(uno).sumar()}"}

@app.get("/prueba2/{num1}&{num2}")
async def SumarMas(num1: int, num2: int):
    return {f"Tu suma de {num1} + {num2} es: " f"{Suma(num1, num2).sumaCompleta()}"}

#Esta prueba es la buena para usarlo en la calculadora
@app.get("/prueba3/")
async def SumarMas(num1: int = 0, num2: int = 0):
    return {f"Tu suma de {num1} + {num2} es: " f"{Suma(num1, num2).sumaCompleta()}"}
