from lxml import etree as ET
# import xml.etree.ElementTree as ET

__version__ = '0.1'

METS_NS = "http://www.loc.gov/METS/"
XLIN_NS = "http://www.w3.org/1999/xlink"

mets_nsmap = {
    'mets': METS_NS,
    }

xlin_nsmap = {
    'xlin': XLIN_NS
}

class Mets(object):
    def __init__(self):
        self.root = ET.Element("{%s}mets" % (METS_NS,), nsmap=mets_nsmap)


# Generic parent classes

# class metsHdr(object):
#     def __init__(self, identifier=None):
#         self.root = ET.Element("{%s}metsHdr" % (METS_NS), nsmap=mets_nsmap)
#         if identifier:
#             self.root.attrib['ID'] = identifier

class metsHdr(object):
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}metsHdr" % (METS_NS), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'ADMID', 'CREATEDATE', 'LASTMODDATE', 'RECORDSTATUS']:
                self.root.attrib[attrib.upper()] = value
            else:
                #TODO: log an exception
                pass
        


class DmdSec(object):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}dmdSec" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class AmdSec(object):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}amdSec" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class StructLink(object):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}structLink" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class StructMap(object):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}structMap" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier


class BehaviorSec(object):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}behaviorSec" % (METS_NS,), nsmap=mets_nsmap)
        if identifier:
            self.root.attrib['ID'] = identifier

# MD extension for parent classes

class MdWrap(object):
    def __init__(self):
        self.root = ET.Element()

# Generic children of MetsHdr Parent
class Agent(object):
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}agent" % (METS_NS,), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'ROLE', 'OTHERROLE', 'TYPE', 'OTHERTYPE']:
                self.root.attrib[attrib.upper()] = value
            else:
                #TODO: log an exception
                pass


class Name(object):
    '''A subelement of Agent. No attributes can be given - only a text value for the element.'''
    def __init__(self, value):
        self.root = ET.Element("{%s}name" % (METS_NS,), nsmap=mets_nsmap)
        self.root.text = value

class Note(object):
    '''A subelement of Agent. No attributes can be given - only a text value for the element.'''
    def __init__(self, value):
        self.root = ET.Element("{%s}name" % (METS_NS,), nsmap=mets_nsmap)
        self.root.text = value

class AltRecordId(object):
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

class MetsDocumentId(object):
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


class MdRef(object):
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


class MdWrap(object):
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


class XmlData(object):
    '''A subelement of MdWrap. Is used to contain XMl data.'''
    def __init__(self):
        self.root = ET.Element("{%s}xmlData" % (METS_NS), nsmap=mets_nsmap)

class BinData(object):
    '''A subelement of MdWrap. Is used to contain base64-encoded binary data.'''
    def __init__(self):
        self.root = ET.Element("{%s}binData" % (METS_NS), nsmap=mets_nsmap)



# Generic children of AMD Parent

class MdExt(object):
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


class FileSec(object):
    def __init__(self):
        self.root = ET.Element("{%s}fileSec" % (METS_NS), nsmap=mets_nsmap)


class FileGrp(object):
    '''A subelement of fileSec. A fileGrp can contain nested fileGrps, 
    or file elements.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}fileGrp" % (METS_NS,), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'VERSDATE', 'ADMID', 'USE']:
                self.root.attrib[attrib.upper()] = value


class File(object):
    '''A subelement of fileGrp. Provides access to the content files for the
    digital object being described by the METS document.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}file" % (METS_NS,), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'SEQ', 'OWNERID', 'ADMID', 'DMDID',
                'GROUPID', 'USE', 'BEGIN', 'END', 'BETYPE']:
                self.root.attrib[attrib.upper()] = value


class FLocat(object):
    '''A subelement of File. Provides a pointer to the location of a content file.
    It uses the XLink reference syntax to provide linking information indicating the 
    actual location of the content file, along with the other attributes specifying
    additional information. NOTE: <FLocat> is an empty element. The location of the
    resource pointed to MUST be stored in the xlink:href attribute.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}FLocat" % (METS_NS), nsmap=xlin_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper in ['ID', 'USE', 'LOCTYPE', 'OTHERLOCTYPE']:
                self.root.attrib[attrib.upper()] = value
            if attrib == "xlin_href":
                self.root.set("{%s}%s" % (XLIN_NS, attrib), value)


class FContent(object):
    '''A subelement of File. It is used to identify a content file contained internally
    within a METS document. It must either be Base64 encoded and contained within the
    subsidiart <binData> wrapper element, or consist of XML information and be contained
    within the subsidiary <xmlData> wrapper element.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}FContent" % (METS_NS), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper in ['ID', 'USE']:
                self.root.attrib[attrib.upper()] = value