import pymysql

pymysql.install_as_MySQLdb()
"""
什么是AJAX
Asynchronous Javascript And Xml
　异步的　　　　js         和　Xml(JSON)
异步访问：当客户端向服务器端发送请求时,服务器在处理的过程中,客户端无需等待,可以做其他操作
AJAX的优点：
    1.异步的访问方式　
    2.局部的刷新方式
使用场合：
    1.搜索建议　
    2.表单验证　
    3.前后端完全分离
SPA--->Singal Page Application

AJAX核心对象----异步对象(XMLHttpRequest)
什么是XMLHttpRequest?
    简称为：xhr,称为"异步对象",代替浏览器向服务器发送异步的请求并接受响应
创建异步对象
    xhr的创建是由js来提供的,主流的异步对象是XMLHttpRequest类型的,并且主流浏览器都支持
(IE7+,Chrome,Firefox,Safari,Opera)

支持XMLHttpRequest:
    通过new XMLHttpRequest()
不支持XMLHttpRequest:
    通过　nex ActiveXObject("Microsoft.XMLHTTP")
判断浏览器的支持性：
    if(window.XMLHttpRequest){
        则说明浏览器支持XMLHttpRequest
    }else{
        则说明浏览器支持ActiveXObject("...")
    }
    
XHR的成员
    方法：open()
    作用：创建请求
    语法：xhr.open(method,url,async);
    method:请求方式,取值"get"或"post"
    url:请求地址,取值　字符串
    async:是否采用异步的方式发送请求
        true:异步的
        false:同步的
    示例：使用get方式向server的地址发送异步请求
        xhr.open("get","/server",true)
        
    属性－－readyState
    作用：表示请求状态,通过不同的请求状态值来表示xhr与服务器的交互情况
    由0~4共5个值来表示5个不同的状态
    0:请求尚未初始化
    1:已经与服务器建立连接
    2:服务器端已经接收请求信息
    3:服务器端处理中...
    4:响应完成
    
    属性－－status
    作用：表示服务器端的响应状态码
    200:服务器端正确处理请求并给出响应
    404:Not Found
    500:Internal Server Error
    示例：
        if(xhr.readyState==4　&&　xhr.status==200){
            //可以接收服务器端的响应信息
        }
    
    属性－－responseText
    作用：表示服务器端响应回来的数据
    示例：
        if(xhr.readyState==4　&&　xhr.status==200){
            //可以接收服务器端的响应信息
            console.log(xhr.reqponseText);
        }
        
    事件－－onreadystatechange
    作用：每当xhr的readyState的值发生改变时要触发的操作－－回调函数
    示例：
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4　&&　xhr.status==200){
            //可以接收服务器端的响应信息
            console.log(xhr.reqponseText);
            }
        }
        
    方法－－send()
    作用：通知xhr向服务器端开始发送请求
    语法：xhr.send(body)
        body:请求主体
        get请求：body的值为null
            xhr.send(null)
        post请求：body的值为具体的请求数据
            xhr.send("请求数据")
            
AJAX的操作步骤
(1)GET请求
    1.创建xhr
    2.创建请求--open()
    3.设置回调函数--onreadystatechange
        1.判断状态
        2.接收响应
        3.业务处理
    4.发送请求--send(null)            
"""""

"""
1.使用AJAX发送POST请求
(1)创建xhr
(2)创建请求
    1.请求方式改为post
    2.有请求参数的话不能拼在地址的后
    3.设置回调函数
    4.设置请求消息头Content-Type
    xhr.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    )
    5.发送请求
    请求数据在send()的参数位置处
    示例：
        xhr.send("name=wang&age=25&gender=男");
        
JSON
介绍JSON:JavaScript Object Notation
            js      对象　　　表现方式
以JS对象的格式来约束前后端交互的字符串数据
JSO--JS对象
    使用JS对象表示一个人的信息,包含如下属性：
    姓名：王二
    年龄：25
    身高：178
    体重：178
    var obj={
        name:"王二",
        age:25,
        height:178,
        weight:178
    }
    console.log("姓名："+obj.name);
    (1)使用JSON表示单个对象
        使用{}表示一个对象
        在{}中使用key:value来表示属性(数据)
        key必须使用“”引起来
        value如果是字符串的话,也必须使用""引起来
        多对key:value之间使用,分离
        示例：
        var obj='{"name":"wang","age":25}';
    (2)使用JSON表示多个对象
        使用[]来表示一组对象
        示例：使用JSON表示2个人的信息
        var users='[{"name":"wang","age":25},{"name":"yang","age":26}]';
前端中处理JSON
    将得到的JSON串转换成JS对象/数组
    var JS对象=JSON.parse(JSON)
        
"""