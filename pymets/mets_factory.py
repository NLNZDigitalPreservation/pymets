from collections import OrderedDict
import os

from pymets import mets_model


def build_mets():
    return mets_model.Mets()

def build_amdsec_filegrp_structmap(mets_doc,
                          ie_id=None,
                          pres_master_dir=None,
                          modified_master_dir=None,
                          access_derivative_dir=None,
                          digital_original=False,
                          input_dir=None):

    flgrp_dict = []

    if (pres_master_dir != None and 
            modified_master_dir != None and 
            access_derivative_dir != None):
        parse_rep_directory(
                mets_doc, 
                pres_master_dir, 
                'PRESERVATION_MASTER',
                ie_id + "-rep1", 
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=pres_master_dir,
                rep_id=ie_id + "-rep1",
                pres_type="Preservation Master",
                input_dir=input_dir))
        parse_rep_directory(
                mets_doc,
                modified_master_dir,
                'MODIFIED_MASTER',
                ie_id + "-rep2",
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=modified_master_dir,
                rep_id=ie_id + "-rep2",
                pres_type="Modified Master",
                input_dir=input_dir))
        parse_rep_directory(
                mets_doc,
                access_derivative_dir,
                'DERIVATIVE_COPY',
                ie_id + "-rep3",
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=access_derivative_dir,
                rep_id=ie_id + "-rep3",
                pres_type="Derivative Copy",
                input_dir=input_dir))

    elif pres_master_dir != None and access_derivative_dir != None:
        parse_rep_directory(
                mets_doc,
                pres_master_dir,
                'PRESERVATION_MASTER',
                ie_id + "-rep1",
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=pres_master_dir,
                rep_id=ie_id + "-rep1",
                pres_type="Preservation Master",
                input_dir=input_dir))
        parse_rep_directory(
                mets_doc,
                access_derivative_dir,
                'DERIVATIVE_COPY',
                ie_id + "-rep2",
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=access_derivative_dir,
                rep_id=ie_id + "-rep2",
                pres_type="Derivative Copy",
                input_dir=input_dir))

    elif pres_master_dir != None and modified_master_dir != None:
        parse_rep_directory(
                mets_doc,
                pres_master_dir,
                'PRESERVATION_MASTER',
                ie_id + "-rep1",
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=pres_master_dir,
                rep_id=ie_id + "-rep1",
                pres_type="Preservation Master",
                input_dir=input_dir))
        parse_rep_directory(
                mets_doc,
                modified_master_dir,
                'MODIFIED_MASTER',
                ie_id + "-rep2",
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=modified_master_dir,
                rep_id=ie_id + "-rep2",
                pres_type="Modified Master",
                input_dir=input_dir))

    elif pres_master_dir != None:
        parse_rep_directory(
                mets_doc,
                pres_master_dir,
                'PRESERVATION_MASTER',
                ie_id + "-rep1",
                digital_original)
        flgrp_dict.append(generate_flgrp_details_and_structmap(
                mets=mets_doc,
                rep_directory_path=pres_master_dir,
                rep_id=ie_id + "-rep1",
                pres_type="Preservation Master",
                input_dir=input_dir))

    if len(flgrp_dict) > 0:
        mets_doc.append(build_fileSec(flgrp_dict=flgrp_dict))

    # reposition the structmap so it is at the final point of the 
    structmap_list = mets_doc.xpath("/mets:mets/mets:structMap", 
            namespaces={'mets': 'http://www.loc.gov/METS/'})
    for structmap in structmap_list:
        mets_doc.append(structmap)
        
    return mets_doc


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

# dmdSec

def build_dmdSec(dmdSec_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets_model.DmdSec, dmdSec_attrs, mdRef_list, 
        mdWrap_list)


def build_mdWrap(mdWrap_attrs, binData_list=None, xmlData_list=None):
    md_wrap = mets_model.MdWrap(**mdWrap_attrs)
    if binData_list:
        for binData_list_element in binData_list:
            bd = mets_model.BinData()
            bd.text = binData_list_element
            md_wrap.append(bd)
    if xmlData_list:
        for xmlData_list_element in xmlData_list:
            xd = mets_model.XmlData()
            xd.append(xmlData_list_element)
    return md_wrap


def build_mdRef(mdRef_attrs):
    return mets_model.MdRef(mdRef_attrs)


# amdSec

def build_amdSec(amdSec_attrs, techMD_list=None, rightsMD_list=None,
    sourceMD_list=None, digiprovMD_list=None):
    amd_sec = mets_model.AmdSec(**amdSec_attrs)
    for md_list in (techMD_list, rightsMD_list, sourceMD_list, digiprovMD_list):
        if md_list:
            for md_list_element in md_list:
                amd_sec.append(md_list_element)
    return amd_sec


def build_techMD(techMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets_model.TechMd, techMD_attrs, mdRef_list, 
        mdWrap_list)


def build_rightsMD(rightsMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets_model.TechMd, rightsMD_attrs, mdRef_list, 
        mdWrap_list)


