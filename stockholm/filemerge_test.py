ad_book1 = {}
ad_book2 = {}

def read_ad():
    file1 = open('address1.txt', 'r')
    lines1 = file1.readlines()

    for line in lines1:
        line = line.strip()
        content = line.split(',')
        ad_book1[content[0]]=content[1]

    file1.close()

    with open('address2.txt', 'r') as file2:
        lines2 = file2.readlines()
        for line in lines2:
            line = line.strip()
            content = line.split(',')
            ad_book2[content[0]] = content[1]

def merge_ad():

    lines = []
    header = '姓名\t     电话\t       邮箱'
    lines.append(header)

    for key in ad_book1:
        line = ''
        if key in ad_book2.keys():
            line = line + '\t'.join([key, ad_book1[key], ad_book2[key]])
        else:
            line = line + '\t'.join([key, ad_book1[key], '**************'])
        line = line + '\n'
        lines.append(line)

    for key in ad_book2:
        line = ''
        if key not in ad_book1.keys():
            line = line + '\t'.join([key, '**************', ad_book2[key]])
            line = line + '\n'
            lines.append(line)

    with open('new_address.txt', 'w') as newfile:
        newfile.writelines(lines)


#if __name__ == '__main__':
read_ad()
merge_ad()