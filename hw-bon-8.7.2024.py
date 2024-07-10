user_id1: str = str(input("Insert user 1 id: "));
first_name1: str = str(input("Insert user 1 first name:"));
last_name1: str = str(input("Insert user 1 last name: "));
height1: float = float(input("Insert user 1 height: "));
birth_year1: int = int(input("Insert user 1 birth year: "));

user_id2: str = str(input("Insert user 2 id: "));
first_name2: str = str(input("Insert user 2 first name:"));
last_name2: str = str(input("Insert user 2 last name: "));
height2: float = float(input("Insert user 2 height: "));
birth_year2: int = int(input("Insert user 2 birth year: "));

user_id3: str = str(input("Insert user 3 id: "));
first_name3: str = str(input("Insert user 3 first name:"));
last_name3: str = str(input("Insert user 3 last name: "));
height3: float = float(input("Insert user 3 height: "));
birth_year3: int = int(input("Insert user 3 birth year: "));

print("f:user 1 id: {user_id1}");
print(f"first name: {first_name1: <10}");
print(f"last name: {last_name1}");
print(f"height: {height1: .2f}");
print(f"birth year: {birth_year1}");

print("f:user 2 id: {user_id2}");
print(f"first name: {first_name2: <10}");
print(f"last name: {last_name2}");
print(f"height: {height2: .2f}");
print(f"birth year: {birth_year2}");

print("f:user 3 id: {user_id3}");
print(f"first name: {first_name3: <10}");
print(f"last name: {last_name3}");
print(f"height: {height3: .2f}");
print(f"birth year: {birth_year3}");
#or

print(f"{user_id1:<{10}} {first_name1:<{10}} {last_name1:<{10}} {height1:<{10}.2f} {birth_year1:<{10}}");
print(f"{user_id2:<{10}} {first_name2:<{10}} {last_name2:<{10}} {height2:<{10}.2f} {birth_year2:<{10}}");
print(f"{user_id3:<{10}} {first_name3:<{10}} {last_name3:<{10}} {height3:<{10}.2f} {birth_year3:<{10}}");
