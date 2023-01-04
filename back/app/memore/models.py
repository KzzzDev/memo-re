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
            models.UniqueConstraint(
                fields=['left', 'right'], name='unique_friend')
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
        return str(self.left) + "+" + str(self.right)

    # 未入力の際のエラーとleftとrightが同じ際のエラーをまとめたもの
    def clean(self):
        try:
            if self.left == self.right:
                raise ValidationError(
                    {'right': "自分と相手が同じユーザーです。"},
                )
        except ObjectDoesNotExist:
            pass


class Note(models.Model):
    """ノートモデル"""

    class Meta(object):
        db_table = 'note'
        verbose_name = verbose_name_plural = 'ノート'

    title = models.CharField(
        _("タイトル"),
        max_length=30,
        blank=True, null=True,
        # validators=[title_validator],
    )
    creator = models.ForeignKey(
        CustomUser,
        verbose_name="作成者",
        related_name="creator",
        on_delete=models.CASCADE,
    )
    keyword = models.CharField(
        _("キーワード"),
        max_length=30,
        blank=True, null=True,
        # validators=[keyword_validator],
    )
    text = models.ImageField(
        _('テキスト'), upload_to='text', blank=True, null=True)
    image = models.ImageField(
        _('画像'), upload_to='image', blank=True, null=True)
    category = models.IntegerField(
        _("カテゴリ"),
        blank=True, null=True
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
        return str(self.id)


class NoteShare(models.Model):
    """ノート共有モデル"""

    class Meta(object):
        db_table = 'note_share'
        verbose_name = verbose_name_plural = 'ノート共有'

        constraints = [
            # user_idとnote_idでユニーク制約
            models.UniqueConstraint(
                fields=['user_id', 'note_id'], name='unique_note_share')
        ]

    user_id = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザーID",
        related_name="user_id",
        on_delete=models.CASCADE,
    )
    note_id = models.ForeignKey(
        Note,
        verbose_name="ノートID",
        related_name="note_id",
        on_delete=models.CASCADE,
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
        return str(self.user_id) + "+" + str(self.note_id)
