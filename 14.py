a,b=map(int,input().split())
result = []
result.append(a+b)
result.append(a-b)
result.append(a*b)
result.append(a/b)
result.append(a+b)
result.append(a**b)
result.append(b+a)
result.append(b-a)
result.append(b*a)
result.append(b/a)
result.append(b+a)
result.append(b**a)
print("%f" % max(result))