V = int(input())
P1_hr = int(input())
P2_hr = int(input())
hr = float(input())
P1_total = (P1_hr*hr)
P2_total = (P2_hr*hr)

water_total = P1_total + P2_total

if V >= water_total:
    print(f'The pool is {int((water_total/V)*100)}% full. Pipe 1: {((P1_total/water_total)*100)}%. Pipe2: {int((P2_total/water_total)*100)}%.')
else:
    print(f'For {hr} hours the pool overflows with {water_total-V} liters')
