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

import os

# @given(u'data is available')
# def step_impl(context):
#     assert False
#
# @when(u'user loads the data without providing a config file')
# def step_impl(context):
#     assert False
#
# @then(u'scene is returned')
# def step_impl(context):
#     assert False
#
# @when(u'some items are no available')
# def step_impl(context):
#     assert False
#


@given(u'data is available')
def step_impl(context):
    import urllib2
    if not os.path.exists('/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5'):
        response = urllib2.urlopen('https://zenodo.org/record/16355/files/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5')
        with open('/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5', mode="w") as fp:
            fp.write(response.read())
    if not os.path.exists('/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5'):
        response = urllib2.urlopen('https://zenodo.org/record/16355/files/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5')
        with open('/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5', mode="w") as fp:
            fp.write(response.read())


@when(u'user loads the data without providing a config file')
def step_impl(context):
    from mpop.scene import Scene
    from datetime import datetime
    os.chdir("/tmp/")
    scn = Scene(platform_name="Suomi-NPP", sensor="viirs",
                start_time=datetime(2015, 3, 11, 11, 20),
                end_time=datetime(2015, 3, 11, 11, 26))
    scn.load(["M02"])
    context.scene = scn

@then(u'the data is available in a scene object')
def step_impl(context):
    assert(context.scene["M02"] is not None)
    try:
        context.scene["M01"] is None
        assert(False)
    except KeyError:
        assert(True)

@when(u'some items are no available')
def step_impl(context):
    context.scene.load(["M01"])

@when(u'user wants to know what data is available')
def step_impl(context):
    from mpop.scene import Scene
    from datetime import datetime
    os.chdir("/tmp/")
    scn = Scene(platform_name="Suomi-NPP", sensor="viirs",
                start_time=datetime(2015, 3, 11, 11, 20),
                end_time=datetime(2015, 3, 11, 11, 26))
    from itertools import chain
    available = []
    for reader in scn.readers.values():
        for item in reader.dataset_names:
            available.append(item)
    context.available_datasets = available

@then(u'available datasets is returned')
def step_impl(context):
    assert(len(context.available_datasets) >= 5)


@given(u'data, longitudes and latitudes are available')
def step_impl(context):
    import numpy
    # we have some fancy donut shaped data
    xx, yy = numpy.mgrid[:200, :200]
    circle = (xx - 100) ** 2 + (yy - 100) ** 2
    donut_data = numpy.logical_and(circle < (6400 + 60), circle > (6400 - 60))

    # The data comes from somewhere around Gulf of Finland
    lon_range = numpy.arange(25, 35, 200)
    lat_range = numpy.arange(55, 65, 200)
    lons, lats = numpy.meshgrid(lon_range, lat_range)

    context.lons = lons
    context.lats = lats
    context.data = donut_data

@given(u'area definition is available')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given area definition is available')

@given(u'timestamp is available')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given timestamp is available')


@when(u'user loads the data, coordinates, timestamp and area definition')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user loads the data, coordinates, timestamp and area definition')

@then(u'scene is resampleable')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then scene is resampleable')
