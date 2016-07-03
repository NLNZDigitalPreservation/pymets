import mets
from lxml import etree as ET

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


dmd = mets.DmdSec(identifier='ie1')
amd = mets.AmdSec(identifier='ie1')
amd = mets.AmdSec(identifier='ie1-rep1-file1')
fileGrp = mets.FileGrp(identifier='ie1-rep1-file1')
structMap = mets.StructMap(identifier='ie1-rep1-file1')
bhvrSec = mets.BehaviorSec(identifier='ie1')



mets_document.root.append(hdr.root)
mets_document.root.append(dmd.root)
mets_document.root.append(amd.root)
mets_document.root.append(fileGrp.root)
mets_document.root.append(structMap.root)
mets_document.root.append(bhvrSec.root)

print(ET.tostring(mets_document.root,pretty_print=True))