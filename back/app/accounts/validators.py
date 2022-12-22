from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, and @/./+/-/_ characters."
    )
    flags = 0

@deconstructible
class UnicodeUseridValidator(validators.RegexValidator):
    regex = r"^[\w]+\Z"
    message = _(
        "入力できる文字はアルファベット、数字、アンダースコアのみです。"
    )
    flags = 0
