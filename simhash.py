import jieba.analyse
import math
import numpy as np


class Simhash():

    def __init__(self,hash_length = 64):
        self.hash_length = hash_length

    # 将字符串进行hash
    def strhash(self,rawstr):
        if rawstr == '':
            return 0

        x = ord(rawstr[0])<<7
        m = 256256
        mask = 2**128-1

        for w in rawstr:
            x = ((x*m)^ord(w))&mask
        x ^= len(rawstr)

        if x == -1:
            x = -2

        x = bin(x).replace('0b','').zfill(self.hash_length)[-self.hash_length:]

        return x

    # 将0转为-1
    def transform(self,s):
        if s == "0":
            s = -1
        return int(s)

    # 将字符串进行simhash
    def simhash(self,sentence):
        keywords = jieba.analyse.extract_tags(sentence, withWeight=True)
        init_hash = np.array([0]*self.hash_length)

        for keyword,weight in keywords:
            keyhash = self.strhash(keyword)
            weight = math.ceil(weight)
            keyhash = np.array([self.transform(i)*weight for i in keyhash])
            init_hash = init_hash+keyhash

        sentence_hash = 1*(init_hash>0)
        return sentence_hash

    # 计算汉明距离
    def hamming(self,sentence1,sentence2):
        hash1 = self.simhash(sentence1)
        hash2 = self.simhash(sentence2)
        dist = self.hash_length-sum(1*(hash1==hash2))
        return dist


if __name__ == '__main__':
    simhash = Simhash()
    s1 = '得到指纹以后，就可以对比不同的图片，看看64位中有多少位是不一样的。在理论上，这等同于计算"汉明距离"（Hamming distance）。如果不相同的数据位不超过5'
    s2 = '得到指纹以后，就可以对比不同的图片，看看64位中有多少位是不一样的。在理论上，这等同于计算'
    s3 = '得到指纹以后，就可以对比不同的图片，看看64位中有多少位是不一样的'
    print(simhash.hamming(s1,s2))
    print(simhash.hamming(s1,s3))
    print(simhash.hamming(s2,s3))
