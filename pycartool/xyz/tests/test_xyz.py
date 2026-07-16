# -*- coding: utf-8 -*-
# Authors: Victor Férat <victor.ferat@live.fr>
#
# License: BSD (3-clause)
import os

import mne
from mne.channels import DigMontage

from pycartool.data import data_path
from pycartool.xyz import read_xyz, write_xyz


def test_read_xyz():
    """Test read_xyz."""
    file_path = os.path.join(data_path, "EGI257.GenevaAverage13.10-10.xyz")
    montage = read_xyz(file_path)
    assert isinstance(montage, DigMontage)

def test_write_xyz(tmp_path):
    """Test write_xyz."""
    file_path = os.path.join(data_path, "EGI257.GenevaAverage13.10-10.xyz")
    montage = read_xyz(file_path)
    info = mne.create_info(ch_names=montage.ch_names, sfreq=1000, ch_types="eeg")
    info.set_montage(montage)
    write_xyz(tmp_path / "test.xyz", info)
    assert os.path.exists(tmp_path / "test.xyz")
    # check same file content
    montage_read = read_xyz(tmp_path / "test.xyz")
    assert montage_read == montage
