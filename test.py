'''
def cal_hap(start,end):

    hap=0
    i= start

    while i<=end:
        hap += i
        i += 1

    return hap

def get_sum(start,end,baesu):
    
    sum = 0

    for i in range(start, end+1):
        if i%baesu==0:
            sum +=i
        
    return sum

start = int(input("시작값 입력 : "))
end = int(input("끝값 입력 : "))
baesu = int(input("배수 입력 : "))

print("합계",cal_hap(start,end))
print("배수 합계",get_sum(start,end,baesu))
'''

import turtle as t

def square(length):
    t.shape("turtle")
    for i in range(4):
        t.fd(length)
        t.lt(90)
while 1:
    length = int(input("길이 입력 : "))
    square(length)
