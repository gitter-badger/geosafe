# coding=utf-8
import os

__author__ = 'Rizky Maulana Nugraha <lana.pcfre@gmail.com>'
__date__ = '1/28/16'


try:
    # Put site specific configuration in this module
    import celeryconfiglocal
except:
    # This is a default value, in case configuration file is not found
    BROKER_URL = os.environ.get('INASAFE_HEADLESS_BROKER_HOST')

    CELERY_RESULT_BACKEND = BROKER_URL

    CELERY_ROUTES = {
        'headless.tasks.inasafe_wrapper': {
            'queue': 'inasafe-headless'
        }
    }
