from django.db import models
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    name = models.CharField(_("Название задачи"), max_length=255, default='')
    description = models.TextField(_("Описание задачи"),blank=True)
    is_favorite = models.BooleanField(_("В избранном"),default=False)
    is_completed = models.BooleanField(_("Выполнена"),default=False)
    created_at = models.DateTimeField(_("Дата создания"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"),auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
