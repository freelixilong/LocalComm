
from django.utils.translation import ugettext_lazy as _
STATUS_CHOICES = [
    ('active', _('In Using')),
    ('delete', _('Deleted')),
    ('lock', _('Only view, cannot edit it')),
]
SEX_CHOICE = [
    ('M', _('male')),
    ('F', _('Female')),
]
PRIVILEDGE_CHOICE = [
    ('super', _('super administrator')),
    ('admin', _('board adminitrator')),
    ('user', _('common user')),
]