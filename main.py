import sys
import re

way = '../../output_file.txt'


def get_summary_rss(str_way):
    with open(str_way, 'r', encoding='UTF8') as f:
        rss = 0
        for i in f.readlines()[1:]:
            rss += int(i.split()[5])
        return round(rss / 1048576, 1)


def get_main_size(ls_output):
    sum_size_file = 0
    count = 0
    for line in ls_output:
        count += 1
        sum_size_file += int(line.split()[4])
    return round(sum_size_file / count / 1024, 2)


def decrypt(line):
    pat = '\S\.{2}'
    while re.search(pat, line):
        line = re.sub(pat, '', line)
        if line == '':
            return 'Note is empty'
    line = line.split('.')
    return ''.join(line)


def main():
    #print(get_summary_rss(sys.stdin.read()))
    '''
    data = sys.stdin.readlines()[1:]
    if not data:
        print('There is no data')
    else:
        print(f"Average file size: {get_main_size(data)} KiB")
    '''
   # print(decrypt(sys.stdin.read()))


if name == "main":
    main()
