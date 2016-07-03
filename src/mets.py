from lxml import etree as ET

__version__ = '0.1'

METS_NS = "http://www.loc.gov/METS/"

mets_nsmap = {
    'mets': METS_NS,
    }


class Mets:
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


class FileGrp(object):
    def __init__(self, identifier=None):
        self.root = ET.Element("{%s}fileGrp" % (METS_NS,), nsmap=mets_nsmap)
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


class mdRef(object):
    '''A subelement of dmdSec, techMd, rightsMD, sourceMD and
    digiProvMD. Accepted attributes are ID, LABEL, XPTR, or the
    Location attributes LOCTYPE or OTHERLOCTYPE.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}mdRef" % (METS_NS), 
            nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'LABEL', 'XPTR', 'LOCTYPE',
                        'OTHERLOCTYPE']:
                self.root.attrib[attrib.upper()] = value
                if attrib.upper() == 'LOCTYPE':
                    if value in ['ARK', 'URN', 'URL', 'PURL', 'HANDLE', 
                        'DOI', 'OTHER']:
                        self.root.attrib.upper() = value
                    else:
                        #TODO: log an exception
            else:
                #TODO: log an exception
                pass

# Generic children of AMD Parent

class TechMd(object):
    def __init__(self, **kwargs):
        super(TechMd, self).__init__(md_type="techMD", **kwargs)


class RightsMd(object):
    def __init__(self, **kwargs):
        super(RightsMd, self).__init__(md_type="rightsMD", **kwargs)


class SourceMd(object):
    def __init__(self, **kwargs):
        super(SourceMd, self).__init__(md_type="sourceMD", **kwargs)


class DigiprovMd(object):
    def __init__(self, **kwargs):
        super(DigiprovMd, self).__init__(md_type="digiprovMD", **kwargs)