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

ET.register_namespace('xlin', XLIN_NS)

STRICT = True


def initialise_values(element, attribs_list):
    for key in element.attrib:
        if key in attribs_list:
            if key == 'xlin_href':
                element.set("{%s}%s" % (XLIN_NS, 'href'), element.attrib[key])
            del element.attrib[key]
        elif key not in attribs_list:
            print("WARN: {} not allowed in element {}".format(
                key, element.TAG))
            if STRICT:
                del element.attrib[key]
        # # check if the attribs are lower-case
        # if key.upper() in attribs_list and key != key.upper():
        #     element.attrib[key.upper()] = element.attrib[key]
        #     del element.attrib[key]
        # elif key.upper() not in attribs_list:
        #     print("WARN: {} not allowed in element {}".format(
        #         key, element.TAG))
        #     del element.attrib[key]


class Mets(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}mets'

# Generic parent classes

# class metsHdr(object):
#     def __init__(self, identifier=None):
#         self.root = ET.Element("{%s}metsHdr" % (METS_NS), nsmap=mets_nsmap)
#         if identifier:
#             self.root.attrib['ID'] = identifier


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


class MdRef(ET.ElementBase):
    '''The metadata reference element <mdRef> element is a generic element
    used throughout the METS schema to provide a pointer to metadata which
    resides outside the METS document. NB: <mdRef> is an empty element. The
    location of the metadata must be recorded in the xlink:href attribute,
    supplemented by the XPTR attribute as needed.'''
    TAG = '{http://www.loc.gov/METS/}mdRef'

    def __init__(self):
        initialise_values(self, ['ID', 'LABEL', 'XPTR', 'MDTYPE',
            'OTHERMDTYPE', 'MDTYPEVERSION', 'MIMETYPE', 'SIZE', 'CREATED',
            'CHECKSUM', 'CHECKSUMTYPE'])
        for value in self.attrib:
            if attrib.upper() == 'LOCTYPE':
                initialise_values(self, ['ARK', 'URN', 'URL', 'PURL', 
                    'HANDLE', 'DOI', 'OTHER'])


class MdWrap(ET.ElementBase):
    '''A subelement of dmdSec, techMD, rightsMD, sourceMD and digiProvMd. It is
    used to wrap metadata from other schemas, such as PREMIS.'''
    TAG = '{http://www.loc.gov/METS/}mdWrap'

    def _init(self):
        initialise_values(self, ['ID', 'LABEL', 
                    # Metadata attribute group
                    'MDTYPE', 'OTHERMDTYPE', 'MDTYPEVERSION', 'MIMETYPE',
                    'SIZE', 'CREATED', 'CHECKSUM', 'CHECKSUMTYPE'])


class XmlData(ET.ElementBase):
    '''The xml data wrapper element <xmlData> is used to contain XML encoded
    metadata. The content of an <xmlData> element can be in any namespace or
    in no namespace. As permitted by the XML Schema Standard, the 
    processContents attribute value for the metadata in an <xmlData> is set to
    "lax". Therefore, if the source schema and its location are identified by
    means of an XML schemaLocation attribute, then an XML processor will 
    validate the elements for which it can find declarations. If a source schema
    is not identified, or cannot be found at the specified schemaLocation, then
    an XML validator will check for well-formedness, but otherwise skip over
    the elements appearing in the <xmlData> element.'''

    TAG = '{http://www.loc.gov/METS/}xmlData'


class BinData(ET.ElementBase):
    '''The binary data wrapper element <binData> is used to contain Base64
    encoded metadata.'''

    TAG = '{http://www.loc.gov/METS/}xmlData'

# class BinData(object):
#     '''A subelement of MdWrap or FContent. Is used to contain base64-encoded binary data.'''
#     def __init__(self):
#         self.root = ET.Element("{%s}binData" % (METS_NS), nsmap=mets_nsmap)



# Generic children of AMD Parent

