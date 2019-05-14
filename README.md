## 项目介绍

一组有趣的微信好友分析脚本:)~

希望你也能喜欢

**特别说明**

>项目中的核心代码并非我原创，乃是一位id为Xusl的作者所作，本人首次接触到代码是在**Python中文社区**的[文章](<https://mp.weixin.qq.com/s/IvnFTvzSEBsGcf5EFFnx0A>)上

如果觉得有顺带用就点个关注吧:)

技术实现上借助了[itchat库](<https://github.com/littlecodersh/ItChat>)使用微信网页版的API接口来获取个人好友的信息

**项目目录结构**

![](proj.jpg)

|    目录or文件    |                   作用                   |
| :--------------: | :--------------------------------------: |
|     conf目录     |            分词有关的背景图片            |
|    config.py     |        后去logger.conf的相对位置         |
|    fonts目录     |               中文字体文件               |
|     log目录      |       itchat运行时相关日志所在未知       |
|   logging.conf   |          logger模块相关配置信息          |
|   **res目录**    | **所有的分析结果最终都会生成在此目录中** |
|  wechat_area.py  |           分析微信好友地区分步           |
| wechat_friend.py |          分析微信好友的性别占比          |
|  wechat_sign.py  |  生成微信好友的个性签名的词云及情感分析  |
| wechat_photo.py  |           生成维系好友头像拼接           |
|      run.py      |              上述操作的集合              |



本项目相比原作者而言，修改或完善了如下内容：

1. 增加了依赖安装列表
2. 修改部分目录代码结构
3. 修复好友拼图时jpg格式图片不支持RGBA问题
4. 更优雅地解决matplotlib绘图库的中文显示问题
5. 增加了一个详尽的README…这样大家就都很方便能玩了...

## 要求

1. Python3.0+
2. mac OS(因为当前代码只在macOS上调试过，运行良好，其它平台，还请大佬们自行调整)

## 如何使用

1. 创建虚拟环境

   ```bash
   python3 -m venv env
   ```

2. 激活虚拟环境

   ```bash
   source env/bin/activate
   ```

3. 安装依赖

   ```bash
   pip install -r requirements.txt
   ```

4. 按需生成自己的各种分析数据

   ```bash
   python wechat_area.py 	# 生成微信好友地区分析数据
   python wechat_friend.py # 生成微信好友性别占比数据
   python wechat_photo.py  # 生成微信好友的头像拼接
   python wechat_sign.py   # 生成微信好友的个性签名的词云及情感分析
   python run.py						# 上述操作依次执行
   ```


# Q&A

1. Question: mac os下如何解决matplotlib的中文显示问题

   Answer: 在虚拟环境下执行如下脚本：

   ```python
   In [1]: import matplotlib as mpl
   In [2]: mpl.matplotlib_fname()
   Out[2]: '/[your path]/matplotlib/mpl-data/matplotlibrc'
   ```

   来到matplotlibrc文件所在的上一级目录，然后将项目**fonts目录**下的**STFANGSO.ttf**字体文件copy到**/[your path]/matplotlib/mpl-data/fonts/ttf**目录下即可

