from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# create a class-based model for the "Cat" table
class Cat(base):
    __tablename__ = "Cat"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    age = Column(String)
    breed = Column(String)
    # owner = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create  a new instance of sessionmaker, then point to out engine (the db)
Session = sessionmaker(db)
# opens and actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declaraticve_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer",
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing",
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL Language",
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11",
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft",
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "Word Wide Web",
)

isaac_dearman = Programmer(
    first_name = "Isaac",
    last_name = "Dearman",
    gender = "M",
    nationality = "British",
    famous_for = "Nothing Yet",
)

# creating records for cat table
creamy_dearworth = Cat(
    first_name = "Creamy",
    last_name = "Dearworth",
    gender = "M",
    age = "4",
    breed = "Scottish Fold",
    # owner = "Isaac & Enya",
)

mr_susan_dearworth = Cat(
    first_name = "Mr.Susan",
    last_name = "Dearworth",
    gender = "M",
    age = "4",
    breed = "Scottish Fold",
    # owner = "Isaac & Enya",
)

meatbags = Cat(
    first_name = "Meatbags",
    last_name = "Unknow",
    gender = "M",
    age = "1",
    breed = "asd",
    # owner = "Unknown (Isaac & Enya)",
)

nora_worth = Cat(
    first_name = "Nora",
    last_name = "Worth",
    gender = "F",
    age = "5",
    breed = "Maine Coon",
    # owner = "Trev & Corrie",
)

# add each instance of our cats to our session
session.add(creamy_dearworth)
session.add(mr_susan_dearworth)
session.add(meatbags)
session.add(nora_worth)


# query the database to find all instances of Cat
cats = session.query(Cat)
for cat in cats:
    print(
        cat.id,
        cat.first_name + " " + cat.last_name,
        cat.gender,
        cat.age,
        cat.breed,
        # cat.owner,
    )

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(isaac_dearman)




# updating a single record
# programmer = session.query(Programmer).filter_by(id=10).first()
# programmer.famous_for = "World President"

# commit out session to the database
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")

# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are your sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

