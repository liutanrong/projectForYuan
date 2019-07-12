def change_line_format(origin_line):
    """
    将一行字符串格式进行转换
    注意中间是\t tab键进行分割而非空格
    :param origin_line: 2017	01	2	0	13	6	300	-36.0365	51.9288	5.7	10
    :return:
    ${year},${mo},${dy},${hr}${mn}${sec}.${msec},${lat},${lon},${m},${dep}
    2017,01,2,0136.300,-36.0365,51.9288,5.7,10
    """
    line_arr = origin_line.strip("\n").split('\t')
    dest_line = '%s,%s,%s,%s%s%s.%s,%s,%s,%s,%s'
    if len(line_arr) is 11:
        dest_line = dest_line % (line_arr[0], line_arr[1],
                                 line_arr[2], line_arr[3], line_arr[4],
                                 line_arr[5], line_arr[6], line_arr[7],
                                 line_arr[8], line_arr[9], line_arr[10])
    return dest_line


if __name__ == '__main__':
    """
    将sc-catalog-tel.txt文本内每一行进行格式转换并输出至sc-sks.txt文件内
    """

    file = open('sc-catalog-tel.txt', "r")
    out_file = open('sc-sks.txt', "w")

    while 1:
        line = file.readline()
        if not line:
            break
        pass
        changed_line = change_line_format(line)
        out_file.write(changed_line)
        out_file.write("\n")

    file.close()
    out_file.close()
