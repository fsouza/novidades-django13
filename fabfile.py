# -*- coding: utf-8 -*-
from fabric.api import cd, lcd, env, local, put, roles, run

env.user = 'xikin'
env.presentation_name = 'novidades-django13'
env.url = 'http://p.souza.cc/%(presentation_name)s' % env
env.presentations_directory = '/home/xikin/p.souza.cc'
env.tmp_dir = '/tmp/django13'
env.remote_directory = '%(presentations_directory)s/%(presentation_name)s' % env
env.roledefs = {
    'remote' : ['f.souza.cc',],
}

def clean():
    local('git clean -dfX')

def build():
    clean()
    local('landslide django13.cfg')

def open():
    local('open index.html')

def compress():
    local('mkdir -p %s' % env.tmp_dir)
    local('cp -rv * %s' % env.tmp_dir)
    with lcd(env.tmp_dir):
        local('pyminify index.html > index_minified.html')
        local('mv index_minified.html index.html')
        local('java -jar yuicompressor.jar theme/css/screen.css > theme/css/screen-minified.css')
        local('java -jar yuicompressor.jar theme/css/print.css > theme/css/print-minified.css')
        local('java -jar yuicompressor.jar theme/js/slides.js > theme/js/slides-minified.js')
        local('java -jar yuicompressor.jar theme/js/init.ga.js >> theme/js/slides-minified.js')
        local('sed -i old "s/screen\.css/screen-minified.css/g" index.html')
        local('sed -i old "s/print\.css/print-minified.css/g" index.html')
        local('sed -i old "s/slides\.js/slides-minified.js/g" index.html')

def package():
    build()
    compress()
    with lcd(env.tmp_dir):
        local('tar -czvf /tmp/django13.tar.gz img index.html theme')

@roles('remote')
def deploy():
    package()

    run('mkdir -p %s' % env.remote_directory)
    put('/tmp/django13.tar.gz', env.remote_directory)

    with cd(env.remote_directory):
        run('tar -xvzf django13.tar.gz')
        run('rm -f django13.tar.gz')


    local('rm -rf /tmp/django13*')
    print 'Deployed, check this out: %(url)s' % env

@roles('remote')
def undeploy():
    with cd(env.presentations_directory):
        run('rm -rf %(presentation_name)s' % env)

    print 'Undeployed, the presentation is not live anymore.'
