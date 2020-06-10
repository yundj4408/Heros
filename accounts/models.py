from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager): # 유저 관리 클래스
    def create_user(self, id, name, password=None, civnum=None, phnum=None): # 유저 생성 함수
        if not id:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            id=id,
            name=name,
            civnum=civnum,
            phnum=phnum,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, name, password=None,civnum=None, phnum=None): # 관리자유저 생성 함수
        user = self.create_user(
            name=name,
            id=id,
            password=password,
            civnum=civnum,
            phnum=phnum,
        )


        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin): #유저 모델
    id = models.CharField(
        verbose_name=_('ID'),
        max_length=20,
        unique=True,
        primary_key=True,
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=10,
        unique=True,
    )
    civnum = models.CharField(
        verbose_name=_('Civnum'),
        max_length=15,
        unique=True,
        default='civnum',
    )
    phnum = models.CharField(
        verbose_name=_('Phnum'),
        max_length=15,
        unique=True,
        default='phnum',
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now,
    )
    # 이 필드는 레거시 시스템 호환을 위해 추가할 수도 있다.
    salt = models.CharField(
        verbose_name=_('Salt'),
        max_length=10,
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'civnum', 'phnum']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.id

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    get_full_name.short_description = _('Full name')
