import numpy as np


class SuperCos():

    @staticmethod
    def one_hot(strs, chars):
        char_size = len(chars)
        vec = [0] * char_size
        for char in str(strs):
            index = chars.index(char)
            vec[index] = 1
        return np.array(vec)

    def cos(self,strlist1,strlist2):
        strlist = strlist1+strlist2
        chars = list(set(''.join(strlist)))
        matrix1 = np.matrix([self.one_hot(i,chars) for i in strlist1])
        matrix2 = np.matrix([self.one_hot(i,chars) for i in strlist2])
        vecdot = matrix1.dot(matrix2.T)
        veclength1 = np.sqrt(matrix1.sum(axis=1))
        veclength2 = np.sqrt(matrix2.sum(axis=1))
        lengthdot = veclength1.dot(veclength2.T)
        cos_matrix = np.divide(vecdot,lengthdot)
        return cos_matrix

    def issim(self,strlist1,strlist2,threshold = 0.6):
        cos_matrix = self.cos(strlist1, strlist2)
        max_cos = cos_matrix.max(axis=1)
        l = len(max_cos)
        normal = [strlist1[i] for i in range(l) if max_cos[i] > threshold]
        return normal

    def unsim(self,strlist1,strlist2,threshold=0.3):
        cos_matrix = self.cos(strlist1,strlist2)
        max_cos = cos_matrix.max(axis=1)
        print(strlist1[max_cos>threshold])
        l = len(max_cos)
        abnormal = [strlist1[i] for i in range(l) if max_cos[i] < threshold]
        return abnormal


cos_sim = SuperCos()

if __name__ =='__main__':
    a = ['有没有']
    b = ['我没有啊','有测试','有妖气']
    import time
    sc = SuperCos()
    s = time.time()
    cos = sc.cos(a,b)
    print(cos)
    e = time.time()
    print(e-s)
    # ab = sc.issim(a,b)








