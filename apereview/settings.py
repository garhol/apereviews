# Django settings for apereview project.
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('garhol', 'chimpoid@gmail.com'),
)
SERVER_EMAIL = 'info@apemanvinyl.com'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'apeblog_db',                      # Or path to database file if using sqlite3.
        'USER': 'apeman_blog',                      # Not used with sqlite3.
        'PASSWORD': 'k4Q72fTh',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'apemanvinyl.com', 'www.apemanvinyl.com', 'blog.apemanvinyl.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/apeman/webapps/apeblog_static/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/static/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home/apeman/webapps/apeblog_static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.

    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'anc%9vv(0-95lcx)=q5v+t7ua2t$01d151anfu2+)o$&qkq1u9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'apereview.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'apereview.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.core.context_processors.request",
"django.contrib.messages.context_processors.messages",
"social_auth.context_processors.social_auth_by_name_backends",
"social_auth.context_processors.social_auth_backends",
"social_auth.context_processors.social_auth_by_type_backends",
"social_auth.context_processors.social_auth_login_redirect",
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

ITEMS_PER_PAGE = 6

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apereview.lib.apps.reviews',
    'apereview.lib.apps.news',
    'apereview.lib.apps.playlist',
    'apereview.lib.apps.artwork',
    'apereview.lib.apps.personnel',
    'apereview.lib.apps.home',
    'apereview.lib.apps.about',
    'apereview.lib.apps.pipelines',
    'tinymce',
    'easy_thumbnails',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    'south',
    'disqus',
    'tastypie',
    'tastypie_swagger',
    'social_auth',
)


DISQUS_API_KEY = 'sqErCtNyeD9pOrVMTkPQ9MYg5H4nfOweYAvqx3tA5WX6rALRWxAnws5xGMwN6fWQ'
DISQUS_WEBSITE_SHORTNAME = 'apemanvinyl'
SHOW_COMMENTS = True

TASTYPIE_SWAGGER_API_MODULE = 'apereview.urls.v1_api'

TINYMCE_DEFAULT_CONFIG = {
'theme': "advanced",
'theme_advanced_toolbar_location': "top",
#'theme_advanced_buttons1': "bold,italic,underline,separator,"
#    "bullist,separator,outdent,indent,separator,undo,redo",
#'theme_advanced_buttons2': "",
'theme_advanced_buttons2_add': "paste,pastetext,pasteword,anchor,",
'theme_advanced_buttons3': "",
'plugins': "paste", 
}

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'apereview.lib.apps.pipelines.pipeline.get_music_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
)


FACEBOOK_APP_ID              = '480810641997337'
FACEBOOK_API_SECRET          = '50a4de64563dc7c79556eec3e24c95fb'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

PREPEND_WWW = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
