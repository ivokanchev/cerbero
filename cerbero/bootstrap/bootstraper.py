# cerbero - a multi-platform build system for Open Source software
# Copyright (C) 2012 Andoni Morales Alastruey <ylatuya@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from cerbero.errors import FatalError
from cerbero.utils import  _


bootstrapers = {}


def register_bootstraper(distro, klass):
    bootstrapers[distro] = klass


class Bootstraper (object):

    def __new__(klass, config):
        bs = {}
        target_distro = config.target_distro
        distro = config.distro

        for dist in [target_distro, distro]:
            if dist not in bootstrapers:
                raise FatalError(_("Not bootstrapper for the distro %s" % dist))
            if dist not in bs:
                bs[dist] = bootstrapers[dist](config)
        return bs.values()


from cerbero.bootstrap import linux, windows

linux.register_all()
windows.register_all()
