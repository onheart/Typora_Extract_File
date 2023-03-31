## 1.Typora提取单文件
一段时间内一直在纠结要怎么记笔记，试了有道云、印象笔记等，要么收费很贵，要么体验一般，还是不如Typora用
的舒服，可能就是用久了。但是去尝试其他的软件就是因为typora也有个让我很头疼的问题，图片管理太逼死强迫症了
，多个文件想要放在同一个文件夹内管理，图片目录也会显示在文档树内，十分难受，只能尽可能减少图片文件夹，同一个
目录下的图片统一放在assets内。

新的问题就是如果想单独拆出来一个文件，还要找到用了哪些图片，太费劲了。知道图片上传到云存储是一个不错的解决
方式，但是因为一些原因，如何找到本地笔记的解决办法还是我当前最急迫的。

现在的解决办法是写一个python的提取单文件的脚本，能够省去后顾之忧，好好学习，好好记笔记。

## 2.使用
很简单，运行``typora提取单文件.py``文件，提示输入提取文件的地址，输入确定即可。

脚本会在提取文件的同级目录中生成文件同名的文件夹，文件夹单独复制剪切出去即可
