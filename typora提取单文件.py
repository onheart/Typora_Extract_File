# 提取单个markdown文件
import os


def create_new_file(md_path):
    '''
    创建新文件夹
    '''
    os.makedirs(md_path[:-3] + '/assets')
    return md_path[:-3] + '/assets/'


def move_img(md_path, new_img_path):
    '''
    移动图片
    '''
    with open(md_path, 'r') as file:
        md_lines = file.readlines()
    for md_line in md_lines:
        relative_img_path = ''
        file_name = ''
        if '![image-' in md_line and '](' in md_line and ')' in md_line:
            relative_img_path = md_line.split('](')[1].split(')')[0]
            n = relative_img_path.rfind('/')
            file_name = relative_img_path[n + 1:]
        front_path = md_path[:md_path.rfind('\\')]
        while relative_img_path.startswith('..'):
            front_path = find_last_path(front_path)
            relative_img_path = relative_img_path[relative_img_path.find('./')+2:]
        img_path = front_path + relative_img_path
        # img_file = open(img_path, 'r')
        # new_img_file = open(new_img_path + file_name, 'w')
        os.system('xcopy ' + img_path + ' ' + new_img_path)


def find_last_path(path):
    '''
    寻找上一级路径
    '''
    n = path.rfind("\\")
    return path[:n + 1]


if __name__ == '__main__':
    md_path = input('输入要提取的markdown文件目录:')
    new_img_path = create_new_file(md_path)
    move_img(md_path, new_img_path)
    print('success')
