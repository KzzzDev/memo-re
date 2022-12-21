from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser


class Friend(models.Model):
    """フレンドモデル"""

    class Meta(object):
        db_table = 'friend'
        verbose_name = verbose_name_plural = 'フレンド'

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
