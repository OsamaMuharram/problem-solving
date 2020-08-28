from collections import Counter ,OrderedDict
x=list(input())
x.sort()
cnt = Counter()
for word in x:
    cnt[word] += 1
    x=sorted(cnt.items())
    y = OrderedDict(cnt.most_common(3))
for chr, count in y.items():
    print(chr,  count)


