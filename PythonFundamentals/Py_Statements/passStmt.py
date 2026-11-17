###When ever we implement if condition and during the implementation we dont have any logic to put inside
#due to sme business change expectation we just add the pass stmt to avoid the error and stoping the next stmt execution
age=29
if age < 18:
    pass
else:
    print("access granted")
