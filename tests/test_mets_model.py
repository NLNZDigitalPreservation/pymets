from nose.tools import *

from lxml import etree as ET

from pymets import mets_model as mm

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
	print("Testing the generation of a dmdSec element with an attrib key of 'IS_HORSEY...' while in default strict mode")
	dmd_el = mm.DmdSec(IS_HORSEY='true')
	assert(len(dmd_el.attrib) == 0)


def test_dmdsec_stub_with_invalid_parameter_while_strict():
	print("Testing the generation of a dmdSec element with an attrib key of 'IS_HORSEY...' while NOT in default strict mode")
	mm.strict = False
	dmd_el = mm.DmdSec(IS_HORSEY='true')
	assert(len(dmd_el.attrib) == 1)
	# Turn strict back on!
	mm.strict = True


def test_dmdsec_add_id_param_after_init():
	print("Testing adding an id attribute to dmdsec after the element has been created...")
	dmd_el = mm.DmdSec()
	dmd_el.ID = 'ie1'
	assert(dmd_el.attrib['ID'] == 'ie1')