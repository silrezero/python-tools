import urllib.parse

def Standard_symbols():   # url标准符号编码
    print("请输入url:")
    base_url = input()
    # data = [('email', '北京1234@qq.com'), ('password', 'bj12345')]
    d1 = urllib.parse.quote(base_url)
    print("编码后的url为：\r" + d1)


if __name__ == "__main__":

    while 1:
        A = input("选择处理方式：标准符号编码(1)，转化为%xx形式(2): ")
        print("\r")
        if A == "1":
            # encode_file(file_path)
            Standard_symbols()
            break
        elif A == "2":
            # decode_file(file_path)
            break
        else:
            print("请选择正确的处理方式。")