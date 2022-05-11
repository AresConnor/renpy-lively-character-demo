init python:
    def chara_demo_nor_talking(st,at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag == 'chara_demo_voice':
            return ('chara_nor_speaking_imgs',0.1)
        else:
            return ('chara_quiet',0.1)
    def chara_demo_chaofeng_talking(st,at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag == 'chara_demo_voice':
            return ('chara_chaofeng_speaking_imgs',0.1)
        else:
            return ('chara_quiet',0.1)
    def chara_demo_shy_talking(st,at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag == 'chara_demo_voice':
            return ('chara_shy_speaking_imgs',0.1)
        else:
            return ('chara_quiet',0.1)