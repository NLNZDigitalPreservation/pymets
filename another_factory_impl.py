import os
from lxml import etree as ET
import pymets.mets_factory as mf

mets_doc = mf.build_mets()

# declare namespaces
DNX_NS = "http://www.exlibrisgroup.com/dps/dnx"
METS_NS = "http://www.loc.gov/METS/"
DC_NS = "http://purl.org/dc/elements/1.1/"
DCTERMS_NS = "http://purl.org/dc/terms/"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
XLIN_NS = "http://www.w3.org/1999/xlink"

mets_nsmap = {
    'mets': METS_NS,
    }
dnx_nsmap = {
    None: DNX_NS
}
dc_nsmap = {
    "dc": DC_NS,
    "dcterms": DCTERMS_NS,
    "xsi": XSI_NS,
}
xlin_nsmap = {
    'xlin': XLIN_NS,
}

# build dmdSec components
# dublin_core = ET.Element("{{dc}}record".format(DC_NS), ns=dc_nsmap)
dublin_core = ET.Element("{%s}record" % (DC_NS,), nsmap=dc_nsmap)
title = ET.SubElement(dublin_core, "{%s}title" % (DC_NS,), nsmap=dc_nsmap)
title.text = "Title of the thing"

dc_mdWrap_attrs = {'MDTYPE': 'DC'}
md_wrap = mf.build_mdWrap(dc_mdWrap_attrs)
md_wrap.append(dublin_core)


dmdSec_attrs = {'ID': 'ie1-dmd'}
dmd_sec = mf.build_dmdSec(dmdSec_attrs, mdRef_list=None, mdWrap_list=[md_wrap])

# print(ET.tostring(dmd_sec))

mets_doc = mf.build_mets() 

mets_doc.append(dmd_sec)
# mets_doc.append(dublin_core)

mf.build_mets_components(mets_doc,
						 ie_id='ie1',
						 ie_dmd=[dublin_core],
						 pres_master_dir=os.path.join('tests', 'test_batch', 'pm'),
						 modified_master_dir=os.path.join('tests', 'test_batch', 'mm'),
						 access_derivative_dir=None,
						 input_dir=os.path.join('tests', 'test_batch'))


print(ET.tostring(mets_doc, pretty_print=True))