def build_sourceMD(sourceMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets_model.SourceMd, sourceMD_attrs, mdRef_list, 
        mdWrap_list)


def build_sourceMD(digiprovMD_attrs, mdRef_list, mdWrap_list):
    return build_generic_sec(mets_model.DigiprovMd, digiprovMD_attrs, mdRef_list, 
        mdWrap_list)

# Helpers for amdsecs for reps and files

def parse_rep_directory(mets_record, 
                        rep_directory_path,
                        pres_type,
                        idNo,
                        digital_original=False):
    if rep_directory_path and len(os.listdir(rep_directory_path)) > 0:
        rep_amd = mets_model.AmdSec(ID=idNo + '-amd')
        mets_record.append(rep_amd)
        flNo = 0
        file_list = ordered_file_list(rep_directory_path)
        for item in file_list:
            flNo += 1
            filepath = item
            amd_id = "{}-file{}".format(idNo, flNo)
            fl_amd = mets_model.AmdSec(ID=amd_id + '-amd')
            mets_record.append(fl_amd)

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


def generate_flgrp_details_and_structmap(mets, rep_directory_path, rep_id,
                                         pres_type, input_dir):
    """Generates the fileGrp details for a representation in the form of
    a list containing a dictionary for each file in the rep.
    At the same time, a structMap is also generated for the rep and
    appended to the mets_model.
    """
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
        file_details = {"{}-file{}".format( rep_id, str(fileNo) ) :
                            {
                            # 'MIMETYPE': mime_type,
                            'href': filepath} }
        fd[rep_id][1].append(file_details)

        # time to build the fileDict for the StructMap!

        item = item[item.find(rep_directory_path)+ len(rep_directory_path):]
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
    structMap_attrs = {'ID': rep_id + "-1", 'TYPE': repType}
    mets.append(build_structMap(structMap_attrs=structMap_attrs, 
                                presType=presType,
                                fileDict=fileDict))
    return fd


def ordered_file_list(rep_directory_path):
    """Checks to see if all files in a directory have integers for filenames,
    and if they do, they will be sorted numerically for the structMap.
    """
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
                item_test = item[:item.rfind(".")]
                int(item_test)  # If we don't get a value error, it's an int!
                int_file_names.append(item)
            except ValueError:
                str_file_names.append(item)
        if len(int_file_names) > 0:
            int_file_names = sorted(int_file_names, 
                key=lambda x: int(x[:x.rfind(".")]))
        files = str_file_names + int_file_names
        for item in files:
            output_file_list.append(os.path.join(root,item))
    return output_file_list


def recurse_over_filedict(root_element, input_dict, pres_type=None):
    if pres_type != None:
        div = mets_model.Div(LABEL=pres_type)
        root_element.append(div)
        root_element = div
    for key in input_dict.keys():
        if type(input_dict[key]) is str:
            fileDiv = mets_model.Div(LABEL=key, TYPE="FILE")
            root_element.append(fileDiv)
            fptr = mets_model.Fptr(FILEID=input_dict[key])
            fileDiv.append(fptr)
        elif type(input_dict[key]) is OrderedDict:
            folderDiv = mets_model.Div(LABEL=key)
            root_element.append(folderDiv)
            recurse_over_filedict(folderDiv, input_dict[key])


def populate_file_dict(file_path_list, file_name, file_id, init_dict):
    if len(file_path_list) > 0:
        if file_path_list[-1] in init_dict.keys():
            populate_file_dict(file_path_list[:-1], 
                               file_name,
                               file_id,
                               init_dict[file_path_list[-1]])
        else:
            init_dict[file_path_list[-1]] = OrderedDict()
            populate_file_dict(file_path_list[:-1],
                               file_name,
                               file_id,
                               init_dict[file_path_list[-1]])
    else:
        init_dict[file_name] = file_id


def build_structMap(structMap_attrs, presType, fileDict):
    structMap = mets_model.StructMap(**structMap_attrs)
    recurse_over_filedict(structMap, fileDict, presType)
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


def build_fileSec(flgrp_dict):
    file_sec = mets_model.FileSec()
    for rep in flgrp_dict:
        for item in rep:
            id_val = item
            rep_no = id_val[3:]
            rep_admid = id_val + "-amd"
            flgrp_attrs = {'USE': rep[item][0]['USE'],
                           'ID': id_val,
                           'ADMID': rep_admid}
            flgrp = mets_model.FileGrp(**flgrp_attrs)
            file_sec.append(flgrp)
            for file_item in rep[item][1]:
                for fi in file_item:
                    file_id = fi
                    file_admid = "{}-amd".format(file_id)
                    file_element = mets_model.File(ID=file_id, 
                                                   ADMID=file_admid)
                    flgrp.append(file_element)
                    flocat = mets_model.FLocat(href=file_item[fi]['href'],
                                               LOCTYPE='URL')
                    file_element.append(flocat)
    return file_sec