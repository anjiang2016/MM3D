#coding:utf-8
# 创建GUI窗口打开图像 并显示在窗口中

from PIL import Image, ImageTk # 导入图像处理函数库
import tkinter as tk           # 导入GUI界面函数库
from cloud2img import *
# 绑定鼠标左键事件，交由processMouseEvent函数去处理，事件对象会作为参数传递给该函数
# canvas.bind(sequence="<Button-1>", func=self.processMouseEvent)

# 创建窗口 设定大小并命名
window = tk.Tk()
window.title('明明老师点云显示软件')
window.geometry('800x800')
global img_png           # 定义全局变量 图像的
var = tk.StringVar()    # 这时文字变量储存器
global img_cloud
global theta
theta=0
global point
# 生成一个标准立方体的点云
point = get_3dbox_cloud(np.array([[0,0,0]]),np.array([[0]]),np.array([[1.0,1.0,1.0]]))
Img = Image.open('./tank.png')
img_cloud = ImageTk.PhotoImage(Img)

global last_me_x,last_me_y,first_set
last_me_x=0
last_me_y=0
first_set=False

# 创建打开图像和显示图像函数
def Open_Img():
    global img_png
    var.set('已打开')
    Img = Image.open('./tank.png')
    img_png = ImageTk.PhotoImage(Img)

def Show_Img():
    global img_png
    var.set('已显示')   # 设置标签的文字为 'you hit me'
    label_Img = tk.Label(window, image=img_png)
    label_Img.pack()

def create_show_pointcloud():
     global img_cloud,theta,point
     # 生成点云
     #point = get_3dbox_cloud(np.array([[0,0,0]]),np.array([[0]]),np.array([[1.0,1.0,1.0]]))
     # 点云投影成图片
     # 点云，旋转角度，平移量
     #theta=np.float(sys.argv[1])
     # 调用point2img将点云旋转平移然后生成Image类型的图片
     img=point2img(point,np.array([[theta]]),np.array([[0.0,0.0,1.0]]),30.0) 
     var.set('已显示点云，旋转角度为%s'%(theta))   
     img_cloud=ImageTk.PhotoImage(img)
    
     #imgvar=img_cloud
     #imgvar=ImageTk.PhotoImage(img)
     Label_Img['image'] =img_cloud 
def right_rotate_pointcloud():
     global img_cloud,theta,point
     theta=theta+0.1
     img=point2img(point,np.array([[theta]]),np.array([[0.0,0.0,1.0]]),30.0) 
     var.set('旋转角度%s'%(theta)) 
     img_cloud=ImageTk.PhotoImage(img)
     Label_Img['image'] =img_cloud 
def left_rotate_pointcloud():
     global img_cloud,theta,point
     theta=theta-0.1
     img=point2img(point,np.array([[theta]]),np.array([[0.0,0.0,1.0]]),30.0) 
     var.set('旋转角度%s'%(theta)) 
     img_cloud=ImageTk.PhotoImage(img)
     Label_Img['image'] =img_cloud 
def rotate_pointcloud(theta_delta):
     global img_cloud,theta,point
     theta=theta+theta_delta
     img=point2img(point,np.array([[theta]]),np.array([[0.0,0.0,1.0]]),30.0) 
     var.set('旋转角度%s'%(theta)) 
     img_cloud=ImageTk.PhotoImage(img)
     Label_Img['image'] =img_cloud 
     
def processBREvent(me):
    global last_me_x,last_me_y,first_set
    first_set=False
    print("鼠标左键释放了")
def processMouseEvent(me):
    global last_me_x,last_me_y,first_set
    print("me=",type(me))
    print("mouse")
    print("位于屏幕", me.x_root, me.y_root)
    print("位于窗口", me.x, me.y)
    print("位于窗口", me.num)


    if first_set is True:
        diff_x=me.x-last_me_x
        diff_y=me.y-last_me_y
        print("diff:%s,%s"%(diff_x,diff_y))
        theta_delta=-np.float(diff_x)/500
        rotate_pointcloud(theta_delta)
    last_me_x=me.x
    last_me_y=me.y
    if first_set is False:
        first_set=True



    #me 处理鼠标事件，ke为控件传递过来的键盘事件对象

def processKeyboardEvent(ke):
    print("ke.keysym", ke.keysym)  # 按键别名
    print("ke.char", ke.char)  # 按键对应的字符
    print("ke.keycode", ke.keycode)  # 按键的唯一代码，用于判断按下的是哪个键</class></key></button-1>
    
# 创建文本窗口，显示当前操作状态,# 使用 textvariable 替换 text, 因为这个可以变化
Label_Show = tk.Label(window,textvariable=var, bg='white', font=('Arial', 12), width=100, height=2)
Label_Show.pack()

# 创建打开图像按钮
btn_Open = tk.Button(window,
    text='打开图像',      # 显示在按钮上的文字
    width=15, height=2,
    command=Open_Img)     # 点击按钮式执行的命令
btn_Open.pack()    # 按钮位置

# 创建显示图像按钮
btn_Show = tk.Button(window,
    text='显示图像',      # 显示在按钮上的文字
    width=15, height=2,
    command=Show_Img)     # 点击按钮式执行的命令
btn_Show.pack()    # 按钮位置

# 创建按钮:实现3d点云的生成与显示
btn_cspoint = tk.Button(window,
    text='生成点云并显示',      # 显示在按钮上的文字
    width=15, height=2,
    command=create_show_pointcloud)     # 点击按钮式执行的命令
btn_cspoint.pack()    # 按钮位置

# 创建按钮：实现3d点云的旋转
btn_rotate_left = tk.Button(window,text="右旋转点云",width=15,height=2,command=left_rotate_pointcloud)
btn_rotate_left.pack()
# 创建按钮：实现3d点云的旋转
btn_rotate_right = tk.Button(window,text="左旋转点云",width=15,height=2,command=right_rotate_pointcloud)
btn_rotate_right.pack()

# 创建图片显示窗口，显示当前图片
# 使用 全局变量img_cloud来给Label_Img提供数据
# 通过改变img_cloud的值，来改变Label_Img显示的图片
Label_Img = tk.Label(window,image=img_cloud)
Label_Img.pack()
# 绑定鼠标左键事件，交由processMouseEvent函数去处理，事件对象会作为参数传递给该函数
# 鼠标单击中
#https://www.cnblogs.com/anita-harbour/p/9449757.html
#Label_Img.bind(sequence="<Button-1>", func=processMouseEvent)
Label_Img.focus_set()
Label_Img.bind(sequence="<Key>", func=processKeyboardEvent)
Label_Img.bind(sequence="<B1-Motion>", func=processMouseEvent)
Label_Img.bind(sequence="<ButtonRelease-1>", func=processBREvent)

# 运行整体窗口
window.mainloop()
