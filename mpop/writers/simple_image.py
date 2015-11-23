#!/usr/bin/python
# Copyright (c) 2015.
#

# Author(s):
#   Martin Raspaud <martin.raspaud@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
"""

from mpop.writers import Writer


class PillowWriter(Writer):

    def __init__(self, **kwargs):
        Writer.__init__(self, default_config_filename="writers/simple_image.cfg", **kwargs)

    def save_image(self, img, **kwargs):
        filename = kwargs.pop("filename", self.get_filename(**img.info))
        img.save(filename)