num1 = 9
num2 = 10
# n = int(input("Enter a number :"))
# print(n)
try:
    print("resource open")
    print(num1/num2)
    
except Exception as e:
    print("Number cannot be divided by zero",e)
except :
    print("Please enter a integer number")  
    print("resource close")
#  Finally statement always will be true
finally:
    print("program run")
    
    
print("Program is running") 

# emanple 1
try:
    list = [9,4,6,2,3]
    index = int(input("Enter a index number :"))
    print(list[index])
    
except ZeroDivisionError as e:
    print("Numnber cannot be divided by zero")
except IndexError as e:
    print("Index not Found plz enter right Index number",e)
except Exception as e:
    print("Something went wrong",e)
    
# emanple 1
  
    
try:
    num = int(input("Enter a number :"))
    assert num % 2 ==0
except:
    print("Not even number")
else:
    reciprocal = 1/num
    print(reciprocal)  