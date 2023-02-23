#!/usr/env/python
# -*- python -*-
#
#       Multisetup
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#

#testing buildbot
"""
Multisetup allows to build and install all the packages of OpenAlea
found in this directory.

:Examples:

    # Developer mode : Installation of the packages
    python multisetup.py develop
    python multisetup.py nosetests -w test

    # User mode: Installation of the packages on the system as root
    python multisetup.py install

    # Administrator mode: Create distribution of the packages
    python multisetup.py nosetests -w test install bdist_egg -d ../dist sdist -d ../dist

.. todo::
    - multisetup -h
        * list of the options
"""
import os, sys

from openalea.deploy.multisetup import Multisetup


dirs = """
adel
cn-rhizodep
cn-wheat
elong-wheat
farquhar-wheat
fspm-wheat
growth-wheat
respi-wheat
senesc-wheat
""".split()

def main():

    args = sys.argv[1:]
    if len(args) == 1 and args[0] in ['-h', '--help']:
        Multisetup.help()
    else:
        if 'develop -u' in args:
            dirs.reverse()
        mysetup = Multisetup(curdir='.', commands=args, packages=dirs)
        mysetup.run()


if __name__ == '__main__':
    main()

