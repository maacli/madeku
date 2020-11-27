## 标准选择器



标签选择器

标签{ }



<h1 class="项目名字"> </h1>

class   类选择器的样式  .class的名称 { }

好处：可以多个标签归类，是同一个 class



id选择器，id必须保证全局唯一！

#id名称{ }

优先级：不遵循就近原则，固定的

id选择器>class选择器>标签选择器



## 层次选择器

1. 后代选择器

   body  p{  

   }

2. 子选择器

   body>p{

   }

3. 相邻兄弟选择器

   “名称” + p{

   }

   只有一个（向下）

   

4. 通用选择器

   “名称”~p{

   }

   当前选中元素向下的所有兄弟元素,选中的元素不包括

```html
<style>
    .mm ~ p {background-color: lightslategray;}
    body p{color: lightblue;}
    body>p{color: lightcoral;}
    .ma~li{background-color: mediumvioletred;}
</style>

</head>
<body>
    <p class="mm">p1</p>
    <p>2</p>
        <h1>1</h1>
        <h1>1</h1>
        <h1>1</h1>
        <h1>1</h1>
    
    <p>3 </p>
    <p>3 </p>
    <p>3 </p>
    <ul>

        <li class="ma">
            <p>4</p>
        </li>
        <li>
            <p>4</p>
        </li>
        <li>
            <p>4</p>
        </li>
    </ul>
    <p class="mm">p1</p>
    <p>p6</p>
</body>
</html>
```





## 结构伪类选择器

伪类

```html
  <style>
        ul li:first-child{      /*ul的第一个子元素*/
            background:mediumvioletred;
        }

        ul li:last-child{   /*ul的最后一个子元素*/
            background: olivedrab;
        }

        p:nth-child(1){    /* 选中p1，定位到父级元素，选择当前的第一个元素，并且是当前类型元素才生效*/
            background: peru;
        }
    </style>
```

![image-20201120234029443](C:\Users\15821\AppData\Roaming\Typora\typora-user-images\image-20201120234029443.png)



## 属性选择器

```html
a[id="first"]{     /*存在id属性的元素   a[id=""]{}      */  
                background: rgb(204, 190, 190);
            }

            a[class*="links"]{   /*   *= 是含有这个元素就行，= 是绝对等于*/
                background: magenta;
            }

            a[href^=http]{      /*  href中以HTTP开头（^=）的选中*/
                background: olive;
            }

            a[href$=pdf]{       /*href中以pdf结尾（$=）的选中*/
                background: papayawhip;
            }
```

**对应html代码：**

```html
<body>
   <p class="demo">

    <a href="http://www.baidu.com" class="links item first"   id="first">1</a>
    <a href="a" class="links item active" target="-_blank" title="text">2</a>
    <a href="images/123.html" class="links item">3</a>
    <a href="images/1.html" class="links item">4  </a>
    <a href="images/1.png" class="links item"> 5 </a>
    <a href="abc" class="links item" >  6</a>
    <a href="/a.pdf" class="links item">  7</a>
    <a href="/abc.pdf" class="links item" >  8</a>
    <a href="/a.doc" class="links item last">  9</a>

</p>
</body>
```

![image-20201121005033156](C:\Users\15821\AppData\Roaming\Typora\typora-user-images\image-20201121005033156.png)



## 字体

```html
 font-family: sans-serif;     /*字体*/
           background: peru;
           font-size: 20px;  /*字体大小*/
           font-weight: 1000;       /*字体粗细*/
           /* font:oblique tolder 16px "楷体"；结合起来用*/
```



![image-20201121011703019](C:\Users\15821\AppData\Roaming\Typora\typora-user-images\image-20201121011703019.png)



```html

       body{
          
              text-indent: 2em; /*首行缩进*/
                
       }
       
       h1{
           text-align: center;  /*文本对齐方式*/
       }

       .p1{
           background: chartreuse;
           height: 250px; /*代码块所占高度*/
           line-height: 50px;   /*行高*/
       }

       .op{
           text-decoration: underline;  /*下划线*/
       }
       .ok{
           text-decoration: line-through;   /*中划线*/
       }
       .ol{
           text-decoration: overline;      /*上划线*/
       }
    </style>

</head>
<body>
    <h1>machuanlin</h1>

    <p class="op">lalal</p>
    <p class="ok">lalal</p>
    <p class="ol">lalal</p>

    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis, sunt.

    </p>
    <p class="p1">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque quo vitae, dolores cupiditate velit commodi soluta temporibus nulla porro earum autem doloribus ea quis. Minima non id ratione sapiente tempora harum deserunt aspernatur ullam qui rem libero impedit, 

    </p>
```



**hver**  :鼠标悬浮状态

**active**：鼠标按住未释放状态

a：active{ 

}

**列表样式**：

```html
  ul li{
           height: 30px;
           list-style: none;    /*列表前的小圆点去掉;circle  空心圆； decimal 数字； square  正方形*/
       }

```



**背景设置**：

```
 div{
           width: 1000px;
           height: 700px;
           border: 1px solid red; /*顺序为 粗细、样式（实线）、颜色*/
           
           background: #cddc39 url(geek.png) 600px 500px no-repeat;
       }

```



## 圆角边框

```html
<style>
      div{
          width: 100px;
          height: 100px;
          border: 10px solid red;
          border-radius: 50px 20px 10px 5px ;   /*边框，顺时针*/
      }
      img{
          border-radius: 100px;     /*更改图片边框*/
      }
```



## 盒子阴影

```html
  box-shadow: 10px 50px 100px yellow;  //盒子阴影
```





## display和浮动

```
display：block  块元素（默认）

​                inline   行内元素

​					inline-block	是块元素也是行内元素
```



```
float 浮动
```

### 父级边框塌陷问题

1. 增加父级元素的高度

2. 增加一个空的 div 标签，清除浮动

3. overflow：hidden  

   在父级元素中增加一个overflow（块高度由内容撑起）

4. 父类添加一个伪类：after

   ```html
   #father：after{
       content：‘’
       display：block
     	clear：both
   	}
   ```

   

## 定位

###  相对定位

相对原来的位置进行偏移，它仍然在标准文档流中

```html
position: relative;//相对定位
top: 20px; /*距离顶部的位置*/    
bottom: 10px;   /*距离底部的位置*/
```



###  绝对定位

``` 
position：absolute
```



定位：基于xxx定位，

1. 没有父级元素定位的前提下，相对于浏览器定位
2. 假设父级元素存在定位，相对于父级元素进行偏移
3. 在父级元素范围内移动

### 固定定位

```
position:fixed;
```



### z-index

图层,默认是  0 层

```
z-index:0
```



