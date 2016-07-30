import mets

import os

from collections import OrderedDict

def build_mets():
    return mets.Mets()

def build_metsHdr():
    pass

def build_agent(agent_attrs, name, note_list):
    pass


def build_generic_sec(sec, attrs, mdRef_list, mdWrap_list):
    generic_sec = sec(**attrs)
    if mdRef_list:
        for mdRef_list_element in mdRef_list:
            pass
    if mdWrap_list:
        for mdWrap_list_element in mdWrap_list:
            generic_sec.append(mdWrap_list_element)
    return generic_sec


def build_dmdSec(dmdSec_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets.DmdSec, dmdSec_attrs, mdRef_list, 
        mdWrap_list)


def build_mdWrap(mdWrap_attrs, binData_list=None, xmlData_list=None):
    md_wrap = mets.MdWrap(**mdWrap_attrs)
    if binData_list:
        for binData_list_element in binData_list:
            bd = mets.BinData()
            bd.text = binData_list_element
            md_wrap.append(bd)
    if xmlData_list:
        for xmlData_list_element in xmlData_list:
            xd = mets.XmlData()
            xd.append(xmlData_list_element)
    return md_wrap


def build_mdRef(mdRef_attrs):
    return mets.MdRef(mdRef_attrs)


def build_amdSec(amdSec_attrs, techMD_list=None, rightsMD_list=None,
    sourceMD_list=None, digiprovMD_list=None):
    amd_sec = mets.AmdSec(**amdSec_attrs)
    for md_list in (techMD_list, rightsMD_list, sourceMD_list, digiprovMD_list):
        if md_list:
            for md_list_element in md_list:
                amd_sec.append(md_list_element)
    return amd_sec


def build_techMD(techMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets.TechMd, techMD_attrs, mdRef_list, 
        mdWrap_list)


def build_rightsMD(rightsMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets.TechMd, rightsMD_attrs, mdRef_list, 
        mdWrap_list)


def build_sourceMD(sourceMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets.SourceMd, sourceMD_attrs, mdRef_list, 
        mdWrap_list)


def build_sourceMD(digiprovMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets.DigiprovMd, digiprovMD_attrs, mdRef_list, 
        mdWrap_list)

# Helpers for constructing structmap and filesec

def os_path_split_asunder(path, debug=False):
    parts = []
    while True:
        newpath, tail = os.path.split(path)
        if debug: print(repr(path), (newpath, tail))
        if newpath == path:
            assert not tail
            if path: parts.append(path)
            break
        parts.append(tail)
        path = newpath
    parts.reverse()
    # Added 09/09/2015: hack to remove leading slash - make this better!
    if parts[0] == "/" or parts[0] == "\\":
        parts = parts[1:]
    return parts


def generate_flgrp_details(mets, rep_directory_path, rep_id, pres_type, input_dir):
    """Generates the fileGrp details for a representation in the form of
    a list containing a dictionary for each file in the rep.
    At the same time, a structMap is also generated for the rep and
    appended to the METS."""
    # start off with structMap details
    repType = 'PHYSICAL'
    presType = pres_type
    fileDict = OrderedDict()
    # presType: 'Preservation Master'
    # fileDict: [ {'Image 1': [{'TYPE': 'FILE'}, {'FILEID': 'fid1-1'}]},
    #             {'Image 2': [{'TYPE': 'FILE'}, {'FILEID': 'fid2-1'}]} ]
    # Now do flgrp details
    # fd = {'rep' + idNo: [{"USE": "VIEW"},[],]}
    fd = {rep_id: [{"USE": "VIEW"},[],]}
    fileNo = 0
    # oo = input_dir
    file_list = ordered_file_list(rep_directory_path)
    for item in file_list:
        fileNo += 1
        filepath = item
        # the filepath needs to be relative to the SIP structure, not the
        # absolute path on the current machine. So, trim the filepath here!
        filepath = filepath[len(input_dir):]
                # 09/09/2015: Hack to remove the leading slash
        if filepath[0] == "/" or filepath[0] == "\\":
            filepath = filepath[1:]
        # file_details = {'fid' + str(fileNo) :
        file_details = {"{}-{}".format( rep_id, str(fileNo) ) :
                            {
                            # 'MIMETYPE': mime_type,
                            'href': filepath} }
        fd[rep_id][1].append(file_details)

        # time to build the fileDict for the StructMap!

        item = item[item.find(rep_directory_path)+ len(rep_directory_path): ]

        file_path_dict = os_path_split_asunder(item)
        # grab the filename from file_path_dict
        file_name = file_path_dict.pop()
        # reverse the file_path_dict, so we can easily 
        # pop off the dirs in order
        file_path_dict = file_path_dict[::-1]

        populate_file_dict(file_path_dict, 
                           file_name, 
                           # "fid%s-%s" % (str(fileNo), idNo),
                           "{}-file{}".format(rep_id, str(fileNo)),
                           fileDict)

        # Now, back to the structMap!
    structMap_attrs = {'ID': rep_id, 'TYPE': repType}
    mets.append(build_structMap(structMap_attrs=structMap_attrs, 
                                presType=presType,
                                fileDict=fileDict))
    return fd


