from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class FormEntriesApphook(CMSApp):
    name = _('Forms')
    # urls = ['djangocms_forms.urls']

apphook_pool.register(FormEntriesApphook)