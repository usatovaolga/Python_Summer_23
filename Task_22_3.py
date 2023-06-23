import keyword
import re
tt=keyword.kwlist
#s=input()
s = 'break del текст else True continue текст'
for i in range(len(tt)):
    s = s.replace(tt[i], '<kw>')
print(s)