# This Python file uses the following encoding: utf-8
import os

import sys

from nose.tools import *
from lxml import etree as ET

from pymets import mets_model as mm

CURRENT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I ran!")


def test_mets_stub():
    print("Testing the generation of a Mets element...")
    mets_doc = mm.Mets()
    assert(mets_doc.tag == '{http://www.loc.gov/METS/}mets')


def test_dmdsec_stub():
    print("Testing the generation of a dmdSec element with an ID attrib...")
    dmd_el = mm.DmdSec(ID='ie1')
    assert(dmd_el.attrib['ID'] == 'ie1')


def test_dmdsec_stub_with_invalid_parameter_while_strict():
    print("Testing the generation of a dmdSec element with an attrib key of" + 
        " 'IS_HORSEY...' while in default strict mode")
    dmd_el = mm.DmdSec(IS_HORSEY='true')
    assert(len(dmd_el.attrib) == 0)


def test_dmdsec_stub_with_invalid_parameter_while_strict():
    print("Testing the generation of a dmdSec element with an attrib key of" +
        " 'IS_HORSEY...' while NOT in default strict mode")
    mm.strict = False
    dmd_el = mm.DmdSec(IS_HORSEY='true')
    assert(len(dmd_el.attrib) == 1)
    # Turn strict back on!
    mm.strict = True


def test_dmdsec_add_id_param_after_init():
    print("Testing adding an id attribute to dmdsec after the element has" +
        " been created...")
    dmd_el = mm.DmdSec()
    dmd_el.ID = 'ie1'
    assert(dmd_el.attrib['ID'] == 'ie1')


def test_metshdr_tag():
    metshdr = mm.MetsHdr()
    assert(metshdr.tag == '{http://www.loc.gov/METS/}metsHdr')

def test_metshdr_tag():
    metshdr = mm.MetsHdr()
    assert(metshdr.tag == '{http://www.loc.gov/METS/}metsHdr')


def test_metshdr_attrs():
    metshdr = mm.MetsHdr(ID='ie1', ADMID='ie1-amd', CREATEDATE='2016-06-01',
        LASTMODDATE='2016-06-03', IS_HORSEY='false')
    # assert(metshdr.tag == '{http://www.loc.gov/METS/}metsHdr')
    metshdr.RECORDSTATUS = 'ACTIVE'
    print("attrib length is {}".format(len(metshdr.attrib)))
    assert(len(metshdr.attrib)) == 5

def test_amdsec_tag():
    amdsec = mm.AmdSec()
    assert(amdsec.tag == '{http://www.loc.gov/METS/}amdSec')

def test_amdsec_attrs():
    amdsec = mm.AmdSec(ID="ie1")
    assert(amdsec.attrib['ID'] == "ie1")
    print("Now updating the ID attrib!")
    amdsec.ID = 'rep1'
    assert(amdsec.attrib['ID'] == "rep1")

def test_FLocat_tag():
    flocat = mm.FLocat()
    assert(flocat.tag == '{http://www.loc.gov/METS/}FLocat')


# Test METS methods

def test_mets_write():
    """Ensure that Mets.write() is able to be written to a file."""
    mets = mm.Mets()
    # Fill with some stuff
    dmd_el = mm.DmdSec(ID='ie1')
    mets.append(dmd_el)
    output_files = os.listdir(os.path.join(CURRENT_DIR, 'data', 'output'))
    if len(output_files) != 0:
        for item in output_files:
            os.remove(os.path.join(CURRENT_DIR, 'data', 'output', item))
    mets.write(os.path.join(CURRENT_DIR, 'data', 'output', 'mets.xml'))

def test_mets_tounicode():
    """Ensure that Mets.tounicode() is working"""
    mets = mm.Mets()
    # Fill with some stuff
    dmd_el = mm.DmdSec(ID='ie1')
    mets.append(dmd_el)
    assert(mets.tounicode().startswith('<mets:mets'))

def test_mets_write_with_utf8():
    """Ensure that Mets.write() is able to be written to a file with utf8"""
    mets = mm.Mets()
    # Fill with some stuff
    dmd_el = mm.DmdSec(ID='ie1')
    mets.append(dmd_el)
    output_files = os.listdir(os.path.join(CURRENT_DIR, 'data', 'output'))
    if len(output_files) != 0:
        for item in output_files:
            os.remove(os.path.join(CURRENT_DIR, 'data', 'output', item))
    mets.write(os.path.join(CURRENT_DIR, 'data', 'output', 'mets.xml'),
        encoding='UTF-8')

def test_mets_write_with_cp_1252():
    """Ensure that Mets.write() is able to be written to a file with cp1252"""
    mets = mm.Mets()
    # Fill with some stuff
    dmd_el = mm.DmdSec(ID='ie1')
    mets.append(dmd_el)
    output_files = os.listdir(os.path.join(CURRENT_DIR, 'data', 'output'))
    if len(output_files) != 0:
        for item in output_files:
            os.remove(os.path.join(CURRENT_DIR, 'data', 'output', item))
    mets.write(os.path.join(CURRENT_DIR, 'data', 'output', 'mets.xml'),
        encoding='cp1252')

def test_mets_write_with_utf8_with_macron():
    """check Mets.write() with utf8 with macron in document"""
    print("trying to do the macron thing!")
    print(sys.version)
    mets = mm.Mets()
    # Fill with some stuff
    dmd_el = mm.DmdSec(ID='ie1')
    dmd_el.text = u'māori'
    mets.append(dmd_el)
    output_files = os.listdir(os.path.join(CURRENT_DIR, 'data', 'output'))
    if len(output_files) != 0:
        for item in output_files:
            os.remove(os.path.join(CURRENT_DIR, 'data', 'output', item))
    mets.write(os.path.join(CURRENT_DIR, 'data', 'output', 'mets.xml'),
        encoding='UTF-8')


def test_TechMD_object_returns_correct_warning():
    """prints invalid 'tag' attribute, rather than trying to print 'TAG' attribute"""
    tech_md = mm.TechMd(ID="IE1", TYPE="Not a thing")
    print(tech_md.attrib)
    assert("TYPE" not in tech_md.attrib)
    assert("ID" in tech_md.attrib)