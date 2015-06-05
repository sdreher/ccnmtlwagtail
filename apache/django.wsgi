import os, sys, site

# enable the virtualenv
site.addsitedir('/var/www/ccnmtlwagtail/ccnmtlwagtail/ve/lib/python2.7/site-packages')

# paths we might need to pick up the project's settings
sys.path.append('/var/www/ccnmtlwagtail/ccnmtlwagtail/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ccnmtlwagtail.settings_production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
