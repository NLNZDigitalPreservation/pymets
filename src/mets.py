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

ET.register_namespace('mets', METS_NS)

class Mets(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}mets'

# Generic parent classes

# class metsHdr(object):
#     def __init__(self, identifier=None):
#         self.root = ET.Element("{%s}metsHdr" % (METS_NS), nsmap=mets_nsmap)
#         if identifier:
#             self.root.attrib['ID'] = identifier


def initialise_values(element, attribs_list):
    for key in element.attrib:
        # check if the attribs are lower-case
        if key.upper() in attribs_list and key != key.upper():
            element.attrib[key.upper()] = element.attrib[key]
            del element.attrib[key]
        elif key.upper() not in attribs_list:
            print("WARN: {} not allowed in element {}".format(
                key, element.TAG))
            del element.attrib[key]

class metsHdr(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}metsHdr'

    def _init(self):
        initialise_values(self, ['ID', 'ADMID', 'CREATEDATE', 'LASTMODDATE', 
            'RECORDSTATUS'])

    @property
    def id(self):
        return self.attrib['ID']
    
    @id.setter
    def id(self, value):
        self.attib['ID'] = value
    
    @property
    def admid(self):
        return self.attrib['ADMID']

    @admid.setter
    def admid(self, value):
        self.attrib['ADMID'] = value

    @property
    def createdate(self):
        return self.attrib['CREATEDATE']
    
    @createdate.setter
    def createdate(self, value):
        self.attrib['CREATEDATE'] = value

    @property
    def lastmoddate(self):
        return self.attrib['LASTMODDATE']
    
    @lastmoddate.setter
    def lastmoddate(self, value):
        self.attrib['LASTMODDATE'] = value

    @property
    def recordstatus(self):
        return self.attrib['RECORDSTATUS']
    
    @recordstatus.setter
    def recordstatus(self, value):
        self.attrib['RECORDSTATUS'] = value
    
        

class DmdSec(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}dmdSec'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value
    

class AmdSec(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}amdSec'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value    


# class AmdSec(object):
#     def __init__(self, identifier=None):
#         self.root = ET.Element("{%s}amdSec" % (METS_NS,), nsmap=mets_nsmap)
#         if identifier:
#             self.root.attrib['ID'] = identifier

class BehaviorSec(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}behaviorSec'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value 



