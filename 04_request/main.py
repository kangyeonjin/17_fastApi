from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/items/")
async def read_items(request : Request):
    #클라이언트 ip
    host = request.client.host
    
    # request 객체로 확인가능한것
    # body(): 본문
    # headers :헤더
    return{"clienthost" : host}

#request Body
#클래스타입으로 만들고, basemodel을 상속받아 구현한다
from pydantic import BaseModel

class Teacher(BaseModel):
    is_working: bool
    name: str
    nickname : str | None = None  #Optional, 선택적으로 넣거나안넣을수있다

@app.post("/teachers")
async def teacher_info(teacher:Teacher):
    
    if teacher.nickname:
        
        return f"안녕하세요 제 이름은{teacher.nickname}이고, 현재 일하는 상태는 {teacher.is_working}입니다"
    return f"안녕하세요 제 이름은{teacher.name}이고, 현재 일하는 상태는 {teacher.is_working}입니다"

#path_parameter -> url에 선언한다
#query_parameter->클래스타입의 매개변수라면
#requestBody -> 그외

#(int)student_no : path_parameter로 받고
#Student : requestBody(이름(str), 나이(int))
#(str)lecture_name : query_parameter

#student no, name, age, lecture_name을 
# 전부 출력하는 문자열로 return해주는 api


from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.post("/student/{student_no}")
async def student_info(
    student_no: int = Path(..., description="학생 번호"),
    student: Student = None,  # request body로 받음
    lecture_name: str = Query(..., description="강의 이름")  # query parameter로 받음
):
    return f"학생 번호: {student_no}, 이름: {student.name}, 나이: {student.age}, 강의 이름: {lecture_name}"


