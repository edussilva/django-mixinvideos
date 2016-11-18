# coding: utf-8
from django.db import models
import requests


class VideoMixin(models.Model):

    IFRAME_VIMEO = '<iframe src="https://player.vimeo.com/video/{}?color=000" width="560" height="315" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>'
    IFRAME_YOUTUBE = '<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>'

    THUMB_YOUTUBE = 'http://img.youtube.com/vi/{}/default.jpg'
    # TODO: Verificar se é possivel consumir a thumb através de uma url, não por json (vimeo)
    THUMB_VIMEO = ''

    video_url = models.URLField(verbose_name=u'URL', help_text=u'Insira a url do vídeo (Youtube ou Vimeo)')

    class Meta:
        abstract = True

    @property
    def get_url(self):
        return self.video_url

    @property
    def id_youtube(self):
        # TODO: usar expressão regular
        _url = self.get_url
        if 'youtu.be' in _url:
            return _url.split('/')[-1]
        elif 'www.youtube.com/embed/' in _url:
            return _url.split('/')[-1].split('?')[0]
        elif 'www.youtube.com' in _url:
            return _url.split('/')[-1].replace('watch?v=', '').split('&')[0]
        return ''

    @property
    def id_vimeo(self):
        return self.get_url.split('/')[-1]

    def _iframe_vimeo(self):
        return self.IFRAME_VIMEO.format(self.id_vimeo)

    def _thumb_vimeo(self):
        # TODO passar para .js
        try:
            _endpoint = 'http://vimeo.com/api/v2/video/{}.json'.format(self.id_vimeo)
            response = requests.get(_endpoint)
            obj = response.json()[0]
            return obj['thumbnail_medium']
        except:
            return ''
        # return self.THUMB_VIMEO.format(self.id_vimeo)

    def _iframe_youtube(self):
        return self.IFRAME_YOUTUBE.format(self.id_youtube)

    def _thumb_youtube(self):
        return self.THUMB_YOUTUBE.format(self.id_youtube)

    def iframe(self):
        _url = self.get_url
        if 'vimeo' in _url:
            return self._iframe_vimeo()
        elif 'youtu' in _url:
            return self._iframe_youtube()
        return ''

    def thumb(self):
        _url = self.get_url
        if 'vimeo' in _url:
            return self._thumb_vimeo()
        elif 'youtu' in _url:
            return self._thumb_youtube()
        return ''

    def get_src(self):
        return self.iframe().split('src="')[1].split('"')[0]
