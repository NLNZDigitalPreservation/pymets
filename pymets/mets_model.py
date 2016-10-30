from lxml import etree as ET
# xml.etree.ElementTree as ET does not work, 
# as we use components that are only available in lxml

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

strict = True


def initialise_values(element, attribs_list):
    for key in element.attrib:
        if key in attribs_list:
            if key in ['href', 'arcrole', 'title', 'show', 'acutate', 'to',
                'FROM']:
                element.set("{%s}%s" % (XLIN_NS, key), element.attrib[key])
                del element.attrib[key]
        elif key not in attribs_list:
            print("WARN: {} not allowed in element {}".format(
                key, element.TAG))
            if strict:
                del element.attrib[key]


class Mets(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}mets'

    def tounicode(self, pretty_print=False):
        return ET.tounicode(self, pretty_print=pretty_print)

    def write(self, filename, pretty_print=False):
        with open(filename, 'w') as f:
            f.write(ET.tounicode(self, pretty_print=pretty_print))
# Generic parent classes


class MetsHdr(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}metsHdr'

    def _init(self):
        initialise_values(self, ['ID', 'ADMID', 'CREATEDATE', 'LASTMODDATE', 
            'RECORDSTATUS'])

    @property
    def ID(self):
        return self.attrib['ID']
    
    @ID.setter
    def ID(self, value):
        self.attib['ID'] = value
    
    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @ADMID.setter
    def ADMID(self, value):
        self.attrib['ADMID'] = value

    @property
    def CREATEDATE(self):
        return self.attrib['CREATEDATE']
    
    @CREATEDATE.setter
    def CREATEDATE(self, value):
        self.attrib['CREATEDATE'] = value

    @property
    def LASTMODDATE(self):
        return self.attrib['LASTMODDATE']
    
    @LASTMODDATE.setter
    def LASTMODDATE(self, value):
        self.attrib['LASTMODDATE'] = value

    @property
    def RECORDSTATUS(self):
        return self.attrib['RECORDSTATUS']
    
    @RECORDSTATUS.setter
    def RECORDSTATUS(self, value):
        self.attrib['RECORDSTATUS'] = value    


class DmdSec(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}dmdSec'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    

class AmdSec(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}amdSec'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value    


class BehaviorSec(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}behaviorSec'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value 



