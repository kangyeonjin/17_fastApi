from fastapi import FastAPI, Depends
from database import session_local, engine
import models, schemas, teacher_crud
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# 제너레이터 함수
# 함수가 제너레이팅한 객체를 반환하게 하는 키워드
#데이터베이스 세션을 안전하게 생성하고 종료함
def get_db():
    db = session_local() #데이터베이스 세션을 생성
    try:
        yield db #생성한 세션을 호출자에게 반환
    finally:
        db.close()  #호출자가 세션사용을마친후 세션을 닫음

#등록
@app.post("/teachers", response_model=schemas.TeacherResponse)
async def create_teacher(
    teacher : schemas.TeacherCreate, 
    db : Session = Depends(get_db)
    ):
    
    response = teacher_crud.create_teacher(db, teacher)
    
    return response

#단일조회
@app.get("/teacher/{teacher_id}", response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id:int, db: Session = Depends(get_db)):
    
    db_teacher = teacher_crud.get_teacher_by_id(db, teacher_id)
    
    return db_teacher

#전체조회
@app.get("/teachers", response_model=list[schemas.TeacherResponse])
async def find_all_teachers(db: Session = Depends(get_db)):
    all_teachers = teacher_crud.get_all_teachers(db)
    return all_teachers

#teacher수정
@app.put("/teachers/{teacher_id}", response_model=schemas.TeacherResponse)
async def update_teacher(
    teacher_id:int,
    teacher: schemas.TeacherUpdate,
    db: Session =  Depends(get_db)
):
    update_teacher = teacher_crud.update_teacher(db, teacher_id, teacher)
    return update_teacher

#teacher 삭제
@app.delete("/teachers/{teacher_id}", status_code=204)

async def delete_teacher(teacher_id:int, db:Session = Depends(get_db)):
    
    teacher_crud.delete_teacher(db, teacher_id)
    
    return None








#등록
@app.post("/student", response_model=schemas.StudnetResponse)
async def create_student(
    student : schemas.studentCreate, 
    db : Session = Depends(get_db)
    ):
    
    response = student_crud.create_student(db, student)
    
    return response

#단일조회
@app.get("/student/{student_id}", response_model=schemas.StudentResponse)
async def find_studnet_by_id(student_id:int, db: Session = Depends(get_db)):
    
    db_studnet = student_crud.get_student_by_id(db, studnet_id)
    
    return db_studnet

#전체조회
@app.get("/studnets", response_model=list[schemas.StudentResponse])
async def find_all_students(db: Session = Depends(get_db)):
    all_student = student_crud.get_all_students(db)
    return all_students

#student수정
@app.put("/students/{student_id}", response_model=schemas.StudnetResponse)
async def update_student(
    student_id:int,
    student: schemas.StudentUpdate,
    db: Session =  Depends(get_db)
):
    update_studnet = student_crud.update_student(db, student_id, student)
    return update_student

#teacher 삭제
@app.delete("/students/{student_id}", status_code=204)

async def delete_student(student_id:int, db:Session = Depends(get_db)):
    
    student_crud.delete_student(db, student_id)
    
    return None
