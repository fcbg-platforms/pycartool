# -*- coding: utf-8 -*-
# Authors: Victor Férat <victor.ferat@live.fr>
#
# License: BSD (3-clause)

import os

from pycartool.data import data_path
from pycartool.rois.regions_of_interest import read_roi


def test_read_roi():
    """Test read_roi"""
    file_path = os.path.join(data_path, "sample_test_roi.rois")
    rois = read_roi(file_path)
    assert len(rois.names) == 32
    assert len(rois.groups_of_indexes) == 32
