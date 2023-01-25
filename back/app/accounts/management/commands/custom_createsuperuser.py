from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


# https://jumpyoshim.hatenablog.com/entry/how-to-automate-createsuperuser-on-django
from accounts.models import CustomUser


class Command(createsuperuser.Command):
    """custom_createsuperuserコマンド"""

    help = 'Create a superuser with a password non-interactively'

    # def add_arguments(self, parser):
    #     super(Command, self).add_arguments(parser)
    #     parser.add_argument(
    #         '--password',
    #         dest='password',
    #         default=None,
    #         help='Specifies the password for the superuser.',
    #     )

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.CustomUserModel = None

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        email = options.get('email')
        password = options.get('password')
        # userid = options.get('userid')
        username = options.get('username')

        if not (email and password and username):
            raise CommandError(
                '--email, --password and --username are required options'
            )

        user_data = {
            'email': email,
            'password': password,
            # 'userid': userid,
            'username': username,
        }

        exists_email = CustomUser.objects.filter(email=email).exists()
        # exists_userid = CustomUser.objects.filter(userid=userid).exists()

        # if exists_email and exists_userid:
        #     raise CommandError('This email and userid already exists.')
        # elif exists_email:
        #     raise CommandError('This email already exists.')
        # elif exists_userid:
        #     raise CommandError('This userid already exists.')
        # else:
        #     CustomUser.objects.create_superuser(**user_data)

        if exists_email:
            raise CommandError('This email already exists.')
        else:
            CustomUser.objects.create_superuser(**user_data)
