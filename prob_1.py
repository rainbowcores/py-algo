import sys, re

def numeric (data):
 
    pattern = re.compile(r'[^0-9]')
    s = re.sub(pattern, '', str(data))
 
    return (s) 

if __name__ == "__main__":
    numeric((sys.argv[1]))