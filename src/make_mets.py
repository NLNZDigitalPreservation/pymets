import mets
from lxml import etree as ET
# import xml.etree.ElementTree as ET

mets_document = mets.Mets()

hdr = mets.metsHdr(id='ie1', admid='888', is_horse='true')
agent = mets.Agent(id='agent1')
hdr.root.append(agent.root)
name1 = mets.Name('Homer Simpson')
agent.root.append(name1.root)
note1 = mets.Note('purloined from the Mighty King of Hoegaarden')
agent.root.append(note1.root)

alt_record_id_1 = mets.AltRecordId(ID='11199911', TYPE='Boat registration ID')
hdr.root.append(alt_record_id_1.root)

mets_doc_id_1 = mets.MetsDocumentId(ID='0001-18')
hdr.root.append(mets_doc_id_1.root)


dmd_ie = mets.DmdSec(identifier='ie1')
amd_ie = mets.AmdSec(identifier='ie1')
amd_file = mets.AmdSec(identifier='ie1-rep1-file1')

amd_file_tech = mets.TechMd()
amd_file_tech_mdWrap = mets.MdWrap(mdtype="PREMIS")
amd_file_tech_mdWrap.root.append(mets.XmlData().root)
amd_file_tech.root.append(amd_file_tech_mdWrap.root)
amd_file_tech_mdWrap_dnx = mets.MdWrap(mdtype="OTHER", othermdtype="dnx")
amd_file_tech_mdWrap_dnx.root.append(mets.XmlData().root)

amd_file_tech.root.append(amd_file_tech_mdWrap_dnx.root)
amd_file.root.append(amd_file_tech.root)

amd_file_digiprov = mets.DigiprovMd()
amd_file_digiprov_wrap = mets.MdWrap(mdtype="PREMIS")
amd_file_digiprov_wrap.root.append(mets.XmlData().root)

fileSec = mets.FileSec()
fileGrp = mets.FileGrp(identifier='ie1-rep1', USE="VIEW")
file1 = mets.File(ID="ie1-rep1-file1", MIMETYPE="image/jpeg", ADMID="ie1-rep1-file1-amd")
file1_locat = mets.FLocat(xlin_href="\\\\folder\\file")
file1.root.append(file1_locat.root)
fileGrp.root.append(file1.root)
fileSec.root.append(fileGrp.root)

structMap = mets.StructMap(identifier='ie1-rep1-file1')
bhvrSec = mets.BehaviorSec(identifier='ie1')



mets_document.root.append(hdr.root)
mets_document.root.append(dmd_ie.root)
mets_document.root.append(amd_ie.root)
mets_document.root.append(amd_file.root)
mets_document.root.append(fileGrp.root)
mets_document.root.append(structMap.root)
mets_document.root.append(bhvrSec.root)

# print(ET.tostring(mets_document.root))
print(ET.tostring(mets_document.root, pretty_print=True, encoding='utf-8'))

# another_mets = mets.Mets()
# print(ET.tostring(another_mets))