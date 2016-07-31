
import os
from lxml import etree as ET
import pymets.mets_factory as mf

mets = mf.build_mets()


# build dmdSec components
binData_list = ['eruweyr8r239484h8r932309eu2oj878yy49r4', 'd3892ud894hd4fhouy87y743']
mdWrap_attrs = {'MDTYPE': 'OTHER', 'OTHERMDTYPE': 'arbitrary_md'}
mdWrap = mf.build_mdWrap(mdWrap_attrs, binData_list=binData_list)
dmdSec_attrs = {'ID': 'ie1-dmd1'}
dmdSec = mf.build_dmdSec(dmdSec_attrs, mdRef_list=None, mdWrap_list=[mdWrap])
mets.append(dmdSec)


# build amdSec components
amdSec_attrs = {'ID': 'ie1-amd1'}
amdSec = mf.build_amdSec(amdSec_attrs)
mets.append(amdSec)


# build techMd components
# start off with binData
t1_binData_list = ['BINARYBASE64NOTREALLY', 'THINGS999OTHERTHINGSB64']

# Now build some dnx
fake_dnx_xml = ET.Element("dnx")
t2_mdWrap_attrs = {'MDTYPE': 'OTHER', 'OTHERMDTYPE': 'dnx'}
tech_mdwrap_2 = mf.build_mdWrap(t2_mdWrap_attrs, xmlData_list=[fake_dnx_xml])

t1_mdWrap_attrs = {'MDTYPE': 'OTHER', 'OTHERMDTYPE': 'arbitrary_md'}
tech_mdwrap = mf.build_mdWrap(t1_mdWrap_attrs, binData_list=t1_binData_list, xmlData_list=None)


tech_MD_attrs = {'ID': 'ie1-amd1-tech1'}
techMd = mf.build_techMD(tech_MD_attrs, mdRef_list=None, mdWrap_list=[tech_mdwrap, tech_mdwrap_2])

amdSec.append(techMd)


# build Structure Map
# struct_map = mf.build_structMap(structMap_attrs)
# amdSec.append(techMd)
filegrp_dict = []

flgrp1 = mf.generate_flgrp_details_and_structmap(mets=mets, 
	rep_directory_path=os.path.join('tests', 'data', 'test_batch_1', 'pm'), 
	rep_id='ie1-rep1', 
	pres_type='PRESERVATION_MASTER', 
	input_dir=os.path.join('tests', 'data', 'test_batch'))
filegrp_dict.append(flgrp1)

flgrp2 = mf.generate_flgrp_details_and_structmap(mets=mets, 
	rep_directory_path=os.path.join('tests', 'data', 'test_batch_1', 'mm'), 
	rep_id='ie1-rep2', 
	pres_type='MODIFIED_MASTER', 
	input_dir=os.path.join('tests', 'data', 'test_batch_1'))
filegrp_dict.append(flgrp2)

# print(filegrp_dict)

fileSec = mf.build_fileSec(filegrp_dict)

mets.append(fileSec)


# print(ET.tostring(mdWrap))
print(ET.tostring(mets, pretty_print=True)) 