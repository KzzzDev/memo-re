from django.core.exceptions import ValidationError, NON_FIELD_ERRORS, ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
from django.utils import timezone


class Friend(models.Model):
    """フレンドモデル"""

    class Meta(object):
        db_table = 'friend'
        verbose_name = verbose_name_plural = 'フレンド'

        constraints = [
            # own_idとfriend_idでユニーク制約
            models.UniqueConstraint(
                fields=['own_id', 'friend_id'], name='unique_friend')
        ]

    own_id = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（自分）",
        related_name="friend_own_id",
        on_delete=models.CASCADE,
    )
    friend_id = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（相手）",
        related_name="friend_friend_id",
        on_delete=models.CASCADE
    )
    approval = models.BooleanField(
        _("登録状態"),
        default=False,
    )
    register_at = models.DateTimeField(
        _("登録日付"),
        default=timezone.now,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.id)

    # 未入力の際のエラーとown_idとfriend_idが同じ際のエラーをまとめたもの
    def clean(self):
        try:
            if self.own_id == self.friend_id:
                raise ValidationError(
                    {'friend_id': "自分と相手が同じユーザーです。"},
                )
        except ObjectDoesNotExist:
            pass


class Note(models.Model):
    """ノートモデル"""

    class Meta(object):
        db_table = 'note'
        verbose_name = verbose_name_plural = 'ノート'

    user_id = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザID",
        related_name="note_user_id",
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        _("タイトル"),
        max_length=255,
    )
    keyword = models.CharField(
        _("キーワード"),
        max_length=255,
    )
    text_uri = models.CharField(
        _('テキストURI'),
        max_length=255,
        blank=True,
        null=True,
    )
    image_uri = models.ImageField(
        _('画像URI'),
        upload_to='image',
    )
    created_at = models.DateTimeField(
        _("作成日"),
        default=timezone.now,
    )
    is_active = models.BooleanField(
        _("有効"),
        default=True,
    )
    is_public = models.BooleanField(
        _("公開状態"),
        default=True,
    )

    def __str__(self):
        return str(self.id)


class NoteShare(models.Model):
    """ノート共有モデル"""

    class Meta(object):
        db_table = 'note_share'
        verbose_name = verbose_name_plural = 'ノート共有'

        constraints = [
            # own_idとfriend_idとnote_idでユニーク制約
            models.UniqueConstraint(
                fields=['own_id', 'friend_id', 'note_id'], name='unique_noteshare')
        ]

    own_id = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（自分）",
        related_name="noteshare_own_id",
        on_delete=models.CASCADE,
    )
    friend_id = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（相手）",
        related_name="noteshare_friend_id",
        on_delete=models.CASCADE,
    )
    note_id = models.ForeignKey(
        Note,
        verbose_name="ノートID",
        related_name="noteshare_note_id",
        on_delete=models.CASCADE,
    )
    notified = models.BooleanField(
        _("通知"),
        default=True,
    )
    apply = models.BooleanField(
        _("申請"),
        default=False,
    )

    def __str__(self):
        return str(self.id)

    # 未入力の際のエラーとown_idとfriend_idが同じ際のエラーをまとめたもの
    def clean(self):
        try:
            if self.own_id == self.friend_id:
                raise ValidationError(
                    {'friend_id': "自分と相手が同じユーザーです。"},
                )
        except ObjectDoesNotExist:
            pass
