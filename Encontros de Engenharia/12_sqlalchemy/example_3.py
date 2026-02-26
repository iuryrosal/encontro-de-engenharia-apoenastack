from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, String, Double, create_engine, text

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    salary = Column(Double, nullable=False)

    def __repr__(self) -> str:
        return f"Employee(id={self.id}, name='{self.name}', salary={self.salary})"

engine = create_engine('sqlite:///database.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

with Session() as session:
    new_employee = Employee(name='Alice', salary=9000)
    session.add(new_employee)
    session.commit()

    print(session.query(Employee).all())

    session.query(Employee).filter(Employee.name == 'Alice').update({Employee.salary: Employee.salary + 1000})
    session.commit()

    print(session.query(Employee).all())
    
    session.query(Employee).filter(Employee.name == 'Alice').delete()
    session.commit()

    print(session.query(Employee).all())