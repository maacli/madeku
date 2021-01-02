# CSRF



**CSRF概念：**CSRF跨站点请求伪造(Cross—Site Request Forgery)，跟XSS攻击一样，存在巨大的危害性，你可以这样来理解：
    攻击者盗用了你的身份，以你的名义发送恶意请求，对服务器来说这个请求是完全合法的，但是却完成了攻击者所期望的一个操作，比如以你的名义发送邮件、发消息，盗取你的账号，添加系统管理员，甚至于购买商品、虚拟货币转账等。 如下：其中Web A为存在CSRF漏洞的网站，Web B为攻击者构建的恶意网站，User C为Web A网站的合法用户。

**CSRF攻击攻击原理及过程如下：**

​    1. 用户C打开浏览器，访问受信任网站A，输入用户名和密码请求登录网站A；

​    2.在用户信息通过验证后，网站A产生Cookie信息并返回给浏览器，此时用户登录网站A成功，可以正常发送请求到网站A；

​    3. 用户未退出网站A之前，在同一浏览器中，打开一个TAB页访问网站B；

​    4. 网站B接收到用户请求后，返回一些攻击性代码，并发出一个请求要求访问第三方站点A；

​	 5.浏览器在接收到这些攻击性代码后，根据网站B的请求，在用户不知情的情况下携带Cookie信息，向网站A发出请求。网站A并不知道该请求其实是由B发起的，所以会根据用户C的Cookie信息以C的权限处理该请求，导致来自网站B的恶意代码被执行。 	



**CSRF攻击实例**

​    受害者 Bob 在银行有一笔存款，通过对银行的网站发送请求 http://bank.example/withdraw?account=bob&amount=1000000&for=bob2 可以使 Bob 把 1000000 的存款转到 bob2 的账号下。通常情况下，该请求发送到网站后，服务器会先验证该请求是否来自一个合法的 session，并且该 session 的用户 Bob 已经成功登陆。

​    黑客 Mallory 自己在该银行也有账户，他知道上文中的 URL 可以把钱进行转帐操作。Mallory 可以自己发送一个请求给银行：http://bank.example/withdraw?account=bob&amount=1000000&for=Mallory。但是这个请求来自 Mallory 而非 Bob，他不能通过安全认证，因此该请求不会起作用。

​    这时，Mallory 想到使用 CSRF 的攻击方式，他先自己做一个网站，在网站中放入如下代码： src=”http://bank.example/withdraw?account=bob&amount=1000000&for=Mallory ”，并且通过广告等诱使 Bob 来访问他的网站。当 Bob 访问该网站时，上述 url 就会从 Bob 的浏览器发向银行，而这个请求会附带 Bob 浏览器中的 cookie 一起发向银行服务器。大多数情况下，该请求会失败，因为他要求 Bob 的认证信息。但是，如果 Bob 当时恰巧刚访问他的银行后不久，他的浏览器与银行网站之间的 session 尚未过期，浏览器的 cookie 之中含有 Bob 的认证信息。这时，悲剧发生了，这个 url 请求就会得到响应，钱将从 Bob 的账号转移到 Mallory 的账号，而 Bob 当时毫不知情。等以后 Bob 发现账户钱少了，即使他去银行查询日志，他也只能发现确实有一个来自于他本人的合法请求转移了资金，没有任何被攻击的痕迹。而 Mallory 则可以拿到钱后逍遥法外。 

**CSRF漏洞检测：**
    检测CSRF漏洞是一项比较繁琐的工作，最简单的方法就是抓取一个正常请求的数据包，去掉Referer字段后再重新提交，如果该提交还有效，那么基本上可以确定存在CSRF漏洞。

**防御CSRF攻击：**

​    目前防御 CSRF 攻击主要有三种策略：

1. 验证 HTTP Referer 字段；

2. 在请求地址中添加 token 并验证；

3. 在 HTTP 头中自定义属性并验证。



**（1）验证 HTTP Referer 字段**

​    根据 HTTP 协议，在 HTTP 头中有一个字段叫 Referer，它记录了该 HTTP 请求的来源地址。在通常情况下，访问一个安全受限页面的请求来自于同一个网站，比如需要访问 http://bank.example/withdraw?account=bob&amount=1000000&for=Mallory，用户必须先登陆 bank.example，然后通过点击页面上的按钮来触发转账事件。这时，该转帐请求的 Referer 值就会是转账按钮所在的页面的 URL，通常是以 bank.example 域名开头的地址。而如果黑客要对银行网站实施 CSRF 攻击，他只能在他自己的网站构造请求，当用户通过黑客的网站发送请求到银行时，该请求的 Referer 是指向黑客自己的网站。因此，要防御 CSRF 攻击，银行网站只需要对于每一个转账请求验证其 Referer 值，如果是以 bank.example 开头的域名，则说明该请求是来自银行网站自己的请求，是合法的。如果 Referer 是其他网站的话，则有可能是黑客的 CSRF 攻击，拒绝该请求。

