x = int(input())
case = [("x <  5", "less than five"), 
        ("x >= 5", "greater than or equal to five"), 
        ("x == 5", "is five")]

print(next(x[0][1]for x in[*zip(case,(*map(lambda c:eval(c[0]),case),))]if x[1]))