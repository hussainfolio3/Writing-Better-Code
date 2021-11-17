from enum import Enum

class Gender(Enum):
    MALE="MALE"
    FEMALE="FEMALE"

class Ethnicity(Enum):
    ASIAN="ASIAN"
    AMERICAN="AMERICAN"
    AFRICAN="AFRICAN"

@dataclass
class Person:
    gender: Gender
    age: int
    ethnicity: Ethnicity

def describe_person(person_obj: Person):
    if feature_flag_enabled:
        if person_obj.gender == Gender.MALE:
            if person_obj.age > 80:
                print("You are a very old male")
        
        if (person_obj.age > 50 and person_obj.age <= 80) and (person_obj.ethnicity == Ethnicity.AMERICAN or person_obj.ethnicity == Ethnicity.AFRICAN):
            print("You are a slightly old person and belong to either Africa or America.")
            
            
if __name__ == "__main__":
    feature_flag_enabled = True
    person = Person()
    describe_person(person)
