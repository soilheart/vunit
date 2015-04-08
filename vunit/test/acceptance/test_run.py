# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2015, Lars Asplund lars.anders.asplund@gmail.com

"""
Run the 'run' VHDL package tests
"""

import unittest
from os.path import join, dirname
from vunit.ui import VUnit
from vunit.test.common import has_modelsim
from vunit import ROOT


@unittest.skipUnless(has_modelsim(), 'Requires modelsim')
class TestRun(unittest.TestCase):
    """
    Run the 'run' VHDL package tests
    """

    def run_sim(self, vhdl_standard):
        """
        Utility function to run the 'run' test compiled with vhdl_standard
        """
        output_path = join(dirname(__file__), "run_out")
        ui = VUnit(clean=True, output_path=output_path,
                   vhdl_standard=vhdl_standard)
        ui.add_library("tb_run_lib")

        vhdl_path = join(ROOT, 'vhdl', 'run')
        ui.add_source_files(join(vhdl_path, 'test', '*.vhd'),
                            "tb_run_lib")
        try:
            ui.main()
        except SystemExit as ex:
            self.assertEqual(ex.code, 0)

    def test_run_vhdl_93(self):
        self.run_sim('93')

    def test_run_vhdl_2002(self):
        self.run_sim('2002')

    def test_run_vhdl_2008(self):
        self.run_sim('2008')
