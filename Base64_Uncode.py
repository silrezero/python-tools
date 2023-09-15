import base64
import os

'''定义控制要处理的文件
file_path="C:\\Users\\ma\\Desktop\\py\\"    #文件存放路径
raw_file_name="1.png"                       #文件名
Processed_file_name="1.txt"                   #处理后文件名
'''

'''
对文件进行base64编码
'''


def encode_file():
    # with open(FILE, "rb") as file:  # 读文件
    #     file_read = file.read()
    # with open(PROCESSED_FILE_NAME, "wb") as encode_file:  # 写入文件
    #     encode_file.write(base64.b64encode(file_read))
    #     print("编码完成！")
    print("请输入编码数据：")
    code = str(input())
    uncode = base64.b64encode(code.encode("utf-8")).decode("utf-8")
    print("编码后为：" + uncode)

'''
对文件进行base64解码
'''


def decode_file():
    # with open(FILE, "rb") as file:  # 读文件
    #     file_read = file.read()
    # with open(PROCESSED_FILE_NAME, "wb") as decode_file:  # 写入文件
    #     decode_file.write(base64.b64decode(file_read))
    #     print("解码完成！")
    print("请输入解码数据：")
    code = input()
    uncode = str(base64.b64decode(code))
    print("解码后为：" + uncode)



if __name__ == "__main__":
    # 输入定义要处理的文件
    # file_path = input("请拖入文件：")  # 拖入要处理的文件
    # FILE_PATH = os.path.split(file_path)[0]  # 取文件所在的路径
    # processed_file_name = input("请输入保存文件名：")
    # PROCESSED_FILE_NAME = FILE_PATH + "\\" + processed_file_name  # 处理后文件与原文件放在同一目录

    while 1:
        A = input("选择处理方式：编码(1)，解码(2): ")
        print("\r")
        if A == "1":
            # encode_file(file_path)
            encode_file()
            break
        elif A == "2":
            # decode_file(file_path)
            decode_file()
            break
        else:
            print("请选择正确的处理方式。")