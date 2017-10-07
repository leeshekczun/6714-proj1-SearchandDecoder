## Submission.py for COMP6714-Project1
import math
###################################################################################################################
## Question No. 0:
def add(a, b): # do not change the heading of the function
    return a + b

# def intersection_galloping(a, b):
#     # just in case these lists have been traversed.
#     a.reset()
#     b.reset()
#     count = 0
#
#     ret = []
#     while not a.eol() and not b.eol():
#         if a.elem() == b.elem():
#             ret.append(a.elem())
#             a.next()  # Note that here you are only allowed to move the cursor of one InvertedList Object.
#         else:
#             if a.elem() < b.elem():
#                 gallop_to(a,b.elem())
#             else:
#                 gallop_to(b,a.elem())
#     # end_while
#     return ret
#
# class InvertedList:
#     def __init__(self, l):
#         self.data = l[:]  # make a copy
#         self.cur = 0  # the cursor
#
#     def get_list(self):
#         return self.data
#
#     def eol(self):
#         # we use cur == len(list) to indicate EOL
#         return False if self.cur < len(self.data) else True
#
#     def next(self, val=1):
#         # does not allow cur to be out-of-range, but use len(list) to indicate EOL
#         self.cur = min(self.cur + val, len(self.data))
#
#     def elem(self):
#         if self.eol():
#             return None
#         else:
#             return self.data[self.cur]
#
#     def peek(self, pos):
#         # look at the element under the current cursor, but does not advance the cursor.
#         if pos < len(self.data):
#             return self.data[pos]
#         else:
#             return None
#
#     def reset(self):
#         self.cur = 0
#



###################################################################################################################
## Question No. 1:
def gallop_to(a, val):  # do not change the heading of the function
    current_cur = 0
    L = a.data[a.cur:]
    delta = 1
    while current_cur + delta < len(L) and L[current_cur + delta] < val:
            delta *= 2
    gamma = delta // 2
    if current_cur + delta <= len(L):
        bin_list = L[(current_cur + gamma):(current_cur + delta + 1)]
        target_cur = binarysearch(bin_list, val,0,len(bin_list)-1)
        a.cur += (target_cur + gamma)
        return        
    else:
        bin_list = L[(current_cur + gamma):]
        target_cur = bsearch(bin_list, val,0,len(bin_list)-1)
        a.cur += (target_cur + gamma)
        return


def binarysearch(array,number,lo,hi):
    if number>array[-1]:
        return len(array)
    mid = (lo + hi) // 2  # midpoint in array
    if number == array[mid]:
        return mid  # number found here
    elif lo == hi:
        return lo
    elif number < array[mid]:
        return binarysearch(array,number, lo, mid - 1)  # try left of here
    else:
        return binarysearch(array,number, mid + 1, hi)  # try above here
###################################################################################################################
## Question No. 2:

def Logarithmic_merge(index, cut_off, buffer_size):  # do not change the heading of the function
    z = {0: []}
    indexs = {}
    for i in range(cut_off):
        z[0].append(index[i])
        z0 = z[0]
        if len(z0) == buffer_size:
            count = 0
            while True:
                if count in indexs:
                    z[count + 1] = indexs[count] + z[count]
                    indexs.pop(count)
                    count += 1
                else:
                    indexs[count] = z[count]
                    break
            z[0] = []
    result = []
    result.append(sorted(z[0]))
    for i in range(max(indexs) + 1):
        if i in indexs:
            result.append(sorted(indexs[i]))
        else:
            result.append([])
    return result



###################################################################################################################
## Question No. 3:

def decode_gamma(inputs):# do not change the heading of the function
    count = 0
    output = []
    for i in range(0,len(inputs)):
        if inputs[i] == '0':
            count = i
            break
    first = inputs[0:count+1]
    second = inputs[count+1:count+count+1]
    if len(inputs)>(2*count+1):
        inputs = inputs[(count+count+1):]
    elif len(inputs)==(2*count+1):
        inputs = []
    a=2**(len(first)-1)
    b=int(second,2)
    output.append(a+b)
    if len(inputs) == 0:
        return  output
    else:
        return output + decode_gamma(inputs)

def decode_delta(inputs):# do not change the heading of the function
    count = 0
    output = []
    for i in range(0, len(inputs)):
        if inputs[i] == '0':
            count = i
            break
    first = inputs[0:count + 1]
    second = inputs[count + 1:count + count + 1]
    a = 2 ** (len(first) - 1)
    b = int(str(second), 2)
    f = (a+b-1)
    third = inputs[count + count + 1:count + count + 1 +f]
    if str(third) == '':
        c = 0
    else:
        c = int(str(third),2)
    output.append(2**f+c)
    if len(inputs) >(len(first)+len(second)+f):
        inputs = inputs[(len(first)+len(second)+f):]
    elif len(inputs)==(len(first)+len(second)+f):
        inputs = []
    if len(inputs)==0:
        return output
    else:
        return output + decode_delta(inputs)


def decode_rice(inputs, b):# do not change the heading of the function
    count = 0
    output = []
    for i in range(0, len(inputs)):
        if inputs[i] == '0':
            count = i
            break
    first = inputs[0:count + 1]
    a = count * b
    second = inputs[count+1:(count+1 + int(math.log2(b)))]
    c = int(str(second),2)
    output.append(a+c)
    if len(inputs)>(count+1 + int(math.log2(b))):
        inputs = inputs[(count+1 + int(math.log2(b))):]
    elif len(inputs)==(count+1 + int(math.log2(b))):
        inputs = []
    if len(inputs)==0:
        return output
    else:
        return output + decode_rice(inputs,b)
