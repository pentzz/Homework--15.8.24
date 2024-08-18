# Task a
tuple1: tuple[int] = (99,)

#Task b
tuple2: tuple[int] = (77, 88, 99)


#Task c
def get_len(a: tuple) -> int:
    return len(a)


#Task d
def join_tuple(a: tuple, b: tuple) -> tuple:
    return a + b


#Task e
def common_tuple(a: tuple, b: tuple) -> tuple:
    com = []
    for item in a:
        if item in b:
            com.append(item)
    com = tuple(com)
    return com


#Task f
def different_tuple(a: tuple, b: tuple) -> tuple:
    diff = []
    for item in a:
        if item not in b:
            diff.append(item)
    for item in b:
        if item not in a and item not in diff:
            diff.append(item)
    com = tuple(diff)
    return com


#Task g
def index_in_tuple(a: tuple, index: int) -> str:
    if index < 0 or index > len(a):
        return None
    return a[index]


#Task h
def reverse_tuple(a: tuple) -> tuple:
    return a[::-1]


#Task i
def div_in_tup(a: tuple, num: int) -> int:
    return len([x for x in a if num % x == 0])


# Task j
def multi_tuple(a: tuple, num: int) -> tuple:
    return a * num


#Task k
def index_tup(a: tuple) -> tuple:
    return tuple((a[i], i) for i in range(len(a)))


#Task l
def dict_from_tup(a: tuple) -> dict:
    result = {}
    result['max'] = max(a)
    result['min'] = min(a)
    result['average'] = sum(a) / len(a)
    result['sum'] = sum(a)
    result['count'] = len(a)
    result['sort'] = sorted(a)
    result['reverse sort'] = sorted(a, reverse=True)
    appearance = {}
    for number in a:
        if number in appearance:
            appearance[number] += 1
        else:
            appearance[number] = 1
    result['appearance'] = appearance
    return result


#Task m
def return_string(a: tuple) -> str:
    result = ""
    for i in range(len(a)):
        result = result + a[i]
    return result


#Task n
def return_tuple(a: str) -> tuple:
    return tuple(a)


# Task o
def return_tup_without_num(a: tuple, num: int) -> tuple:
    return tuple([x for x in a if x != num])


#Task p
def no_dup_tuple(a: tuple) -> tuple:
    no_dup_list = []
    for i in range(len(a)):
        if a[i] not in no_dup_list:
            no_dup_list.append(a[i])
    return tuple(no_dup_list)


#Task q
def return_index_of_tup(a: tuple, num: int) -> tuple:
    temp_list = []
    for i in range(len(a)):
        if a[i] == num:
            temp_list.append(i)
    return tuple(temp_list)


#Task r
def names_and_grades() -> tuple:
    names: list = []
    grades: list = []
    while True:
        try:
            name = input("Please enter a name: (enter 'done' to finish) ")
            if name.lower() == "done":
                break
            if name == "" or name == " ":
                print("Please enter a valid name!\nTry again..")
                continue
            names.append(name)
        except:
            print("Please enter a valid name!")
    while len(grades) != len(names):
            try:
                grade: int = int(input("Please enter a grade: (enter -999 to finish) "))
                if grade == -999:
                    break
                if grade < 0 or grade > 100:
                    print("Please enter the grade in range 0-100!\nTry again..")
                    continue
                grades.append(grade)
            except:
               print("Please enter a valid grade!")
    return tuple(zip(names, grades))
