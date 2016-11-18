# django-mixinvideos
Mixin para plataformas de vídeos

##Install
'''bash
pip install django-mixinvideos
'''
Para usar o mixin adicione 'mixin_videos' em seu 'INSTALLED_APPS'

##Usage
Em seu 'models.py'
'''python
from mixin_videos.mixin import VideoMixin


class Foo(VideoMixin):
    pass
'''
