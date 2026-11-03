name=input("Enter Student name:")
math=float(input("Enter Math marks:"))
english=float(input("Enter English marks:"))
python=float(input("Enter python marks:"))
print(f"Student Name:{name}")

if (math<0 or math>100) or (english<0 or english>100) or (python<0 or python>100):
    print("Invalid marks")
else:
    average_marks=(math+english+python)/3 
    print(f"Average Marks:{average_marks:.2f}")

    if average_marks>=80 and average_marks<=100:
        print("Final Grade:A+")
    elif average_marks>=70 and average_marks<=79:
        print("Final Grade:A")
    elif average_marks>=60 and average_marks<=69:
        print("Final Grade:A-")
    elif average_marks>=50 and average_marks<=59:
        print("Final Grade:B")
    elif average_marks>=40 and average_marks<=49:
        print("Final Grade:C")
    else:
        print("Final Grade:F")



