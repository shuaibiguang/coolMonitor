1.0 
由于时间太赶没将html做入django内

htnl->ajax（请求接口）->django（处理请求）->caiji

caiji->django->ajax->web(展示)

/html下放置的是html静态的代码
  核心的js在index.html里面

/jiankong 下面放的是django的代码，jiankong/opsapp/views.py  核心代码
  请求被监控的服务器的服务端，发送指令，收集采集端的信息，并作处理，返回值给ajax

/caiji  下面放的是需要部署在采集端的python文件，调用了psutil模块，在部署前需要先安装此模块
  接受django传过来的指令，根据指令收集当前服务器的信息

占用端口情况

nginx 端口 80

django 端口 8000

采集端端口 8001

前端使用开源后台模板AdminLTE-2.3.7

python2.7 and python3.5  均可运行
