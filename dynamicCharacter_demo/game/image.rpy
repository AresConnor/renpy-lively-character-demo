init:
    image wink00:
        'images/eye_wink/琴里-1/0.png'
    image wink01:
        'images/eye_wink/琴里-1/1.png'
    image wink02:
        'images/eye_wink/琴里-1/2.png'
    image wink03:
        'images/eye_wink/琴里-1/3.png'
    image wink10:
        'images/eye_wink/琴里-1嘲讽/0.png'
    image wink11:
        'images/eye_wink/琴里-1嘲讽/1.png'
    image wink12:
        'images/eye_wink/琴里-1嘲讽/2.png'
    image wink13:
        'images/eye_wink/琴里-1嘲讽/3.png'
    image wink20:
        'images/eye_wink/琴里-1害羞/0.png'
    image wink21:
        'images/eye_wink/琴里-1害羞/1.png'
    image wink22:
        'images/eye_wink/琴里-1害羞/2.png'
    image wink23:
        'images/eye_wink/琴里-1害羞/3.png'

    image kotori_emotion_nor:
        'images/emotion/琴里-1.png'
    image kotori_emotion_chaofeng:
        'images/emotion/琴里-1嘲讽.png'
    image kotori_emotion_shy:
        'images/emotion/琴里-1害羞.png'

    image kotori_speaking00:
        'images/speaking/琴里-1/0.png'
    image kotori_speaking01:
        'images/speaking/琴里-1/1.png'
    image kotori_speaking02:
        'images/speaking/琴里-1/2.png'
    image kotori_speaking03:
        'images/speaking/琴里-1/1.png'
    image kotori_speaking10:
        'images/speaking/琴里-1嘲讽/0.png'
    image kotori_speaking11:
        'images/speaking/琴里-1嘲讽/1.png'
    image kotori_speaking12:
        'images/speaking/琴里-1嘲讽/2.png'
    image kotori_speaking13:
        'images/speaking/琴里-1嘲讽/1.png'
    image kotori_speaking20:
        'images/speaking/琴里-1害羞/0.png'
    image kotori_speaking21:
        'images/speaking/琴里-1害羞/1.png'
    image kotori_speaking22:
        'images/speaking/琴里-1害羞/2.png'
    image kotori_speaking23:
        'images/speaking/琴里-1害羞/1.png'

image chara_nor_winking:
    'wink00'
    choice 5:
        5.0
    choice 4:
        3.0
    choice 1:
        1.0
    'wink01'
    0.03
    'wink02'
    0.03
    'wink03'
    0.03
    'wink02'
    0.05
    'wink01'
    0.05
    repeat
image chara_chaofeng_winking:
    'wink10'
    choice 5:
        5.0
    choice 4:
        3.0
    choice 1:
        1.0
    'wink11'
    0.03
    'wink12'
    0.03
    'wink13'
    0.03
    'wink12'
    0.05
    'wink11'
    0.05
    repeat
image chara_shy_winking:
    'wink20'
    choice 5:
        5.0
    choice 4:
        3.0
    choice 1:
        1.0
    'wink21'
    0.03
    'wink22'
    0.03
    'wink23'
    0.03
    'wink22'
    0.05
    'wink21'
    0.05
    repeat

image chara_nor_speaking_imgs:
    'kotori_speaking00'
    0.1
    'kotori_speaking01'
    0.1
    'kotori_speaking02'
    0.1
    'kotori_speaking03'
    repeat
image chara_chaofeng_speaking_imgs:
    'kotori_speaking10'
    0.1
    'kotori_speaking11'
    0.1
    'kotori_speaking12'
    0.1
    'kotori_speaking13'
    repeat
image chara_shy_speaking_imgs:
    'kotori_speaking20'
    0.1
    'kotori_speaking21'
    0.1
    'kotori_speaking22'
    0.1
    'kotori_speaking23'
    0.1
    repeat

image chara_quiet:
    Color(color='#0000', hls=None, hsv=None, rgb=None, alpha=0)
    xsize 96
    ysize 36

image chara_nor_speaking = DynamicDisplayable(chara_demo_nor_talking)
image chara_chaofeng_speaking = DynamicDisplayable(chara_demo_chaofeng_talking)
image chara_shy_speaking = DynamicDisplayable(chara_demo_shy_talking)

layeredimage chara_demo_image:
    always:
        'images/琴里.png'
    group emotion:
        pos (192,111)
        attribute normal default:
            'kotori_emotion_nor'
        attribute chaofeng:
            'kotori_emotion_chaofeng'
        attribute shy:
            'kotori_emotion_shy'
    group face:
        pos (267,242)
        attribute nor_winking default:
            'chara_nor_winking'
        attribute chaofeng_winking:
            'chara_chaofeng_winking'
        attribute shy_winking:
            'chara_shy_winking'
    group mouth:
        pos (298,283)
        attribute nor_speaking:
            'chara_nor_speaking'
        attribute chaofeng_speaking:
            'chara_chaofeng_speaking'
        attribute shy_speaking:
            'chara_shy_speaking'

image bg:
    'images/BG1701.png'
    zoom 0.67