import os
import chardet

def find_all_file(path):
    for root,dirs,files in os.walk(path):
        for f in files:
            fullname = os.path.join(root,f)
            yield fullname
            pass
    pass

def judge_coding(path):
    with open(path,'rb') as f:
        c = chardet.detect(f.read())
    if c != 'utf-8':
        return c

def change_to_utf_file(path):
    for i in find_all_file(path):
        c = judge_coding(i)
        if c:
            change(i,c['encoding'])

def change(path,coding):
    with open(path,'r',encoding=coding) as f:
        text = f.read()
    with open(path,'w',encoding='utf-8')as f:
        f.write(text)

def main():
    my_path = ''
    change_to_utf_file(my_path)

if __name__ == '__main__':
    main()

