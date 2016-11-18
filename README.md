# django-mixinvideos
Mixin para plataformas de vídeos

##Install
```bash
pip install django-mixinvideos
```
Para usar o mixin adicione `mixin_videos` em seu `INSTALLED_APPS`

##Usage
Em seu `models.py`
```python
from mixin_videos.mixin import VideoMixin

class Foo(VideoMixin):
    pass
```
Em sua `template`, para exibir o iframe:
```html
    <div>
        {{ foo.iframe|safe }}
    </div>
```
Caso queira exibir a imagem de capa padrão:
```html
    <img src="{{ foo.thumb }}" alt="foo"/>
```
