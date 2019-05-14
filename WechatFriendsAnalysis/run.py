"""
Brief Description: 运行脚本，将依次执行全部的分析过程
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create: 2019-05-14 By deimo.
Copyright (C) jadger@163.com 2019 All Rights Reserved.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import wechat_area
import wechat_photo
import wechat_sign
import wechat_friend

if __name__ == '__main__':
    wechat_area.deal()
    wechat_friend.deal()
    wechat_sign.deal()
    wechat_photo.deal()

