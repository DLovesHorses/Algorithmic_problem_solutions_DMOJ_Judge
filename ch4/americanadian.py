text = input()

while(text != 'quit!'):
    if not text[-3] in 'aeiouy':
        if text[-2:] == 'or':
            text = text[:-2] + 'our'

    print(text)
    text = input()