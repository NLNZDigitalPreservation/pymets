from lxml import etree as ET
# import xml.etree.ElementTree as ET

__version__ = '0.1'

METS_NS = "http://www.loc.gov/METS/"

mets_nsmap = {
    'mets': METS_NS,
    }


class XmlElement(object):
    def __init__(self):
        self.root = None
    def __repr__(self):
        return self.root


class Mets(XmlElement):
    def __init__(self):
        self.root = ET.Element("{%s}mets" % (METS_NS,), nsmap=mets_nsmap)


# Generic parent classes

# class metsHdr(object):
#     def __init__(self, identifier=None):
#         self.root = ET.Element("{%s}metsHdr" % (METS_NS), nsmap=mets_nsmap)
#         if identifier:
#             self.root.attrib['ID'] = identifier

class metsHdr(XmlElement):
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}metsHdr" % (METS_NS), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'ADMID', 'CREATEDATE', 'LASTMODDATE', 'RECORDSTATUS']:
                self.root.attrib[attrib.upper()] = value
            else:
                #TODO: log an exception
                pass
        


class DmdSec(XmlElement):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}dmdSec" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class AmdSec(XmlElement):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}amdSec" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class StructLink(XmlElement):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}structLink" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class StructMap(XmlElement):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}structMap" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class BehaviorSec(XmlElement):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}behaviorSec" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier

# MD extension for parent classes

class MdWrap(XmlElement):
    def __init__(self):
        self.root = ET.Element()

# Generic children of MetsHdr Parent
class Agent(XmlElement):
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}agent" % (METS_NS,), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'ROLE', 'OTHERROLE', 'TYPE', 'OTHERTYPE']:
                self.root.attrib[attrib.upper()] = value
            else:
                #TODO: log an exception
                pass


class Name(XmlElement):
    '''A subelement of Agent. No attributes can be given - only a text value for the element.'''
    def __init__(self, value):
        self.root = ET.Element("{%s}name" % (METS_NS,), nsmap=mets_nsmap)
        self.root.text = value

class Note(XmlElement):
    '''A subelement of Agent. No attributes can be given - only a text value for the element.'''
    def __init__(self, value):
        self.root = ET.Element("{%s}name" % (METS_NS,), nsmap=mets_nsmap)
        self.root.text = value

class AltRecordId(XmlElement):
    '''A subelement of metsHdr. Accepts no attributes - only an element value.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}altRecordId" % (METS_NS,), 
            nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'TYPE']:
                self.root.attrib[attrib.upper()] = value
            else:
                #TODO: log an exception
                pass

class MetsDocumentId(XmlElement):
    '''A subelement of metsHdr. Accepted attributes are ID and TYPE.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}metsDocumentID" % (METS_NS,), 
            nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'TYPE']:
                self.root.attrib[attrib.upper()] = value
            else:
                #TODO: log an exception
                pass


class MdRef(XmlElement):
    '''A subelement of dmdSec, techMd, rightsMD, sourceMD and
    digiProvMD. Accepted attributes are ID, LABEL, XPTR, or the
    Location attributes LOCTYPE or OTHERLOCTYPE.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}mdRef" % (METS_NS), 
            nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'LABEL', 'XPTR', 
                        # Metadata attribute group
                        'MDTYPE', 'OTHERMDTYPE','MDTYPEVERSION',
                        # File Core attribute group
                        'MIMETYPE', 'SIZE', 'CREATED', 'CHECKSUM',
                        'CHECKSUMTYPE']:
                self.root.attrib[attrib.upper()] = value
            if attrib.upper() == 'LOCTYPE':
                if value in ['ARK', 'URN', 'URL', 'PURL', 'HANDLE', 
                    'DOI', 'OTHER']:
                    self.root.attrib[attrib.upper()] = value 
                else:
                    #TODO: log an exception
                    pass


class MdWrap(XmlElement):
    '''A subelement of dmdSec, techMD, rightsMD, sourceMD and digiProvMd. It is
    used to wrap metadata from other schemas, such as PREMIS.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}mdWrap" % (METS_NS), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'LABEL', 
                    # Metadata attribute group
                    'MDTYPE', 'OTHERMDTYPE', 'MDTYPEVERSION', 'MIMETYPE',
                    'SIZE', 'CREATED', 'CHECKSUM', 'CHECKSUMTYPE']:
                self.root.attrib[attrib.upper()] = value


class XmlData(XmlElement):
    '''A subelement of MdWrap. Is used to contain XMl data.'''
    def __init__(self):
        self.root = ET.Element("{%s}xmlData" % (METS_NS), nsmap=mets_nsmap)

class BinData(XmlElement):
    '''A subelement of MdWrap. Is used to contain base64-encoded binary data.'''
    def __init__(self):
        self.root = ET.Element("{%s}binData" % (METS_NS), nsmap=mets_nsmap)



# Generic children of AMD Parent

class MdExt(XmlElement):
    def __init__(self, element=None,  **kwargs):
        self.root = ET.Element("{%s}%s" % (METS_NS, element), nsmap=mets_nsmap)
        # self.mdWrap = ET.SubElement(self.root,
        #     "{%s}mdWrap" % METS_NS, MDTYPE="OTHER", OTHERMDTYPE="dnx")

class TechMd(MdExt):
    def __init__(self, **kwargs):
        super(TechMd, self).__init__(element="techMD", **kwargs)


class RightsMd(MdExt):
    def __init__(self, **kwargs):
        super(RightsMd, self).__init__(element="rightsMD", **kwargs)


class SourceMd(MdExt):
    def __init__(self, **kwargs):
        super(SourceMd, self).__init__(element="sourceMD", **kwargs)


class DigiprovMd(MdExt):
    def __init__(self, **kwargs):
        super(DigiprovMd, self).__init__(element="digiprovMD", **kwargs)


# fileSec classes


class FileSec(XmlElement):
    def __init__(self):
        self.root = ET.Element("{%s}fileSec" % (METS_NS), nsmap=mets_nsmap)


class FileGrp(XmlElement):
    '''A subelement of fileSec. A fileGrp can contain nested fileGrps, 
    or file elements.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}fileGrp" % (METS_NS,), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'VERSDATE', 'ADMID', 'USE']:
                self.root.attrib[attrib.upper()] = value


class File(XmlElement):
    '''A subelement of fileGrp. Provides access to the content files for the
    digital object being described by the METS document.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}file" % (METS_NS,), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'SEQ', 'OWNERID', 'ADMID', 'DMDID',
                'GROUPID', 'USE', 'BEGIN', 'END', 'BETYPE']:
                self.root.attrib[attrib.upper()] = value