#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
const int maxn = 210;
const double eps = 1e-12;    //精度要求高一点

int n,m;    //n是总点数，m是凸包中平面的数量
bool g[maxn][maxn];    //g用来判断一条边被照到几次

double rand_eps()    //用rand函数来生成一个非常小的随机数
{
    return ((double)rand() / RAND_MAX - 0.5) * eps;    //用rand生成一个-0.5到0.5之间的数，再乘eps，就得到了一个非常小的随机数
}

struct Point{    //定义点的结构体
    double x,y,z;    //xyz三个坐标
    void shake()    //微小扰动，给每个坐标都加一个极小的随机数
    {
        x += rand_eps(), y += rand_eps(), z += rand_eps();
    }
    Point operator-(Point t)    //重载一下减号运算符
    {
        return {x-t.x, y-t.y, z-t.z};
    }
    Point operator*(Point t)    //叉乘
    {
        return {y*t.z - t.y*z, t.x*z - x*t.z, x*t.y - y*t.x};
    }
    double operator&(Point t)    //点积
    {
        return x*t.x + y*t.y + z*t.z;
    }
    double len()        //求向量的模长，三个坐标也能存向量
    {
        return sqrt(x*x + y*y + z*z);
    }
}p[maxn];    //p来存所有点

struct Plane{    //定义平面的结构体
    int v[3];    //三个顶点
    Point norm()    //求法向量
    {
        return (p[v[1]] - p[v[0]]) * (p[v[2]] - p[v[0]]);    //平面中两向量的叉积
    }
    bool above(Point t )    //判断一个点是否在平面上方
    {
        return ((t-p[v[0]]) & norm()) >= 0;    //用向量和法向量的点积判断
    }
    double area()        //求一平面的面积
    {
        return norm().len() / 2;    //法向量的模长除以2
    }
}plane[maxn],tp[maxn];    //plane存凸包上的平面，tp用来更新凸包，每次凸包上要留的平面和新加的平面都存进tp，要删的平面不存，最后将tp在复制给plane，就实现了凸包的更新

void convex()
{
    plane[m++] = {0,1,2};    //初始化凸包，随便三个点存入，确定最开始的一个平面，这里取得是前三个点
    plane[m++] = {2,1,0};    //因为不知道第一个平面怎么样是逆时针，所以都存一遍，顺时针存的一会会被删掉
    for(int i = 3;i < n;i++)    //从第四个点开始循环每个点
    {
        int cnt = 0;
        for(int j = 0;j < m;j++)    //循环每个平面
        {
            bool fg = plane[j].above(p[i]);    //判断这个点是否在该平面上方
            if(!fg)        //如果是下方的话，说明照不到
                tp[cnt++] = plane[j];    //存进tp数组
            for(int k = 0;k < 3;k++)    //循环该平面的三条边
                g[plane[j].v[k]][plane[j].v[(k+1)%3]] = fg;    //ab边照不照得到情况赋值给g[a][b]
        }
        for(int j = 0;j < m;j++)    //然后就循环每个平面的每条边
        {
            for(int k = 0;k < 3;k++)
            {
                int a = plane[j].v[k],b = plane[j].v[(k+1)%3];
                if(g[a][b] && !g[b][a])        //判断该边是否被照到了一次，即是否是交界线的边
                    tp[cnt++] = {a,b,i};    //若是，加新平面abi，ab一定是逆时针的，i在后面
            }
        }
        m = cnt;    //将tp再赋值给plane
        for(int j = 0;j < m;j++)
            plane[j] = tp[j];
    }
}

int main()
{
    cin >> n;
    for(int i = 0;i < n;i++)
    {
        cin >> p[i].x >> p[i].y >> p[i].z;    //输入n个点
        p[i].shake();    //微小扰动
    }

    convex();    //求三维凸包

    double ans = 0;        //求面积和
    for(int i = 0;i < m;i++)    //循环最终凸包上的m个平面
        ans += plane[i].area();    //将平面的面积加和
    printf("%.6lf\n",ans);    //输出答案

    return 0;
}
