import wikipedia

def article(title):
    result = wikipedia.summary(title)
    return result
def write(filename, data):
    filename = 'EP.last_summary\wiki\countries\{}.txt'.format(filename)
    with open (filename, 'w', encoding='utf-8') as file:
        file.write(data)

wikipedia.set_lang('th')

with open('EP.last_summary\wiki\search-word.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

word = []
for l in lines:
    word.append(l.strip())

print(word)

for w in word:
    data = article(w)
    write(w, data)

