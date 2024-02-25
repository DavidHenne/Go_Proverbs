import json

def chunked(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    data = {"proverbs": []}
    txt_file = open("../data/proverbs.txt", "r")
    key = 1
    for l in chunked(txt_file.readlines(), 2):
        data["proverbs"].append({"author": l[1].rstrip(),
                                 "text": l[0].rstrip(),
                                 "key": key})
        key += 1
    txt_file.close()

    with open('../data/proverbs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
