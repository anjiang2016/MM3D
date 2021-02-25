# coding:utf-8
import sys
from box2cloud import *
from PIL import Image, ImageTk # 导入图像处理函数库
pc2 = get_3dbox_cloud(np.array([[0,0,0]]),np.array([[0]]),np.array([[1.0,1.0,1.0]]))
print(pc2.shape)

print(np.ones([pc2.shape[0],1]).shape)
pc2 = np.concatenate([pc2,np.ones([pc2.shape[0],1])],axis=1)
print(pc2.shape)


def roat_tans(point,theta,xyz,times):
    #  旋转,平移
    rt_matrix=np.array([
              [np.cos(theta),0,np.sin(theta),xyz[0,0]],
              [0,1,0,xyz[0,1]],
              [-np.sin(theta),0,np.cos(theta),xyz[0,2]],
             ])
    #point_new=np.dot(point,rt_matrix.T)
    point_new=np.dot(rt_matrix,point.T)
    print("point_new's shape:")
    print(point_new.shape)
    
    # 相机内参
    fx = 4137.8
    fy = 4147.3
    u0=4256/2
    v0=2832/2 
    intMatrix=np.array([
                  [fx/times,0,u0],  
                  [0,fy/times,v0],  
                  [0,0,1],  
                ]) 
    #向平面映射        
    uv=np.dot(intMatrix,point_new) 
    Z = uv[2:3,:] 
    uv = uv/np.concatenate([Z,Z,Z],axis=0)
    print(uv.shape)


    return uv


def uv2image(uv):
    #import pdb
    #pdb.set_trace()
    # 成像平面大小
    u=4256
    v=2832 
    # 从uv中拿到x,y坐标,坐标是整形的
    x=(uv[0,:]).astype(int)
    y=(uv[1,:]).astype(int)
    
    # 超过边界的点去掉
    door=(x<4256)*(x>-1)*(y<2832)*(y>-1)
    xs=x[door]
    ys=y[door]
      
    print("xs'shape:")
    print(xs.shape)
    
    img=np.zeros([v,u])
    print("img's shape")
    print(img.shape)
    #img[[0,1],[0,2]]=1
    img[ys,xs]=255
    return img

def point2img(point,theta,xyz,times):
    point = np.concatenate([point,np.ones([point.shape[0],1])],axis=1)
    uv=roat_tans(point,theta,xyz,times)
    img=uv2image(uv)
    p = Image.fromarray(np.uint8(img));
    return p 
    
if __name__=="__main__":
    # 获取点云
    point = get_3dbox_cloud(np.array([[0,0,0]]),np.array([[0]]),np.array([[1.0,1.0,1.0]]))
    # 点云投影成图片
    # 点云，旋转角度，平移量
    theta=np.float(sys.argv[1])
    p=point2img(point,np.array([[theta]]),np.array([[0.0,0.0,1.0]]),30.0)
    p.save("./p.png");
        