class MdExt(ET.ElementBase):
    '''Generic parent class of techMd, rightsMD, sourceMD and digiprovMd. Not
    intended to be called directly.'''

    def _init(self, element_name=None):
        self.TAG = '{http://www.loc.gov/METS/}' + element_name
        initialise_values(self, ['ID', 'ADMID', 'CREATED', 'STATUS'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value
    
    @property
    def admid(self):
        return self.attrib['ADMID']

    @admid.setter
    def admid(self, value):
        self.attrib['ADMID'] = value

    @property
    def created(self):
        return self.attrib['CREATED']

    @created.setter
    def created(self, value):
        self.attrib['CREATED'] = value

    @property
    def status(self):
        return self.attrib['STATUS']

    @status.setter
    def status(self, value):
        self.attrib['STATUS'] = value
    
    


# class MdExt(object):
#     def __init__(self, element=None,  **kwargs):
#         self.root = ET.Element("{%s}%s" % (METS_NS, element), nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             self.root.attrib[attrib] = value
        # self.mdWrap = ET.SubElement(self.root,
        #     "{%s}mdWrap" % METS_NS, MDTYPE="OTHER", OTHERMDTYPE="dnx")


class TechMd(MdExt):
    def _init(self, **kwargs):
        super(TechMd, self)._init("techMD", **kwargs)

# class TechMd(MdExt):
#     def __init__(self, **kwargs):
#         super(TechMd, self).__init__(element="techMD", **kwargs)


class RightsMd(MdExt):
    def _init(self, **kwargs):
        super(RightsMd, self)._init("rightsMD",**kwargs)

# class RightsMd(MdExt):
#     def __init__(self, **kwargs):
#         super(RightsMd, self).__init__(element="rightsMD", **kwargs)


class SourceMd(MdExt):
    def _init(self, **kwargs):
        super(SourceMd, self)._init("sourceMD", **kwargs)

# class SourceMd(MdExt):
#     def __init__(self, **kwargs):
#         super(SourceMd, self).__init__(element="sourceMD", **kwargs)

class DigiprovMd(MdExt):
    def _init(self, **kwargs):
        super(DigiprovMd, self)._init("digiprovMD", **kwargs)

# class DigiprovMd(MdExt):
#     def __init__(self, **kwargs):
#         super(DigiprovMd, self).__init__(element="digiprovMD", **kwargs)


# fileSec classes


class FileSec(ET.ElementBase):
    '''The overall purpose of the content file section element <fileSec> is to
    provide an inventory of and the location for the content files that
    comprise the digital object being described in the METS document. '''
    TAG = '{http://www.loc.gov/METS/}fileSec'

# class FileSec(object):
#     def __init__(self):
#         self.root = ET.Element("{%s}fileSec" % (METS_NS), nsmap=mets_nsmap)


class FileGrp(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}fileGrp'

    def _init(self):
        initialise_values(self, ['ID', 'VERSDATE', 'ADMID', 'USE'])

# class FileGrp(object):
#     '''A subelement of fileSec. A fileGrp can contain nested fileGrps, 
#     or file elements.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}fileGrp" % (METS_NS,), nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper() in ['ID', 'VERSDATE', 'ADMID', 'USE']:
#                 self.root.attrib[attrib.upper()] = value


class File(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}file'

    def _init(self):
        initialise_values(self, ['ID', 'SEQ', 'OWNERID', 'ADMID', 'DMDID',
                'GROUPID', 'USE', 'BEGIN', 'END', 'BETYPE'])

    @property
    def id(self):
        return self.attrib['ID']

    @id.setter
    def id(self, value):
        self.attrib['ID'] = value

    @property
    def seq(self):
        return self.attrib['SEQ']

    @seq.setter
    def seq(self, value):
        self.attrib['SEQ'] = value

    @property
    def ownerid(self):
        return self.attrib['OWNERID']

    @ownerid.setter
    def ownerid(self, value):
        self.attrib['OWNERID'] = value

    @property
    def admid(self):
        return self.attrib['ADMID']

    @admid.setter
    def admid(self, value):
        self.attrib['ADMID'] = value

    @property
    def dmdid(self):
        return self.attrib['DMDID']

    @dmdid.setter
    def dmdid(self, value):
        self.attrib['DMDID'] = value

    @property
    def use(self):
        return self.attrib['USE']

    @use.setter
    def use(self, value):
        self.attrib['USE'] = value

    @property
    def begin(self):
        return self.attrib['BEGIN']

    @begin.setter
    def begin(self, value):
        self.attrib['BEGIN'] = value

    @property
    def end(self):
        return self.attrib['END']

    @end.setter
    def end(self, value):
        self.attrib['END'] = value

    @property
    def betype(self):
        return self.attrib['BETYPE']

    @betype.setter
    def end(self, value):
        self.attrib['BETYPE'] = value
    

# class File(object):
#     '''A subelement of fileGrp. Provides access to the content files for the
#     digital object being described by the METS document.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}file" % (METS_NS,), nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper() in ['ID', 'SEQ', 'OWNERID', 'ADMID', 'DMDID',
#                 'GROUPID', 'USE', 'BEGIN', 'END', 'BETYPE']:
#                 self.root.attrib[attrib.upper()] = value


class FLocat(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}FLocat'

    def _init(self):
        initialise_values(self, ['ID', 'USE', 'LOCTYPE', 'OTHERLOCTYPE', 'xlin_href'])
        


# class FLocat(object):
#     '''A subelement of File. Provides a pointer to the location of a content file.
#     It uses the XLink reference syntax to provide linking information indicating the 
#     actual location of the content file, along with the other attributes specifying
#     additional information. NOTE: <FLocat> is an empty element. The location of the
#     resource pointed to MUST be stored in the xlink:href attribute.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}FLocat" % (METS_NS), nsmap=xlin_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper in ['ID', 'USE', 'LOCTYPE', 'OTHERLOCTYPE']:
#                 self.root.attrib[attrib.upper()] = value
#             if attrib == "xlin_href":
#                 self.root.set("{%s}%s" % (XLIN_NS, attrib), value)


class FContent(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}FContent'

    def _init(self):
        initialise_values(self, ['ID', 'USE'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def USE(self):
        return self.attrib['USE']

    @USE.setter
    def USE(self, value):
        self.attrib['USE'] = value
    

# class FContent(object):
#     '''A subelement of File. It is used to identify a content file contained internally
#     within a METS document. It must either be Base64 encoded and contained within the
#     subsidiart <binData> wrapper element, or consist of XML information and be contained
#     within the subsidiary <xmlData> wrapper element.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}FContent" % (METS_NS), nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper in ['ID', 'USE']:
#                 self.root.attrib[attrib.upper()] = value
#             else:
#                 #TODO: add exception
#                 pass


class Stream(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}stream'

    def _init(self):
        # "streamType" is something of an anomaly here, as it is the only
        # attribute whose spelling is in camelCase. as such, we should case
        # for if it is supplied in upper-case
        for attrib_value in self.attrib:
            if attrib_value == 'STREAMTYPE':
                self.attrib['streamType'] = self.attrib[attrib_value]
                del self.attrib[attrib_value
                ]
        initialise_values(self, ['ID', 'OWNERID', 'ADMID', 'DMDID', 'BEGIN',
                        'END', 'BETYPE', 'streamType'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    
    @property
    def OWNERID(self):
        return self.attrib['OWNERID']

    @OWNERID.setter
    def OWNERID(self, value):
        self.attrib['OWNERID'] = value
    
    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @ADMID.setter
    def ADMID(self, value):
        self.attrib['ADMID'] = value

    @property
    def DMDID(self):
        return self.attrib['DMDID']

    @DMDID.setter
    def DMDID(self, value):
        self.attrib['DMDID'] = value

    @property
    def BEGIN(self):
        return self.attrib['BEGIN']

    @BEGIN.setter
    def BEGIN(self, value):
        self.attrib['BEGIN'] = value

    @property
    def END(self):
        return self.attrib['END']

    @END.setter
    def END(self, value):
        self.attrib['END'] = value

    @property
    def BETYPE(self):
        return self.attrib['BETYPE']

    @BETYPE.setter
    def BETYPE(self, value):
        self.attrib['BETYPE'] = value

    @property
    def streamType(self):
        return self.attrib['streamType']

    @streamType.setter
    def streamType(self, value):
        self.attrib['streamType'] = value

# class Stream(object):
#     '''A subelement of File. A component byte stream element <stream> may
#     be composed of one or more subsidiary streams. An MPEG4 file, for example,
#     might contain separate audio and video streams, each of which is
#     associated with technical metadata. The repeatable <stream> element
#     provides a mechanism to record the existence of separate data streams
#     within a particular file, and the opportunity to associate <dmdSec> 
#     and <amdSec> with those subsidiary data streams if desired.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}stream" % (METS_NS), nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper() in ['ID', 'OWNERID', 'ADMID', 'DMDID', 'BEGIN',
#                         'END', 'BETYPE']:
#                 self.root.attrib[attrib.upper()] = value    
#             elif attrib.upper() == 'STREAMTYPE':
#                 self.root.attrib['streamType'] = value
#             else:
#                 # TODO: add exception
#                 pass


class TransformFile(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}transformFile'

    def _init(self):
        initialise_values(self, ['ID', 'TRANSFORMTYPE', 'TRANSFORMALGORITHM',
                    'TRANSFORMKEY', 'TRANSFORMBEHAVIOR', 'TRANSFORMORDER'])

# class TransformFile(object):
#     '''A subelement of File. The transform file element <transformFile>
#     provides a means to access any subsidiary files listed below a <file>
#     element by indicating the steps required to "unpack" or transform the
#     subsidiary files. This element is repeatable and might provide a link to a
#     <behavior> in the <behaviorSec> that performs the transformation. '''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}transformFile" % (METS_NS), 
#             nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper() in ['ID', 'TRANSFORMTYPE', 'TRANSFORMALGORITHM',
#                     'TRANSFORMKEY', 'TRANSFORMBEHAVIOR', 'TRANSFORMORDER']:
#                 self.root.attrib[attrib.upper()] = value
#             else:
#                 # TODO: add exception
#                 pass


# structMap classes

class StructMap(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}transformFile'

    def _init(self):
        initialise_values(self, ['ID', 'TYPE', 'LABEL'])

# class StructMap(object):
#     '''The structural map section <structMap> is the heart of a METS document.
#     It provides a means for organising the digital content represented by the
#     <file> elements in the <fileSec> of the METS document into a coherent
#     hierarchical structure. Such a hierarchical structure can be presented to
#     users to facilitate their comprehension and navigation of the digital 
#     content. The structure consists of a series of nested <div> elements. A
#     <div> element may directly point to content via <fptr> (file pointer)
#     elements or <mptr> (METS pointer) elements.'''
#     def __init__(self, **kwargs):
#         self.root = ET.Element("{%s}structMap" % (METS_NS,), nsmap=mets_nsmap)
#         for attrib, value in kwargs.items():
#             if attrib.upper() in ['ID', 'TYPE', 'LABEL']:
#                 self.root.attrib[attrib.upper()] = value
#             else:
#                 # TOD: add exception
#                 pass

class Div(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}div'

# class Div(object):
#     '''A subelement of METS.'''
#     def __init__(self, **kwargs):
#         self.root