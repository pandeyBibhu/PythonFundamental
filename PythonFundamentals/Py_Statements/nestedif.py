###when we use if statement inside a if statement then its is know as nested if
##inner if statement executes only when outer conditin is true

x=51
if x>10:
    print("above ten")
    if x>20:
        print("above twenty")
    else:
        print("below twenty 20")
# Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
