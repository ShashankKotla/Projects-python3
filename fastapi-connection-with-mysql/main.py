from fastapi import FastAPI, HTTPException #fastAPI is the class, which provides all functionality's.
import mysql.connector
from pydantic import BaseModel #Date serialization and validation can be done
from typing import Optional


# httpExecption can be used to show raise error to client


class structure(BaseModel): #structure format
    table : str
    id: int
    name: str
    age: Optional[int] = None

app = FastAPI() #instance of class fastAPI

def mysql_connection():
    try:
        db_conn = mysql.connector.connect(
            database = "", #add db name
            user="", #add user name
            port="", #add port
            password="", #add password
            host = "localhost"
            )
        print("Connection Successful")
        return db_conn
    except mysql.connector.Error as err:
        print("Some thing went wrong:", err)
    
@app.get("/") # path operation decorator.path is also commonly called an endpoint or a route 
async def tables(): #path operation function
    conn= mysql_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Failed to connect to mysql database")
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        # cursor.close()
        return [{x} for x in cursor]
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Failed to get the tables names from mysql database: {err}")
    
    
@app.get("/desc_values")
async def desc_values(table:str):
    conn = mysql_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Failed to connect to mysql database")
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        return [{y} for y in cursor]
    except mysql.connector.Error as err2:
        raise HTTPException(status_code=500, detail=f"Failed to get the tables names from mysql database: {err2}")
    

@app.post("/add_values")
async def insert_values(item: structure, table):
    conn = mysql_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Failed to connect to mysql database")
    try:
        cursor = conn.cursor()
        exe = f"INSERT INTO {table}(name, age) VALUES {item.name,item.age}"
        cursor.execute(exe)
        conn.commit()
        return{"message": "Values inserted successfully"}
    except Exception as err3:
        raise HTTPException(status_code=500, detail=f"failed to insert into employee table: {err3}")
    

@app.put("/change_character")
async def change_character(updated_value: str, previous_value:str, table:str):
    conn = mysql_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail=f"Failed to connect to mysql database")
    try:
        cursor = conn.cursor()
        value_change = f"UPDATE {table} SET name={updated_value} WHERE name={previous_value}"
        cursor.execute(value_change)
        conn.commit()
        return {"message": "Value updated successfully"}
    except mysql.connector.Error as err3:
        raise HTTPException(status_code=500, detail=f"failed to update value in database{err3}")
    
@app.delete("/delete_value")
async def delete_value(delete_item: str, table:str):
    conn = mysql_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Failed to connect to mysql database")
    try:
        cursor = conn.cursor()
        delete_value = f"DELETE FROM {table} WHERE name={delete_item}"
        cursor.execute(delete_value)
        conn.commit()
        return {"massage": "deleted item succesfully"}
    except mysql.connector.Error as err4:
        raise HTTPException(status_code=500, detail=f"failed to delete item from the database{err4}")
    



