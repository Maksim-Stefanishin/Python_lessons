def calc_count(sp):
    total = 0
    for el in sp:
        # if type(el) == type([]):
        if isinstance(el, list):
            total += calc_count(el)
        else:
            total += el
    return total




count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)
print(calc_count(count_all))