# Generic children of MetsHdr Parent
class Agent(ET.ElementBase):

    TAG = '{http://www.loc.gov/METS/}agent'

    def _init(self):
        initialise_values(self, ['ID', 'ROLE', 'OTHERROLE', 'TYPE', 'OTHERTYPE'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    
    @property
    def ROLE(self):
        return self.attrib['ROLE']

    @ROLE.setter
    def ROLE(self, value):
        self.attrib['ROLE'] = value

    @property
    def OTHERROLE(self):
        return self.attrib['OTHERROLE']

    @OTHERROLE.setter
    def OTHERROLE(self, value):
        self.attrib['OTHERROLE'] = value

    @property
    def TYPE(self):
        return self.attrib['TYPE']

    @TYPE.setter
    def TYPE(self, value):
        self.attrib['TYPE'] = value

    @property
    def OTHERTYPE(self):
        return self.attrib['OTHERTYPE']

    @OTHERTYPE.setter
    def othertype(self, value):
        self.attrib['OTHERTYPE'] = value


class Name(ET.ElementBase):
    '''A subelement of Agent. No attributes can be given - only a text value 
    for the element.
    '''
    
    TAG = '{http://www.loc.gov/METS/}name'


class Note(ET.ElementBase):
    '''A subelement of Agent. No attributes can be given - only a text value
    for the element.
    '''

    TAG = '{http://www.loc.gov/METS/}note'


class AltRecordID(ET.ElementBase):
    '''A subelement of metsHdr. Allows one to use alternative record 
    identifier values for the digital object represented by the METS document;
    the primary record identifier is stored in the OBJID attribute in the root
    <mets> document.
    '''

    TAG = '{http://www.loc.gov/METS/}altRecordID'

    def _init(self):
        initialise_values(self, ['ID', 'TYPE'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def TYPE(self):
        return self.attrib['TYPE']

    @TYPE.setter
    def TYPE(self, value):
        self.attrib['TYPE'] = value
    

class MetsDocumentId(ET.ElementBase):
    '''A subelement of metsHdr. Accepted attributes are ID and TYPE.'''

    TAG = '{http://www.loc.gov/METS/}metsDocumentID'

    def _init(self):
        initialise_values(self, ['ID', 'TYPE'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def TYPE(self):
        return self.attrib['TYPE']

    @TYPE.setter
    def TYPE(self, value):
        self.attrib['TYPE'] = value


class MdRef(ET.ElementBase):
    '''The metadata reference element <mdRef> element is a generic element
    used throughout the METS schema to provide a pointer to metadata which
    resides outside the METS document. NB: <mdRef> is an empty element. The
    location of the metadata must be recorded in the xlink:href attribute,
    supplemented by the XPTR attribute as needed.'''
    TAG = '{http://www.loc.gov/METS/}mdRef'

    def __init__(self):
        initialise_values(self, ['ID', 'LABEL', 'XPTR', 'LOCTYPE', 
            'OTHERLOCTYPE', 'MDTYPE', 'OTHERMDTYPE', 'MDTYPEVERSION',
            'MIMETYPE', 'SIZE', 'CREATED','CHECKSUM', 'CHECKSUMTYPE', 'href'])
    
    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    
    @property
    def LABEL(self):
        return self.attrib['LABEL']

    @LABEL.setter
    def LABEL(self, value):
        self.attrib['LABEL'] = value

    @property
    def XPTR(self):
        return self.attrib['XPTR']

    @XPTR.setter
    def XPTR(self, value):
        self.attrib['XPTR'] = value

    @property
    def LOCTYPE(self):
        return self.attrib['LOCTYPE']

    @LOCTYPE.setter
    def LOCTYPE(self, value):
        self.attrib['LOCTYPE'] = value

    @property
    def OTHERLOCTYPE(self):
        return self.attrib['OTHERLOCTYPE']

    @OTHERLOCTYPE.setter
    def OTHERLOCTYPE(self, value):
        self.attrib['OTHERLOCTYPE'] = value

    @property
    def MDTYPE(self):
        return self.attrib['MDTYPE']

    @MDTYPE.setter
    def MDTYPE(self, value):
        self.attrib['MDTYPE'] = value

    @property
    def OTHERMDTYPE(self):
        return self.attrib['OTHERMDTYPE']

    @OTHERMDTYPE.setter
    def OTHERMDTYPE(self, value):
        self.attrib['OTHERMDTYPE'] = value

    @property
    def MDTYPEVERSION(self):
        return self.attrib['MDTYPEVERSION']

    @MDTYPEVERSION.setter
    def MDTYPEVERSION(self, value):
        self.attrib['MDTYPEVERSION'] = value

    @property
    def MIMETYPE(self):
        return self.attrib['MIMETYPE']

    @MIMETYPE.setter
    def MIMETYPE(self, value):
        self.attrib['MIMETYPE'] = value

    @property
    def SIZE(self):
        return self.attrib['SIZE']

    @SIZE.setter
    def SIZE(self, value):
        self.attrib['SIZE'] = value

    @property
    def CREATED(self):
        return self.attrib['CREATED']

    @CREATED.setter
    def CREATED(self, value):
        self.attrib['CREATED'] = value

    @property
    def CHECKSUM(self):
        return self.attrib['CHECKSUM']

    @CHECKSUM.setter
    def CHECKSUM(self, value):
        self.attrib['CHECKSUM'] = value

    @property
    def CHECKSUMTYPE(self):
        return self.attrib['CHECKSUMTYPE']

    @CHECKSUMTYPE.setter
    def CHECKSUMTYPE(self, value):
        self.attrib['CHECKSUMTYPE'] = value

    @property
    def href(self):
        return self.attrib['{http://www.w3.org/1999/xlink}href']

    @href.setter
    def href(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}href'] = value


class MdWrap(ET.ElementBase):
    '''A subelement of dmdSec, techMD, rightsMD, sourceMD and digiProvMd. It
    is used to wrap metadata from other schemas, such as PREMIS.
    '''
    TAG = '{http://www.loc.gov/METS/}mdWrap'

    def _init(self):
        initialise_values(self, ['ID', 'LABEL', 
                    # Metadata attribute group
                    'MDTYPE', 'OTHERMDTYPE', 'MDTYPEVERSION', 'MIMETYPE',
                    'SIZE', 'CREATED', 'CHECKSUM', 'CHECKSUMTYPE'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    
    @property
    def LABEL(self):
        return self.attrib['LABEL']

    @LABEL.setter
    def LABEL(self, value):
        self.attrib['LABEL'] = value

    @property
    def MDTYPE(self):
        return self.attrib['MDTYPE']

    @MDTYPE.setter
    def MDTYPE(self, value):
        self.attrib['MDTYPE'] = value

    @property
    def OTHERMDTYPE(self):
        return self.attrib['OTHERMDTYPE']

    @OTHERMDTYPE.setter
    def OTHERMDTYPE(self, value):
        self.attrib['OTHERMDTYPE'] = value

    @property
    def MDTYPEVERSION(self):
        return self.attrib['MDTYPEVERSION']

    @MDTYPEVERSION.setter
    def MDTYPEVERSION(self, value):
        self.attrib['MDTYPEVERSION'] = value

    @property
    def MIMETYPE(self):
        return self.attrib['MIMETYPE']

    @MIMETYPE.setter
    def MIMETYPE(self, value):
        self.attrib['MIMETYPE'] = value

    @property
    def SIZE(self):
        return self.attrib['SIZE']

    @SIZE.setter
    def SIZE(self, value):
        self.attrib['SIZE'] = value

    @property
    def CREATED(self):
        return self.attrib['CREATED']

    @CREATED.setter
    def CREATED(self, value):
        self.attrib['CREATED'] = value

    @property
    def CHECKSUM(self):
        return self.attrib['CHECKSUM']

    @CHECKSUM.setter
    def CHECKSUM(self, value):
        self.attrib['CHECKSUM'] = value

    @property
    def CHECKSUMTYPE(self):
        return self.attrib['CHECKSUMTYPE']

    @CHECKSUMTYPE.setter
    def CHECKSUMTYPE(self, value):
        self.attrib['CHECKSUMTYPE'] = value


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
    the elements appearing in the <xmlData> element.
    '''

    TAG = '{http://www.loc.gov/METS/}xmlData'


class BinData(ET.ElementBase):
    '''The binary data wrapper element <binData> is used to contain Base64
    encoded metadata.
    '''

    TAG = '{http://www.loc.gov/METS/}binData'



# Generic children of AMD Parent

class MdExt(ET.ElementBase):
    '''Generic parent class of techMd, rightsMD, sourceMD and digiprovMd. Not
    intended to be called directly.
    '''

    def _init(self, element_name=None):
        self.tag = '{http://www.loc.gov/METS/}' + element_name
        initialise_values(self, ['ID', 'ADMID', 'CREATED', 'STATUS'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    
    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @ADMID.setter
    def ADMID(self, value):
        self.attrib['ADMID'] = value

    @property
    def CREATED(self):
        return self.attrib['CREATED']

    @CREATED.setter
    def CREATED(self, value):
        self.attrib['CREATED'] = value

    @property
    def STATUS(self):
        return self.attrib['STATUS']

    @STATUS.setter
    def STATUS(self, value):
        self.attrib['STATUS'] = value
    

class TechMd(MdExt):
    def _init(self, **kwargs):
        super(TechMd, self)._init("techMD", **kwargs)


class RightsMd(MdExt):
    def _init(self, **kwargs):
        super(RightsMd, self)._init("rightsMD",**kwargs)


class SourceMd(MdExt):
    def _init(self, **kwargs):
        super(SourceMd, self)._init("sourceMD", **kwargs)


class DigiprovMd(MdExt):
    def _init(self, **kwargs):
        super(DigiprovMd, self)._init("digiprovMD", **kwargs)


class FileSec(ET.ElementBase):
    '''The overall purpose of the content file section element <fileSec> is to
    provide an inventory of and the location for the content files that
    comprise the digital object being described in the METS document.
    '''
    TAG = '{http://www.loc.gov/METS/}fileSec'


class FileGrp(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}fileGrp'

    def _init(self):
        initialise_values(self, ['ID', 'VERSDATE', 'ADMID', 'USE'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def VERSDATE(self):
        return self.attrib['VERSDATE']

    @VERSDATE.setter
    def VERSDATE(self, value):
        self.attrib['VERSDATE'] = value

    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @ADMID.setter
    def ADMID(self, value):
        self.attrib['ADMID'] = value

    @property
    def USE(self):
        return self.attrib['USE']

    @USE.setter
    def USE(self, value):
        self.attrib['USE'] = value
    


class File(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}file'

    def _init(self):
        initialise_values(self, ['ID', 'SEQ', 'OWNERID', 'ADMID', 'DMDID',
                'GROUPID', 'USE', 'BEGIN', 'END', 'BETYPE'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def SEQ(self):
        return self.attrib['SEQ']

    @SEQ.setter
    def SEQ(self, value):
        self.attrib['SEQ'] = value

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
    def USE(self):
        return self.attrib['USE']

    @USE.setter
    def USE(self, value):
        self.attrib['USE'] = value

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


class FLocat(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}FLocat'

    def _init(self):
        initialise_values(self, ['ID', 'USE', 'LOCTYPE', 'OTHERLOCTYPE', 'href'])

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

    @property
    def LOCTYPE(self):
        return self.attrib['LOCTYPE']

    @LOCTYPE.setter
    def LOCTYPE(self, value):
        self.attrib['LOCTYPE'] = value

    @property
    def OTHERLOCTYPE(self):
        return self.attrib['OTHERLOCTYPE']

    @OTHERLOCTYPE.setter
    def OTHERLOCTYPE(self, value):
        self.attrib['OTHERLOCTYPE'] = value

    @property
    def href(self):
        return self.attrib['{http://www.w3.org/1999/xlink}href']

    @href.setter
    def href(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}href'] = value
        

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
    

class Stream(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}stream'

    def _init(self):
        # "streamType" is something of an anomaly here, as it is the only
        # attribute whose spelling is in camelCase (except for xlin:href). 
        # As such, we should case for if it is supplied in all-caps.
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


class TransformFile(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}transformFile'

    def _init(self):
        initialise_values(self, ['ID', 'TRANSFORMTYPE', 'TRANSFORMALGORITHM',
                    'TRANSFORMKEY', 'TRANSFORMBEHAVIOR', 'TRANSFORMORDER'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def TRANSFORMTYPE(self):
        return self.attrib['TRANSFORMTYPE']

    @TRANSFORMTYPE.setter
    def TRANSFORMTYPE(self, value):
        self.attrib['TRANSFORMTYPE'] = value

    @property
    def TRANSFORMALGORITHM(self):
        return self.attrib['TRANSFORMALGORITHM']

    @TRANSFORMALGORITHM.setter
    def TRANSFORMALGORITHM(self, value):
        self.attrib['TRANSFORMALGORITHM'] = value
    
    @property
    def TRANSFORMKEY(self):
        return self.attrib['TRANSFORMKEY']

    @TRANSFORMKEY.setter
    def TRANSFORMKEY(self, value):
        self.attrib['TRANSFORMKEY'] = value

    @property
    def TRANSFORMBEHAVIOR(self):
        return self.attrib['TRANSFORMBEHAVIOR']

    @TRANSFORMBEHAVIOR.setter
    def TRANSFORMBEHAVIOR(self, value):
        self.attrib['TRANSFORMBEHAVIOR'] = value

    @property
    def TRANSFORMORDER(self):
        return self.attrib['TRANSFORMORDER']

    @TRANSFORMORDER.setter
    def TRANSFORMORDER(self, value):
        self.attrib['TRANSFORMORDER'] = value


# structMap classes

class StructMap(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}structMap'

    def _init(self):
        initialise_values(self, ['ID', 'TYPE', 'LABEL'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def TYPE(self):
        return self.attrib['TYPE']

    @TYPE.setter
    def TYPE(self, value):
        self.attrib['TYPE'] = value

    @property
    def LABEL(self):
        return self.attrib['LABEL']

    @LABEL.setter
    def LABEL(self, value):
        self.attrib['LABEL'] = value
    


class Div(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}div'

    def _init(self):
        initialise_values(self, ['ID', 'ORDER', 'ORDERLABEL', 'LABEL',
            'DMDID', 'ADMID', 'TYPE', 'CONTENTIDS'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def ORDER(self):
        return self.attrib['ORDER']

    @ORDER.setter
    def ORDER(self, value):
        self.attrib['ORDER'] = value

    @property
    def ORDERLABEL(self):
        return self.attrib['ORDERLABEL']

    @ORDERLABEL.setter
    def ORDERLABEL(self, value):
        self.attrib['ORDERLABEL'] = value

    @property
    def LABEL(self):
        return self.attrib['LABEL']

    @LABEL.setter
    def LABEL(self, value):
        self.attrib['LABEL'] = value

    @property
    def DMDID(self):
        return self.attrib['DMDID']

    @DMDID.setter
    def DMDID(self, value):
        self.attrib['DMDID'] = value

    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @DMDID.setter
    def ADMID(self, value):
        self.attrib['ADMID'] = value

    @property
    def TYPE(self):
        return self.attrib['TYPE']

    @TYPE.setter
    def TYPE(self, value):
        self.attrib['TYPE'] = value

    @property
    def CONTENTIDS(self):
        return self.attrib['CONTENTIDS']

    @CONTENTIDS.setter
    def CONTENTIDS(self, value):
        self.attrib['CONTENTIDS'] = value

class Mptr(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}mptr'

    def _init(self):
        initialise_values(self, ['ID', 'CONTENTIDS', 'LOCTYPE',
            'OTHERLOCTYPE', ])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def CONTENTIDS(self):
        return self.attrib['CONTENTIDS']

    @CONTENTIDS.setter
    def CONTENTIDS(self, value):
        self.attrib['CONTENTIDS'] = value

    @property
    def LOCTYPE(self):
        return self.attrib['LOCTYPE']

    @LOCTYPE.setter
    def LOCTYPE(self, value):
        self.attrib['LOCTYPE'] = value

    @property
    def OTHERLOCTYPE(self):
        return self.attrib['OTHERLOCTYPE']

    @OTHERLOCTYPE.setter
    def OTHERLOCTYPE(self, value):
        self.attrib['OTHERLOCTYPE'] = value


class Fptr(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}fptr'

    def _init(self):
        initialise_values(self, ['ID', 'FILEID', 'CONTENTIDS'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def FILEID(self):
        return self.attrib['FILEID']

    @FILEID.setter
    def FILEID(self, value):
        self.attrib['FILEID'] = value

    @property
    def CONTENTIDS(self):
        return self.attrib['CONTENTIDS']

    @CONTENTIDS.setter
    def CONTENTIDS(self, value):
        self.attrib['CONTENTIDS'] = value


class Par(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}par'

    def _init(self):
        initialise_values(self, 'ID')

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    

class Seq(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}seq'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value


class Area(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}area'

    def _init(self):
        initialise_values(self, ['ID', 'FILEID', 'SHAPE', 'COORDS',
            'BEGIN', 'END', 'BETYPE', 'EXTENT', 'EXTTYPE', 'ADMID',
            'CONTENTIDS'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def FILEID(self):
        return self.attrib['FILEID']

    @FILEID.setter
    def FILEID(self, value):
        self.attrib['FILEID'] = value

    @property
    def SHAPE(self):
        return self.attrib['SHAPE']

    @SHAPE.setter
    def SHAPE(self, value):
        self.attrib['SHAPE'] = value

    @property
    def COORDS(self):
        return self.attrib['COORDS']

    @COORDS.setter
    def COORDS(self, value):
        self.attrib['COORDS'] = value

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
    def EXTENT(self):
        return self.attrib['EXTENT']

    @EXTENT.setter
    def EXTENT(self, value):
        self.attrib['EXTENT'] = value

    @property
    def EXTTYPE(self):
        return self.attrib['EXTTYPE']

    @EXTTYPE.setter
    def EXTTYPE(self, value):
        self.attrib['EXTTYPE'] = value

    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @ADMID.setter
    def ADMID(self, value):
        self.attrib['ADMID'] = value

    @property
    def CONTENTIDS(self):
        return self.attrib['CONTENTIDS']

    @CONTENTIDS.setter
    def CONTENTIDS(self, value):
        self.attrib['CONTENTIDS'] = value


class SmLink(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}smLink'

    def _init(self):
        initialise_values(self, ['ID', 'arcrole', 'title', 'show',
            'actuate', 'to', 'from'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def arcrole(self):
        return self.attrib['{http://www.w3.org/1999/xlink}arcrole']

    @arcrole.setter
    def arcrole(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}arcrole'] = value

    @property
    def title(self):
        return self.attrib['{http://www.w3.org/1999/xlink}title']

    @title.setter
    def title(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}title'] = value

    @property
    def show(self):
        return self.attrib['{http://www.w3.org/1999/xlink}show']

    @show.setter
    def show(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}show'] = value

    @property
    def actuate(self):
        return self.attrib['{http://www.w3.org/1999/xlink}actuate']

    @actuate.setter
    def actuate(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}actuate'] = value

    @property
    def to(self):
        return self.attrib['{http://www.w3.org/1999/xlink}to']

    @to.setter
    def to(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}to'] = value

    @property
    def FROM(self):
        return self.attrib['{http://www.w3.org/1999/xlink}from']

    @to.setter
    def FROM(self, value):
        self.attrib['{http://www.w3.org/1999/xlink}from'] = value


class SmLinkGrp(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}smLinkGrp'

    def _init(self):
        initialise_values(self, ['ID', 'ARCLINKORDER'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def ARCLINKORDER(self):
        return self.attrib['ARCLINKORDER']

    @ARCLINKORDER.setter
    def ARCLINKORDER(self, value):
        self.attrib['ARCLINKORDER'] = value
    

class SmLocatorLink(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}smLocatorLink'

    def _init(self):
        initialise_values(self, ['ID'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self):
        self.attrib['ID'] = value


class SmArcLink(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}smArcLink'

    def _init(self):
        initialise_values(self, ['ID', 'ARCTYPE', 'ADMID'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self):
        self.attrib['ID'] = value

    @property
    def ARCTYPE(self):
        return self.attrib['ARCTYPE']

    @ID.setter
    def ARCTYPE(self):
        self.attrib['ARCTYPE'] = value

    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @ID.setter
    def ADMID(self):
        self.attrib['ADMID'] = value


class Behavior(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}behavior'

    def _init(self):
        initialise_values(self, ['ID', 'STRUCTID', 'BTYPE', 'CREATED',
            'LABEL', 'GROUPID', 'ADMID'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value
    
    @property
    def STRUCTID(self):
        return self.attrib['STRUCTID']

    @STRUCTID.setter
    def STRUCTID(self, value):
        self.attrib['STRUCTID'] = value

    @property
    def BTYPE(self):
        return self.attrib['BTYPE']

    @BTYPE.setter
    def BTYPE(self, value):
        self.attrib['BTYPE'] = value

    @property
    def CREATED(self):
        return self.attrib['CREATED']

    @CREATED.setter
    def CREATED(self, value):
        self.attrib['CREATED'] = value

    @property
    def LABEL(self):
        return self.attrib['LABEL']

    @LABEL.setter
    def LABEL(self, value):
        self.attrib['LABEL'] = value

    @property
    def GROUPID(self):
        return self.attrib['GROUPID']

    @GROUPID.setter
    def GROUPID(self, value):
        self.attrib['GROUPID'] = value

    @property
    def ADMID(self):
        return self.attrib['ADMID']

    @ADMID.setter
    def ADMID(self, value):
        self.attrib['ADMID'] = value


class InterfaceDef(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}interfaceDef'

    def _init(self):
        initialise_values(self, ['ID', 'LABEL'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def LABEL(self):
        return self.attrib['LABEL']

    @LABEL.setter
    def LABEL(self, value):
        self.attrib['LABEL'] = value


class Mechanism(ET.ElementBase):
    TAG = '{http://www.loc.gov/METS/}mechanism'

    def _init(self):
        initialise_values(self, ['ID', 'LABEL'])

    @property
    def ID(self):
        return self.attrib['ID']

    @ID.setter
    def ID(self, value):
        self.attrib['ID'] = value

    @property
    def LABEL(self):
        return self.attrib['LABEL']

    @LABEL.setter
    def LABEL(self, value):
        self.attrib['LABEL'] = value