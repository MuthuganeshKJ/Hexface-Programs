# Contribution J.Muthuganesh

def format_decimal_latex(a):
    return_data = ""
    a = str(a)
    for e in a:
        if(e == '.'):
            if(a[-1] == '0'):
                break
            else:
                return_data += '\cdot'
        else:
            return_data+=e
    return return_data

def format_zero_integer_latex(a):
    if(a == 0):
        return ''
    else:
        return str(int(a))

def format_one_integer(a):

    if(a==1):
        return ''
    else:
        return str(a)
        
def format_complexnumber_latex(a, b):
    operation = '+'
    if(b<0):
        operation = '-'
        b *= -1    
    a = format_zero_integer_latex(a)
    b = format_zero_integer_latex(b)
    if(b == '1'):
        b = ''
    if(a == ''):
       return "(" + "i" + b + ")"
    return "(" + a + " " + operation + " i" + b + ")"

def format_text_to_latex(text):
    text = list(map(str, text.split(' ')))
    rv = ''
    for i in range(len(text)):
        if i==0:
            rv+=text[i]
        else:
            rv+='\,\,'+text[i]
    return (rv)

def format_vector_latex(vector_x):
    vect = "("
    ch = 'i'
    flag = True
    for e in vector_x:
        if(e!=0):
            if(e<0 or flag) :
                vect+= (format_one_integer(e)+ch)
                flag = False
            else:
                vect += ("+"+format_one_integer(e)+ch)
        ch = chr(ord(ch)+1)
    vect += ")"
    return vect 