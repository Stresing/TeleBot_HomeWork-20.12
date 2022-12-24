def like():
    with open("rating.txt", 'r+', encoding='utf-8') as f:
        text = f.read()
        lines = text.split('\n')
        lines[0] = str(int(lines[0]) + 1)
        open('rating.txt', 'w', encoding='utf-8').close()
        f.seek(0)
        f.write('\n'.join(lines))



def dislike():
    with open("rating.txt", 'r+', encoding='utf-8') as f:
        text = f.read()
        lines = text.split('\n')
        lines[1] = str(int(lines[1]) + 1)
        open('rating.txt', 'w', encoding='utf-8').close()
        f.seek(0)
        f.write('\n'.join(lines))
