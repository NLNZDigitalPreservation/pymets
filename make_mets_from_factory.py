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
t1_binData_list = ['BINARYBASE64NOTREALLY', 'THINGS999OTHERTHINGSB64']
t1_mdWrap_attrs = {'MDTYPE': 'OTHER', 'OTHERMDTYPE': 'arbitrary_md'}
tech_mdwrap = mf.build_mdWrap(t1_mdWrap_attrs, binData_list=t1_binData_list)
tech_MD_attrs = {'ID': 'ie1-amd1-tech1'}
techMd = mf.build_techMD(tech_MD_attrs, mdRef_list=None, mdWrap_list=[tech_mdwrap])

amdSec.append(techMd)

# print(ET.tostring(mdWrap))
print(ET.tostring(mets, pretty_print=True)) 