# Generic children of MetsHdr Parent
class Agent(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}agent'

    def _init(self):
        initialise_values(self, ['ID', 'ROLE', 'OTHERROLE', 'TYPE', 'OTHERTYPE'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value
    
    @property
    def role(self):
        return self.attrib['ROLE']

    @role.setter
    def role(self, value):
        self.attrib['ROLE'] = value

    @property
    def otherrole(self):
        return self.attrib['OTHERROLE']

    @otherrole.setter
    def otherrole(self, value):
        self.attrib['OTHERROLE'] = value

    @property
    def type(self):
        return self.attrib['TYPE']

    @type.setter
    def type(self, value):
        self.attrib['TYPE'] = value

    @property
    def othertype(self):
        return self.attrib['OTHERTYPE']

    @othertype.setter
    def othertype(self, value):
        self.attrib['OTHERTYPE'] = value


class Name(ET.ElementBase):
    '''A subelement of Agent. No attributes can be given - only a text value for the element.'''
    
    TAG = '{http://www.loc.gov/METS/}name'


class Note(ET.ElementBase):
    '''A subelement of Agent. No attributes can be given - only a text value for the element.'''

    TAG = '{http://www.loc.gov/METS/}note'

# class Note(object):
#     '''A subelement of Agent. No attributes can be given - only a text value for the element.'''
#     def __init__(self, value):
#         self.root = ET.Element("{%s}note" % (METS_NS,), nsmap=mets_nsmap)
#         self.root.text = value

class AltRecordID(ET.ElementBase):
    '''A subelement of metsHdr. Allows one to use alternative record identifier
    values for the digital object represented by the METS document; the primary
    record identifier is stored in the OBJID attribute in the root <mets>
    document.'''

    TAG = '{http://www.loc.gov/METS/}altRecordID'

    def _init(self):
        initialise_values(self, ['ID', 'TYPE'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value

    @property
    def type(self):
        return self.attrib['TYPE']

    @type.setter
    def type(self, value):
        self.attrib['TYPE'] = value
    

class MetsDocumentId(ET.ElementBase):
    '''A subelement of metsHdr. Accepted attributes are ID and TYPE.'''

    TAG = '{http://www.loc.gov/METS/}metsDocumentID'

    def _init(self):
        initialise_values(self, ['ID', 'TYPE'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value

    @property
    def type(self):
        return self.attrib['TYPE']

    @type.setter
    def type(self, value):
        self.attrib['TYPE'] = value


# class MetsDocumentId(object):
#     '''A subelement of metsHdr. Accepted attributes are ID and TYPE.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}metsDocumentID" % (METS_NS,), 
#             nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper() in ['ID', 'TYPE']:
#                 self.root.attrib[attrib.upper()] = value
#             else:
#                 #TODO: log an exception
#                 pass


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

class MdWrap(ET.ElementBase):
    '''A subelement of dmdSec, techMD, rightsMD, sourceMD and digiProvMd. It is
    used to wrap metadata from other schemas, such as PREMIS.'''
    TAG = '{http://www.loc.gov/METS/}mdWrap'

    def _init(self):
        initialise_values(self, ['ID', 'LABEL', 
                    # Metadata attribute group
                    'MDTYPE', 'OTHERMDTYPE', 'MDTYPEVERSION', 'MIMETYPE',
                    'SIZE', 'CREATED', 'CHECKSUM', 'CHECKSUMTYPE'])

# class MdWrap(object):
#     '''A subelement of dmdSec, techMD, rightsMD, sourceMD and digiProvMd. It is
#     used to wrap metadata from other schemas, such as PREMIS.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}mdWrap" % (METS_NS), nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper() in ['ID', 'LABEL', 
#                     # Metadata attribute group
#                     'MDTYPE', 'OTHERMDTYPE', 'MDTYPEVERSION', 'MIMETYPE',
#                     'SIZE', 'CREATED', 'CHECKSUM', 'CHECKSUMTYPE']:
#                 self.root.attrib[attrib.upper()] = value


class XmlData(object):
    '''A subelement of MdWrap or FContent. Is used to contain XMl data.'''
    def __init__(self):
        self.root = ET.Element("{%s}xmlData" % (METS_NS), nsmap=mets_nsmap)

class BinData(object):
    '''A subelement of MdWrap or FContent. Is used to contain base64-encoded binary data.'''
    def __init__(self):
        self.root = ET.Element("{%s}binData" % (METS_NS), nsmap=mets_nsmap)



# Generic children of AMD Parent

class MdExt(object):
    def __init__(self, element=None,  **kwargs):
        self.root = ET.Element("{%s}%s" % (METS_NS, element), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            self.root.attrib[attrib] = value
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
            else:
                #TODO: add exception
                pass


class Stream(object):
    '''A subelement of File. A component byte stream element <stream> may
    be composed of one or more subsidiary streams. An MPEG4 file, for example,
    might contain separate audio and video streams, each of which is
    associated with technical metadata. The repeatable <stream> element
    provides a mechanism to record the existence of separate data streams
    within a particular file, and the opportunity to associate <dmdSec> 
    and <amdSec> with those subsidiary data streams if desired.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}stream" % (METS_NS), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'OWNERID', 'ADMID', 'DMDID', 'BEGIN',
                        'END', 'BETYPE']:
                self.root.attrib[attrib.upper()] = value    
            elif attrib.upper() == 'STREAMTYPE':
                self.root.attrib['streamType'] = value
            else:
                # TODO: add exception
                pass


class TransformFile(object):
    '''A subelement of File. The transform file element <transformFile>
    provides a means to access any subsidiary files listed below a <file>
    element by indicating the steps required to "unpack" or transform the
    subsidiary files. This element is repeatable and might provide a link to a
    <behavior> in the <behaviorSec> that performs the transformation. '''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}transformFile" % (METS_NS), 
            nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'TRANSFORMTYPE', 'TRANSFORMALGORITHM',
                    'TRANSFORMKEY', 'TRANSFORMBEHAVIOR', 'TRANSFORMORDER']:
                self.root.attrib[attrib.upper()] = value
            else:
                # TODO: add exception
                pass


# structMap classes
class StructMap(object):
    '''The structural map section <structMap> is the heart of a METS document.
    It provides a means for organising the digital content represented by the
    <file> elements in the <fileSec> of the METS document into a coherent
    hierarchical structure. Such a hierarchical structure can be presented to
    users to facilitate their comprehension and navigation of the digital 
    content. The structure consists of a series of nested <div> elements. A
    <div> element may directly point to content via <fptr> (file pointer)
    elements or <mptr> (METS pointer) elements.'''
    def __init__(self, **kwargs):
        self.root = ET.Element("{%s}structMap" % (METS_NS,), nsmap=mets_nsmap)
        for attrib, value in kwargs.items():
            if attrib.upper() in ['ID', 'TYPE', 'LABEL']:
                self.root.attrib[attrib.upper()] = value
            else:
                # TOD: add exception
                pass

class Div(object):
    '''A subelement of METS.'''
    def __init__(self, **kwargs):
        self.root