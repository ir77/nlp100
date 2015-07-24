# coding: UTF-8

raw = u"パタトクカシーー"
raw2 = u""
for i, str in enumerate(raw):
    if i % 2 == 0:
        raw2 += str
print raw2
