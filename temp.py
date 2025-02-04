t_count = {"C": 1, "B": 1, "A": 1}
c_count = {"C": 1, "B": 1, "A": 2}


def is_valid_counts()->bool:
    for i in t_count:
        if t_count[i] > c_count[i]:
            return False
    return True

def check(a):
    a.append(0)

abc = []
check(abc)
print(abc)
