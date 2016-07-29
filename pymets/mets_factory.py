import mets

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
