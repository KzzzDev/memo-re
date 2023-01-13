from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .validators import UnicodeUsernameValidator
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


# class UserManager(UserManager):
#     """認証をusernameからemailに変更"""
#
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(object):
        db_table = 'custom_user'
        verbose_name = verbose_name_plural = 'カスタムユーザー'

    # username_validator = UnicodeUsernameValidator()
    # userid_validator = UnicodeUseridValidator()

    # userid = models.CharField(
    #     _("ユーザーID"),
    #     max_length=30,
    #     help_text=_("この項目は必須です。半角アルファベット、半角数字、アンダースコアで30文字以下にしてください。"),
    #     validators=[userid_validator],
    #     unique=True
    # )
    username = models.CharField(
        _("ユーザ名"),
        max_length=255,
        # help_text=_("この項目は必須です。半角アルファベット、半角数字、@/./+/-/_ で30文字以下にしてください。"),
        # validators=[username_validator],
    )
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    icon_uri = models.ImageField(_('アイコンパス'), max_length=255, upload_to='icon', default='icon/default.jpg')
    # icon_thumbnail = ImageSpecField(
    #     source='icon_uri',
    #     processors=[ResizeToFill(300, 300)],
    #     format='JPEG',
    # )
    tag = models.CharField(_('タグ'), max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(_("作成日"), default=timezone.now)
    updated_at = models.DateTimeField(_("更新日"), blank=True, null=True)

    objects = UserManager()
    # usernameからemail認証に変更
    USERNAME_FIELD = 'email'
    # createsuperuserでemailの他に必須な項目
    REQUIRED_FIELDS = ["password", "username"]

    def __str__(self):
        return str(self.id)
