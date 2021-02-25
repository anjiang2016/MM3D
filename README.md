# MM3D
从零开始写一个3d点云的显示软件，从此以后，3d显示不求人。

## 点云定义
- 三维直接中的点在数学中用(x,y,z)三个坐标来表示，
- N个点组成的Nx3的矩阵，就是点云。
- 无论是什么格式的点云数据，本质就是Nx3的矩阵。我们就是通过这个Nx3的矩阵来把立体的物体显示出来
-
## 生成点云
- box2cloud.py
- 给定一个3dbox的中心点，旋转角度，长，宽，高，生成这个3dbox的点云

## 显示理论
- 世界坐标系到像素坐标系到转换过程

## 点云映射为图片
- cloud2img.py
- 按照世界坐标系到像素坐标系的对应关系，我们准备好相机参数矩阵A，旋转平移矩阵H，假设3d点云为P 
- 则：AxHxP，然后再归一化，就是像素坐标系的坐标uv了
- 得到坐标后，把坐标转换为img,即，使img[uv[0],uv[1]]=color[uv[0],uv[1]就行了
- 这个color[uv[0],uv[1]]可以是255，就是黑白图的意思
- 这个color也可以是[R,G,B]表示颜色。这时候显示的点云就是彩色点云了
## 辅助开发用的显示用的软件
- pptk_show.py

## 用按钮来控制点云的旋转
- mmteacher_3d_display_button.py
- 这里主要涉及到用按钮来控制旋转角度，从而方便操作点云旋转
## 用鼠标来控制点云的旋转
- mmteacher_3d_display_mouse.py
- 这里主要涉及到用鼠标来控制旋转角度，从而方便操作点云旋转，这种操作方式更加高效

## 当前进度和后续开发计划
    - 完成了不带颜色的点云转化为图片的过程，后续把颜色加上
    - 当前例子很少，只用了一个标准的立方体，后续后给一些特殊的点云，比如人脸的，或者某个物体的
    - 后面还想实现一下3d人脸的3维显示，并且做到3d人脸会跟随摄像头中的人。
    - 当前实现了点云的显示，绕y轴的旋转，后续会实现绕x,z轴的旋转，会实现点云的放大缩小
    - 当前还没有把坐标轴绘制出来，后续会把坐标轴绘制出来。


第一版的显示软件：
![image](http://152.136.201.129:8090/fileop/media/img/image_8ZGdwHW.png)

p.png
![image](https://github.com/anjiang2016/MM3D/blob/main/p.png)
