# Type hint
# age: int that mean age should be an integer number. if we enter something else except interger we get and type error
# can_drive() -> bool mean can_drive fn return type boolean.


def can_drive(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False

can_drive(20)