def ordered_file_list(rep_directory_path):
    """Checks to see if all files in a directory have integers for filenames,
    and if they do, they will be sorted numerically for the structMap."""
    # NOTE: this function assumes that the files either have no extension,
    # or that they contain a single extension. If, for example, you have a
    # directory full of files like 1.tar.gz, 2.tar.gz, etc, they will not be
    # sorted numerically.

    file_list = os.walk(rep_directory_path)
    output_file_list = []

    for root, dirs, files in file_list:
        int_file_names = []
        str_file_names = []
        for item in files:
            try:
                # coercing to unicode to better handle utf8 characters
                item = unicode(item, "utf-8") 
                item_test = item[:item.rfind(".")]
                int(item_test)  # If we don't get a value error, it's an int!
                int_file_names.append(item)
            except ValueError:
                str_file_names.append(item)
        if len(int_file_names) > 0:
            int_file_names = sorted(int_file_names, key=lambda x: int(x[:x.rfind(".")]))
        files = str_file_names + int_file_names
        for item in files:
            output_file_list.append(os.path.join(root,item))
    return output_file_list


def recurse_over_filedict(root_element, input_dict):
    for key in input_dict.keys():
        if type(input_dict[key]) is str:
            fileDiv = mets.Div(LABEL=key, TYPE="FILE")
            root_element.append(fileDiv)
            fptr = mets.Fptr(FILEID=input_dict[key])
            fileDiv.append(fptr)
        elif type(input_dict[key]) is OrderedDict:
            folderDiv = mets.Div(LABEL=key)
            root_element.append(folderDiv)
            recurse_over_filedict(folderDiv, input_dict[key])


def populate_file_dict(file_path_list, file_name, file_id, init_dict):
    if len(file_path_list) > 0:
        if file_path_list[-1] in init_dict.keys():
            populate_file_dict(file_path_list[:-1], file_name, file_id, init_dict[file_path_list[-1]])
        else:
            init_dict[file_path_list[-1]] = OrderedDict()
            populate_file_dict(file_path_list[:-1], file_name, file_id, init_dict[file_path_list[-1]])
    else:
        init_dict[file_name] = file_id


def build_structMap(structMap_attrs, presType, fileDict):
    structMap = mets.StructMap(**structMap_attrs)
    recurse_over_filedict(structMap, fileDict)
     # repId (str): representation ID, e.g. '1', '2', etc.
     #        repType (str): e.g. 'PHYSICAL', 'DIGITAL', etc.
     #        presType (str): e.g. 'PRESERVATION MASTER', 'MODIFIED MASTER', etc.
     #        fileDict (list): e.g -
     #            {"path":
     #                {"to":
     #                    {"file":
     #                        {
     #                            "file1.fl": "fid1-1",
     #                            "file2.fl": "fid2-1"
     #                        },
     #                     "different":
     #                        {"file":
     #                            {
     #                                "file3.fl": "fid3-1"
     #                            },
     #                        }
     #                    }
     #                }
     #              }

    return structMap