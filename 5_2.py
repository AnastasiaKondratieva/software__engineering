###UTF-8###

result = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

print(sorted(result)[:3:])
print(sorted(result, reverse=True)[:3:])

res = []
for x in result:
    if x > 10.0:
        res.append(x)
print(sorted(res))