**（2）在请求地址中添加 token 并验证**

​     CSRF 攻击之所以能够成功，是因为黑客可以完全伪造用户的请求，该请求中所有的用户验证信息都是存在于 cookie 中，因此黑客可以在不知道这些验证信息的情况下直接利用用户自己的 cookie 来通过安全验证。要抵御 CSRF，关键在于在请求中放入黑客所不能伪造的信息，并且该信息不存在于 cookie 之中。可以在 HTTP 请求中以参数的形式加入一个随机产生的 token，并在服务器端建立一个拦截器来验证这个 token，如果请求中没有 token 或者 token 内容不正确，则认为可能是 CSRF 攻击而拒绝该请求。

**（3）在 HTTP 头中自定义属性并验证**

​    这种方法也是使用 token 并进行验证，和上一种方法不同的是，这里并不是把 token 以参数的形式置于 HTTP 请求之中，而是把它放到 HTTP 头中自定义的属性里。通过 XMLHttpRequest 这个类，可以一次性给所有该类请求加上 csrftoken 这个 HTTP 头属性，并把 token 值放入其中。这样解决了上种方法在请求中加入 token 的不便，同时，通过 XMLHttpRequest 请求的地址不会被记录到浏览器的地址栏，也不用担心 token 会透过 Referer 泄露到其他网站中去。



**以下是三个 php文件的模拟**

```
<html>
<hred>
    <title>CSRF</title>
</hred>

<body>
    <form action="get.php" method="GET">
        <p>ID: <input type="text" name="inputid" /></p>
        <p>Money: <input type="text" name="inputmoney" /></p>
        <p><input type="submit" /></p>
    </form>
</body>

</html>
```

```
<html>
<head>
    <title>login</title>
</head>

<body>
    <form action="" method="GET">
        <p>name: <input type="text" name="name" /></p>
        <p>pass: <input type="text" name="pass" /></p>
        <p><input type="submit" value="login" /></p>
    </form>
</body>

</html>

<?php
    $name=$_GET['name'];
    $pass=$_GET['pass'];
    if(isset($name) && isset ($pass))
    {
        if($name == "deelmind" && $pass == "geek")
        {
            setcookie("csrf","deelmindgeekcookkie");
            header("location:http://192.168.64.2/csrf/main.php");     
        }
        else{
            header("location:http://192.168.64.2/csrf/index.php");
        }
    }
?>
```

```
<?php
    $cookie = $_COOKIE['csrf'];
    if(!isset($cookie)){
        exit();
    }
    if($cookie !='deelmindgeekcookie'){
        echo "exit";
        exit();
    }

    $id = $_GET['inputid'];
    $money = $_GET['inputmoney'];
    if(isset($id) && isset($money))
    {
        echo "买", $id,"花费",$money;
    }
    else{
        ehco "please input your etc";
    }    
    $money =100-$money;
    $sql ='update goods set price =',$money.'where name ="',$id.'"';
    //echo $sql."<br>";
    //Connect to a mysql server  连接数据库服务器
    $link = mysqli_connect(
        '192.168.64.2', //the host to connect to 连接mysql地址
        'myuser',  // the user to connect as  连接mysql用户名
        'my_password',  // the password to use  连接mysql密码
        'test');  // the default datebase to query 连接数据库名称
    // echo $link;
    if (!$link){
        printf ("can't connect to mysql server.Errorcode: %s",mysqli_connect_error());
        exit;
    }else
        echo '数据库连接上了！'，"</br>";
    if($result =mysql_query($link,$sql)){
        // fetch the result of the query 返回查询结果
    while( $row = mysqli_fetch_assoc($result)){
        echo $row['name'].$row['price'],"&nbsy;", "</br>";

    }
    mysqli_result($result); 
    }
    )
```

```
<html>
<head>
    <title>CSRF</title>
</head>
<body>
    <img src=http://192.168.64.2/csrf/get.php?inputid=goods1&inputmoney=3>
</body>
</html>
```

![](C:\Users\15821\Pictures\微信截图_20210103013512.png)