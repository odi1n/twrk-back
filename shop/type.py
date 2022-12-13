from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusType(models.TextChoices):
    IN_STOCK = 'in_stock', _('in_stock')
    OUT_OF_STOCK = 'out_of_stock', _('out_of_stock')
    ON_COMMAND = 'on_command', _('on_command')
    WAITING_RECEIPT = 'waiting_receipt', _('waiting_receipt')
    DONT_PRODUCE = 'dont_produce', _('dont_produce')


class Type(models.TextChoices):
    STRING = 'string', _('string')
    DECIMAL = 'decimal', _('decimal')
