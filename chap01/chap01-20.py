def check_same_num(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    same_num = set1.intersection(set2)

    if same_num:
        return True
    else:
        return False

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = check_same_num(list1, list2)
print("두 리스트에 같은 항목이 있나요?", result)