# code-golf

Small scripts for code golf problems in various languages (but probably Python).


### **Alternesting**
 - Given an input, wrap in parens then go in one character on each side and repeat for brackets. Repeat until you reach the string's core (len <= 2). 
 - `Hello World!` becomes `(H[e(l[l(o[ W]o)r]l)d]!)

### **Print Own Size**
 - Make a script that prints its own byte count.

### **RandInt Until Zero**
 - Print random integers between 0 and 99 (inclusive).
 - Stop *after* printing any 0.

### **Switch Case Tuple**
 - Given a switch case in a nested tuple format `((condition_code_as_str, result), (condition_code_as_str_two, result_two), ...)`, return the result for the first true condition.
