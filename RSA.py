#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-08-09 13:58:03
# @Author  : gong_jian
# @Email   : gong_jian@inspur.com
# @Version : $Id$
# 导入pycryptodome模块
from Crypto.PublicKey import RSA as rsa
from Crypto.Cipher import PKCS1_OAEP
import base64


# 加密
def encrypt(text):
    with open('public_key.txt') as f:
        # 拼接公钥前后缀
        key = '-----BEGIN RSA PUBLIC KEY-----\n' + str(f.read()) + '\n-----END RSA PUBLIC KEY-----'
        # 加载公钥
        pukey = rsa.importKey(key)
    # 构建加密器1
    encryptor = PKCS1_OAEP.new(pukey)
    encresult = encryptor.encrypt(text)
    # print(encresult)
    encresult = base64.b64encode(encresult).decode()
    return encresult

# 解密
def decrypt(text):
    with open('private_key.txt') as f:
        key = '-----BEGIN RSA PRIVATE KEY-----\n' + str(f.read()) + '\n-----END RSA PRIVATE KEY-----'
        prkey = rsa.import_key(key)
    decryptor = PKCS1_OAEP.new(prkey)
    decresult = decryptor.decrypt(base64.b64decode(text)).decode()
    return decresult

def main():
    while True:
        mode = input("1加密解密，2解密：")
        if mode == '1':
            # 加、解密
            text = input("输入需要加密的文本：").encode()
            enc = encrypt(text)
            print(enc)
            dec = decrypt(enc)
            print(dec)
        else:
            # 解密
            ciphertext = input("输入需要解密的密文：")
            dec = decrypt(ciphertext)
            print(dec)

if __name__ == '__main__':
    main()
