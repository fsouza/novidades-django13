Novidades do Django 1.3
=======================

    Francisco Souza

    @franciscosouza

------------------------

Class Based Views
=================

.fx: build-code

* Views agora são classes...
* Herança
* Mixins

.. sourcecode:: python

    class HelloWorldView(View):

        def get(self):
            return HttpResponse("Hello world")

------------------------

Obrigado!
=========

    Francisco Souza

    f@souza.cc

    `f.souza.cc <http://f.souza.cc>`_
