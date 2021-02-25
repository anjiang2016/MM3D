import numpy as np
import pptk
import pdb


# 生成颜色矩阵
def create_color(num,color):
    ca=color 
    for i in range(num-1):
        ca = np.concatenate((ca,color),axis=0)
    #print(ca.shape)
    return ca        

# 给定viewer和点的数量
def set_color(v,num):
    color_point=np.array([[0.0,1.0,0.0]])
    color=create_color(num,color_point) 
    v.attributes(color)
    v.set(point_size=0.01)    

def show(pc):
    num = pc.shape[0]
    #print(num)
    v=pptk.viewer(pc)
    set_color(v,num)

if __name__=="__main__":
    num=10
    pc=np.random.rand(num,3)
    print(pc.shape)
    #color=np.random.rand(num,3)
    #print(color.shape)
    #v=pptk.viewer(pc)
    #set_color(v,num)
    #v.set(point_size=0.1)
    #v.attributes(color)
    show(np.random.rand(100,3))
