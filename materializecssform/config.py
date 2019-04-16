from django.conf import settings

MATERIALIZECSS_COLUMN_COUNT = getattr(settings, 'MATERIALIZECSS_COLUMN_COUNT', 12)
MATERIALIZECSS_VALIDATION = getattr(settings, 'MATERIALIZECSS_VALIDATION', True)
MATERIALIZECSS_ICON_SET = getattr(settings, 'MATERIALIZECSS_ICON_SET', 'default')
