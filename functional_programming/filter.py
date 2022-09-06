# 3 Filter the scores that pass over 50%
def fil(item):
    return item > 50


scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(fil, scores)))
