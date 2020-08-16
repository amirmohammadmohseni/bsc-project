from django.db import models
from django.contrib.auth.models import User


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=8)

    class Role(models.TextChoices):
        STUDENT = 'ST', _('Student')
        PROFESSOR = 'PR', _('Professor')
        ADMIN = 'AD', _('Admin')

    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.STUDENT,
    )


class Student(BaseUser):
    field = models.ForeignKey('Field', on_delete=models.SET_NULL, null=True)
    enteranceYear = models.SmallIntegerField()
    advisorProf = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)


class Professor(BaseUser):
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)


class Group(models.Model):
    title = models.CharField(max_length=30)
    manager = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'pk': self.pk})


class Field(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = _('field')
        verbose_name_plural = _('fields')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('field_detail', kwargs={'pk': self.pk})
