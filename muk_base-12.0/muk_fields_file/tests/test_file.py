###################################################################################
# 
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import os
import logging

from odoo.tests import common

from odoo.addons.muk_fields_file.fields.file import File

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class FileTestCase(common.TransactionCase):
    
    def setUp(self):
        super(FileTestCase, self).setUp()

    def tearDown(self):
        super(FileTestCase, self).tearDown()
        
    def test_import(self):
        self.assertEqual(File.type, "file")
        