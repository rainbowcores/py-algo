import sys, re

def unrepeated (data):
 
    unique_list = []
      
    for value in data:
        if value not in unique_list:
            unique_list.append(value)
 
    return (unique_list) 

if __name__ == "__main__":
    unrepeated()