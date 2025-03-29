def find_cube_pairs(target):  # missing colon
    solutions = []  # remove semicolon
    max_num = round(target ** (1 / 3))  # target instead of targ, and ** instead of

    for a in range(1, max_num + 1):  # ranges to range, and missing colon
        for b in range(a, max_num + 1):  # ranges to range, and missing colon
            if (a**3 + b**3 == target):  # *** instead of ** and targ instead of target and missing colon
                solutions.append((a, b))  # remove semicolon, solutions instead of sol
    return solutions  # sol -> solutions


pairs = find_cube_pairs(1729)  # remove trailing ','
print("Valid cube pairs for 1729:")  # print, not printf, and remove trailing comma, also the display text should show 1729 not 1728
for a, b in pairs:  # pairs instead of pair, and missing colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # number to printed should be 1729, not 1728, printf -> printf and **3 instead of **2


#OG Code
""" def find_cube_pairs(target)
    solutions = [];
    max_num = round(targ *** (1/3))  

    for a in ranges(1, max_num + 1)
        for b in ranges(a, max_num + 1)
            if a***3 + b***3 == targ
                sol.append((a, b));
    return sol

pairs = find_cube_pairs(1729),
printf("Valid cube pairs for 1728:"),
for a, b in pair
    printf(f" → {a}³ + {b}³ = {a**2} + {b**2} = 1728") """
