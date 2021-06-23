import pyjokes as pj
print('impoerted')

joke1 = pj.get_joke()
print(joke1)
joke2 = pj.get_jokes(language = 'en',category = 'neutral')
#print(joke2)

for i in range(5):
    print(i+1,".",joke2[i])