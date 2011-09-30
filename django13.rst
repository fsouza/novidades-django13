Novidades do Django 1.3
=======================

    Francisco Souza

    @franciscosouza

------------------------

Class Based Views
=================

.fx: build-code

.. class:: build

* Construção de views como classes
* Herança
* Mixins

.. sourcecode:: python

    class HelloWorldView(View):

        def get(self):
            return HttpResponse("Hello world")

------------------------

Class Based Views
=================

.. sourcecode:: python

    urlpatterns = patterns('',
        url('^hello', HelloWorldView.as_view()),
    )

------------------------

staticfiles
===========

* Fica com o Petry :)

------------------------

Logging handlers
================

------------------------

.fx: big-code

.. sourcecode:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'special': {
                '()': 'project.logging.SpecialFilter',
                'foo': 'bar',
            }
        },
        'handlers': {
            'null': {
                'level':'DEBUG',
                'class':'django.utils.log.NullHandler',
            },
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'formatter': 'simple'
            },

    [...]

------------------------

unittest2
=========

.. sourcecode:: python

    from django.utils import unittest


------------------------

RequestFactory
==============

.. sourcecode:: python

    from django.utils import unittest
    from django.test.client import RequestFactory
    from hello.views import HelloWorldView


    class TestHelloWorldView(unittest.TestCase)

        @classmethod
        def setUpClass(cls):
            cls.factory = RequestFactory()

        def test_say_hello(self):
            request = self.factory.get('/hello')
            view = HelloWorldView()
            response = view.get(request)
            self.assertEquals("Hello World", response.content)

------------------------

Obrigado!
=========

    Francisco Souza

    f@souza.cc

    `f.souza.cc <http://f.souza.cc>`_
