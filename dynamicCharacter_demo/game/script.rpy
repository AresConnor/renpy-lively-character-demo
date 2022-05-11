# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define demo_chara = Character('琴里立绘demo',voice_tag = 'chara_demo_voice')


# 游戏在此开始。

label start:
    scene bg
    show chara_demo_image normal nor_winking at center
    '琴里normal 眨眼'
    show chara_demo_image chaofeng chaofeng_winking at center with Dissolve(0.5) 
    '琴里嘲讽 眨眼'
    show chara_demo_image shy shy_winking at center with Dissolve(0.5) 
    '琴里害羞 眨眼'
    '开始测试说话张嘴'
    show chara_demo_image chaofeng chaofeng_winking chaofeng_speaking at center with Dissolve(0.5)
    voice 'audio/chara_demo_voice.mp3'
    demo_chara '琴里说话....'
    
    return

