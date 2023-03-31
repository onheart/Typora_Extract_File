# 提取单个markdown文件
import os
import shutil


def create_new_file(md_path):
    '''
    创建新文件夹
    '''
    img_path = md_path[:-3] + '/assets/'
    file_path = md_path[:-3]
    os.makedirs(img_path, mode=0o777)
    return [file_path,img_path]


def move_img(md_path, new_img_path):
    '''
    移动图片
    '''
    with open(md_path, 'r', encoding='utf-8') as file:
        md_lines = file.readlines()
    for md_line in md_lines:
        relative_img_path = ''
        file_name = ''
        if '![image-' in md_line and '](' in md_line and ')' in md_line:
            relative_img_path = md_line.split('](')[1].split(')')[0]
            n = relative_img_path.rfind('/')
            file_name = relative_img_path[n + 1:]
        else:
            continue
        front_path = md_path[:md_path.rfind('\\')+1]
        while relative_img_path.startswith('..'):
            front_path = find_last_path(front_path)
            relative_img_path = relative_img_path[relative_img_path.find('./') + 2:]
        img_path = front_path + relative_img_path
        shutil.copy2(img_path, new_img_path)

def move_md(md_path, file_path):
    '''
    移动markdown文件
    '''
    shutil.copy2(md_path, file_path)

def modify_md(md_path):
    '''
    当图片存在非同文件夹下的assets时修改图片路径
    '''
    with open(md_path, 'r+', encoding='utf-8') as file:
        md_lines = file.readlines()
    for md_line in md_lines:
        relative_img_path = ''
        file_name = ''
        if '![image-' in md_line and '](' in md_line and ')' in md_line:
            relative_img_path = md_line.split('](')[1].split(')')[0]
            n = relative_img_path.rfind('/')
            file_name = relative_img_path[n + 1:]
            new_line = f'![{file_name}](assets/{file_name})'
            file.write(new_line)
        else:
            continue

def find_last_path(path):
    '''
    寻找上一级路径
    '''
    n = path.rfind("\\")
    return path[:n + 1]


if __name__ == '__main__':
    md_path = input('输入要提取的markdown文件目录:')
    new_path = create_new_file(md_path)
    move_img(md_path, new_path[1])
    move_md(md_path, new_path[0])
    print('success')
