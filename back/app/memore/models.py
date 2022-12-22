from django.core.exceptions import ValidationError, NON_FIELD_ERRORS, ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser


class Friend(models.Model):
    """フレンドモデル"""

    class Meta(object):
        db_table = 'friend'
        verbose_name = verbose_name_plural = 'フレンド'

        constraints = [
            # leftとrightでユニーク制約
            models.UniqueConstraint(fields=['left', 'right'], name='unique_friend')
        ]

    left = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザー（自分）",
        related_name="left",
        on_delete=models.CASCADE,
    )
    right = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザー（相手）",
        related_name="right",
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    def __str__(self):
        return str(self.left)

    # 未入力の際のエラーとleftとrightが同じ際のエラーをまとめたもの
    def clean(self):
        try:
            if self.left == self.right:
                raise ValidationError(
                    {'right': "自分と相手が同じユーザーです。"},
                )
        except ObjectDoesNotExist:
            pass


# class Note(models.Model):
#     """ノートモデル"""
#
#     id =
#
#     class Meta(object):
#         db_table = 'note'
#         verbose_name = verbose_name_plural = 'ノート'
#
#     title =
#     keyword =
#
#
#     def __str__(self):
#         return str(self.id)
#
#
# class NoteShare(models.Model):
#
#
#     def __str__(self):
#         return str(self.)
