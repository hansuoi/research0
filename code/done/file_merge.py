while True:
    print('file type (txt or csv) = ', end='')
    file_type = input()

    if file_type=='txt' or file_type=='csv':
        break


print('path of first file  = ', end='')
f_file = input()

print('path of latter file = ', end='')
l_file = input()

print('path of result file = ', end='')
r_file = input()



if file_type == 'txt':
    # 開く
    with open(f_file, 'r', encoding='utf-8') as f:
        first  = f.readlines()
    with open(l_file, 'r', encoding='utf-8') as f:
        latter = f.readlines()

    # 一応全部の行末に改行付けとく
    for file in [first, latter]:
        for i in range(len(file)):
            if file[i][len(file[i])-1] != '\n':
                file[i] += '\n'

    # 書き込む
    with open(r_file, 'w', encoding='utf-8') as f:
        f.writelines(first)
        f.writelines(latter)


else:    # if file_type == 'csv':
    import csv

    # 開く ここから
    with open(f_file, 'r', encoding='utf-8') as f1:
        with open(l_file, 'r', encoding='utf-8') as f2:
            first  = csv.reader(f1, delimiter=',')
            latter = csv.reader(f2, delimiter=',')
            # 開く ここまで

            # 以下、書き込み
            with open(r_file, 'w', encoding='utf-8', newline='') as f3:
                writer = csv.writer(f3)
                for f in first:
                    writer.writerow(f)
                for l in latter:
                    writer.writerow(l)
