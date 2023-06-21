def n(w,f):f=~f;return w if len(w)<3 else w[0]+"[("[f]+n(w[1:-1],f)+"])"[f]+w[-1]
print(f"({n(input(),1)})")