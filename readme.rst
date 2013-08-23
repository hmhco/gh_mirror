======================
gh_mirror
======================

The goal of the project is to simply mirror an organisations repositories. Using the github API it acquires the details of all organisation repositories and subsequently clones and or updates as required.

Token in the clear:

``gh_mirror -o my_org -t OAUTH-TOKEN -d /data/gh_mirrors``

Token less clear:

``gh_mirror -o my_org -t `cat ~/gh_token` -d /data/gh_mirrors``

Install
--------------

.. code-block::
    
    git clone https://github.com/zircote/gh_mirror.git
    pushd gh_mirror
    python setup.py install
    popd
