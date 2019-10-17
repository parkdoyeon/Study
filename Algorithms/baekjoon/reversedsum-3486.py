N = int(input())
cases = []
answer = []
for _ in range(N):
    cases.append(str(input()).split())

for c in cases:
    one, two = (int(c[0][::-1].strip('0')), int(c[1][::-1].strip('0')))
    answer.append(str(one+two)[::-1].strip('0'))

for a in answer:
    print(a)