from pptk_show import * 


# 生成一些随机点
#pointcloud=np.random.rand(10,3)


def get_vertex(xyz,theta,dim):
    print(dim.shape)
    w=dim[0,0]
    h=dim[0,1]
    l=dim[0,2]
    vertex=np.zeros([8,4])
    vertex[0,:]=np.array([0.5*w,0.5*h,0.5*l,1])
    vertex[1,:]=np.array([-0.5*w,0.5*h,0.5*l,1])
    vertex[2,:]=np.array([-0.5*w,-0.5*h,0.5*l,1])
    vertex[3,:]=np.array([0.5*w,-0.5*h,0.5*l,1])

    vertex[4,:]=np.array([0.5*w,0.5*h,-0.5*l,1])
    vertex[5,:]=np.array([-0.5*w,0.5*h,-0.5*l,1])
    vertex[6,:]=np.array([-0.5*w,-0.5*h,-0.5*l,1])
    vertex[7,:]=np.array([0.5*w,-0.5*h,-0.5*l,1])
    
    #  旋转,平移
    rt_matrix=np.array([
              [np.cos(theta),0,np.sin(theta),xyz[0,0]],
              [0,1,0,xyz[0,1]],
              [-np.sin(theta),0,np.cos(theta),xyz[0,2]],
             ])
    vertex_new=np.dot(vertex,rt_matrix.T)
    

    return vertex_new
 
# 生成一条边
def get_line_point(p1,p2):
    #pc = np.concatenate([[p1],[p2]],axis=0)
    num=max(abs(p2-p1)/0.01)
   
    num=int(num)
    pc=np.zeros([num,3])
    x = np.array(np.linspace(p1[0],p2[0],num))   
    y = np.array(np.linspace(p1[1],p2[1],num))    
    z = np.array(np.linspace(p1[2],p2[2],num))    
    dx=p2[0]-p1[0] 
    dy=p2[1]-p1[1]
    dz=p2[2]-p1[2]
    num=num-1
    for i in range(x.shape[0]): 
        x[i]= p1[0] + i*dx/float(num)
        y[i]= p1[1] + i*dy/float(num)
        z[i]= p1[2] + i*dz/float(num)
        #pc=np.concatenate([pc,np.array([[x[i],y[i],z[i]]])])      
        pc[i,:]=np.array([[x[i],y[i],z[i]]])      
    #print(pc.shape)
    #print(pc)
    return pc
          
        
  

        


# 生成一个3dbox

def get_3dbox_cloud(xyz,theta,dim):
    vertex= get_vertex(xyz,theta,dim)
    pc = vertex
    #1
    line_pc=get_line_point(vertex[0],vertex[1])
    pc = np.concatenate([pc,line_pc],axis=0)
    #2
    line_pc=get_line_point(vertex[2],vertex[1])
    pc = np.concatenate([pc,line_pc],axis=0)
    ##3
    line_pc=get_line_point(vertex[2],vertex[3])
    pc = np.concatenate([pc,line_pc],axis=0)
    ##4
    line_pc=get_line_point(vertex[0],vertex[3])
    pc = np.concatenate([pc,line_pc],axis=0)
    #
    #1
    line_pc=get_line_point(vertex[4+0],vertex[4+1])
    pc = np.concatenate([pc,line_pc],axis=0)
    ##2
    line_pc=get_line_point(vertex[4+2],vertex[4+1])
    pc = np.concatenate([pc,line_pc],axis=0)
    ##3
    line_pc=get_line_point(vertex[4+2],vertex[4+3])
    pc = np.concatenate([pc,line_pc],axis=0)
    ##4
    line_pc=get_line_point(vertex[4+0],vertex[4+3])
    pc = np.concatenate([pc,line_pc],axis=0)
    #
    ##1
    line_pc=get_line_point(vertex[0],vertex[4+0])
    pc = np.concatenate([pc,line_pc],axis=0)
    ##1
    line_pc=get_line_point(vertex[1],vertex[4+1])
    pc = np.concatenate([pc,line_pc],axis=0)
    ##1
    line_pc=get_line_point(vertex[2],vertex[4+2])
    pc = np.concatenate([pc,line_pc],axis=0)
    #1
    line_pc=get_line_point(vertex[3],vertex[4+3])
    pc = np.concatenate([pc,line_pc],axis=0)
    return pc 



if __name__=="__main__":
    xyz=np.random.rand(1,3)
    theta=np.random.rand(1,1)*np.pi/2
    dim=np.random.rand(1,3)
    print(xyz)
    print(theta)
    print(dim)
    pc1 = get_3dbox_cloud(xyz,theta,dim)
    #pc2 = get_3dbox_cloud(np.array([[0,0,0]]),np.array([[0]]),np.array([[1.0,1.0,1.0]]))
    #pc = np.concatenate([pc1,pc2],axis=0)
    #print(pc)
    print(pc1.shape)
    # 显示pc1
    show(pc1)
