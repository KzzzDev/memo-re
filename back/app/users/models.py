from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(object):
        db_table = 'custom_user'
        verbose_name = verbose_name_plural = 'カスタムユーザー'

    score = models.IntegerField(verbose_name='点数', default=0)
    score_updated_at = models.DateTimeField(verbose_name='点数更新日時', null=True, blank=True)
    ranking = models.IntegerField(verbose_name='ランキング', null=True, blank=True)
    icon = models.ImageField(verbose_name='アイコン', upload_to='icon/', default='icon/default.jpg')
    icon_thumbnail = ImageSpecField(source='icon',
                                    processors=[ResizeToFill(300, 300)],
                                    format='JPEG', )
