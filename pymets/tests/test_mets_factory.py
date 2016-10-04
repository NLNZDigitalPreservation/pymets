from nose.tools import *
from lxml import etree as ET

from pymets import mets_factory as mf
import os

nsmap = {"dnx"}

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I ran!")

def test_build_amdsec_filegrp_structmap():
    mets = mf.build_mets()
    mf.build_amdsec_filegrp_structmap(mets,
        ie_id='ie1',
        pres_master_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)),'data', 'test_batch_1', 'pm'),
        modified_master_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'test_batch_1', 'mm'),
        access_derivative_dir=None,
        digital_original=False,
        input_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'test_batch_1'))
    amd_sec_list = mets.findall("./{http://www.loc.gov/METS/}amdSec")
    print("Here is the list of amdSec items: {}".format(amd_sec_list))
    assert(len(amd_sec_list) == 4)
    print(ET.tostring(mets, pretty_print=True))