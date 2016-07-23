import os
import mets
from lxml import etree as ET
from lxml import isoschematron
# import xml.etree.ElementTree as ET

mets_document = mets.Mets()

# hdr = mets.metsHdr(id='ie1', admid='888', is_horse='true')
# hdr = mets.metsHdr(id='ie1')
hdr = mets.metsHdr(id='ie1', is_horse='true')
hdr.createdate = '2015-05-12 23:49:23'
agent = mets.Agent(id='agent1', role="CREATOR")
hdr.append(agent)
name1 = mets.Name('Homer Simpson')
agent.append(name1)
note1 = mets.Note('purloined from the Mighty King of Hoegaarden')
agent.append(note1)



alt_record_id_1 = mets.AltRecordID(TYPE='Boat registration ID')
alt_record_id_1.text = '009911191'
hdr.append(alt_record_id_1)

mets_doc_id_1 = mets.MetsDocumentId('001.mets', ID='metsDocID-001')
# mets_doc_id_1.text = '001.mets'
hdr.append(mets_doc_id_1)


dmd_ie = mets.DmdSec(ID='ie1-dc')
amd_ie = mets.AmdSec(ID='ie1-amd')
amd_file = mets.AmdSec(ID='ie1-rep1-file1')

amd_file_tech = mets.TechMd(ID='ie1-rep1-file1-amdTech')
amd_file_tech_mdWrap = mets.MdWrap(mdtype="PREMIS")
xmlData_one = mets.XmlData()
prem_one = ET.Element("premisThing")
# amd_file_tech_mdWrap_xmlData.root.append(prem_one)
# xmlData_one.root.append(prem_one)


amd_file_tech_mdWrap.append(mets.XmlData().root)
amd_file_tech.root.append(amd_file_tech_mdWrap)
amd_file_tech_mdWrap_dnx = mets.MdWrap(mdtype="OTHER", othermdtype="dnx")
xml_data_two = mets.XmlData()
dnx_one = ET.Element("dnx")
xml_data_two.root.append(dnx_one)
# amd_file_tech_mdWrap_dnx.root.append(xml_data_two.root)


# amd_file_tech.root.append(amd_file_tech_mdWrap_dnx.root)
amd_file.append(amd_file_tech.root)

amd_file_digiprov = mets.DigiprovMd()
amd_file_digiprov_wrap = mets.MdWrap(mdtype="PREMIS")
amd_file_digiprov_wrap.append(mets.XmlData().root)

fileSec = mets.FileSec()
fileGrp = mets.FileGrp(identifier='ie1-rep1', USE="VIEW")
file1 = mets.File(ID="ie1-rep1-file1", MIMETYPE="image/jpeg", ADMID="ie1-rep1-file1-amd")
file1_locat = mets.FLocat(xlin_href="\\\\folder\\file")
file1.root.append(file1_locat.root)
fileGrp.root.append(file1.root)
fileSec.root.append(fileGrp.root)

structMap = mets.StructMap(identifier='ie1-rep1-file1')
bhvrSec = mets.BehaviorSec(ID='ie1')


# mets_document.root.append(hdr2.root)
mets_document.append(hdr)
mets_document.append(dmd_ie)
mets_document.append(amd_ie)
mets_document.append(amd_file)
mets_document.append(fileGrp.root)
mets_document.append(structMap.root)
mets_document.append(bhvrSec)

# print(ET.tostring(mets_document.root))
print(ET.tostring(mets_document, pretty_print=True, encoding='utf-8'))

# validate xml with schematron
# sch_doc = isoschematron.Schematron(file=os.path.join('.', 'validators',
# 	'mets.stron'), store_report=True)
# validation = sch_doc.validate(mets_document)
# print(validation)
# # if validation == False:
# 	print(sch_doc.validation_report)

# validate cml with mets.xsd
# xmlschema_doc = ET.parse(os.path.join('.', 'validators', 'mets.xsd'))
# xmlschema = ET.XMLSchema(xmlschema_doc)
# # print(xmlschema.validate(mets_document.root))
# print(xmlschema.assert_(mets_document))


# another_mets = mets.Mets()
# print(ET.tostring(another_mets))