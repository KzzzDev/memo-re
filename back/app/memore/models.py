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
            # own_idとuser_to_idでユニーク制約
            models.UniqueConstraint(
                fields=['user_from', 'user_to'], name='unique_user_to')
        ]

    user_from = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（自分）",
        related_name="friend_user_from_id",
        on_delete=models.CASCADE,
    )
    user_to = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（相手）",
        related_name="friend_user_to_id",
        on_delete=models.CASCADE
    )
    notified = models.BooleanField(
        _("通知"),
        default=True,
    )
    apply = models.BooleanField(
        _("申請ステータス"),
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

    # 未入力の際のエラーとown_idとuser_to_idが同じ際のエラーをまとめたもの
    def clean(self):
        try:
            if self.user_from == self.user_to:
                raise ValidationError(
                    {'user_to': "自分と相手が同じユーザーです。"},
                )
        except ObjectDoesNotExist:
            pass


class Note(models.Model):
    """ノートモデル"""

    class Meta(object):
        db_table = 'note'
        verbose_name = verbose_name_plural = 'ノート'

    user = models.ForeignKey(
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
    image_uri = models.CharField(
        _('画像URI'),
        max_length=255,
        # upload_to='image',
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
            # own_idとuser_to_idとnote_idでユニーク制約
            models.UniqueConstraint(
                fields=['user_from', 'user_to', 'note'], name='unique_noteshare')
        ]

    user_from = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（自分）",
        related_name="noteshare_user_from_id",
        on_delete=models.CASCADE,
    )
    user_to = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザ（相手）",
        related_name="noteshare_user_to_id",
        on_delete=models.CASCADE,
    )
    note = models.ForeignKey(
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
    register_at = models.DateTimeField(
        _("登録日付"),
        default=timezone.now,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.id)

    # 未入力の際のエラーとown_idとuser_to_idが同じ際のエラーをまとめたもの
    def clean(self):
        try:
            if self.user_from == self.user_to:
                raise ValidationError(
                    {'user_to': "自分と相手が同じユーザーです。"},
                )
        except ObjectDoesNotExist:
            pass
