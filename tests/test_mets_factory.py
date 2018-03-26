import os
import shutil

from lxml import etree as ET
from nose.tools import *

from pymets import mets_factory as mf

nsmap = {"dnx"}

mixed_files = ['1.txt', '2.txt', 'apples.txt', 'carrots.txt', 'zebras.txt',
               '99.txt', 'aarvarks.txt', '4.txt']

def setup():
    print("SETUP!")
    os.mkdir('manyfiles_numeric')
    for i in range(100):
        i = str(i)
        with open('manyfiles_numeric/{}.txt'.format(i), 'w') as f:
            f.write(i)
    os.mkdir('manyfiles_alphanum')
    for i in range(100):
        i = str(i)
        with open('manyfiles_alphanum/page {}.txt'.format(i), 'w') as f:
            f.write(i)
    os.mkdir('manyfiles_mixed')
    for i in mixed_files:
        with open('manyfiles_mixed/{}'.format(i), 'w') as f:
            f.write(i)
    os.mkdir('manyfiles_leading_zeroes')
    for i in range(100):
        filename = 'page {:02d}.txt'.format(i)
        with open('manyfiles_leading_zeroes/{}'.format(filename), 'w') as f:
            f.write(filename)

def teardown():
    print("TEAR DOWN!")
    shutil.rmtree('manyfiles_numeric')
    shutil.rmtree('manyfiles_alphanum')
    shutil.rmtree('manyfiles_mixed')
    shutil.rmtree('manyfiles_leading_zeroes')

def test_basic():
    print("I ran!")

def test_build_amdsec_filegrp_structmap():
    mets = mf.build_mets()
    mf.build_amdsec_filegrp_structmap(mets,
        ie_id='ie1',
        pres_master_dir=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'data',
                'test_batch_1',
                'pm'),
        modified_master_dir=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'data',
                'test_batch_1',
                'mm'),
        access_derivative_dir=None,
        digital_original=False,
        input_dir=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'data',
                'test_batch_1'))
    amd_sec_list = mets.findall("./{http://www.loc.gov/METS/}amdSec")
    print("Here is the list of amdSec items: {}".format(amd_sec_list))
    assert(len(amd_sec_list) == 4)
    print(ET.tostring(mets, pretty_print=True))

def test_ordered_numeric_file_list():
    """make sure that numeric values are returned in a sensible order"""
    filelist = mf.ordered_file_list('manyfiles_numeric')
    for i in range(100):
        str_i = str(i)
        assert(filelist[i] == 'manyfiles_numeric/{}.txt'.format(str_i))
    # assert(filelist[0] == 'manyfiles_numeric/0.txt')
    # assert(filelist[-1] == 'manyfiles_numeric/99.txt')
    print(filelist)

def test_ordered_alphanum_file_list():
    """non-numeric filenames should return like sorted(os.listdir())"""
    filelist = mf.ordered_file_list('manyfiles_alphanum')
    test_list = []
    for i in range(100):
        test_list.append('manyfiles_alphanum/page {}.txt'.format(str(i)))
    test_list = sorted(test_list)
    assert(test_list == filelist)
    # assert(filelist[0] == 'manyfiles_alphanum/page 0.txt')
    # assert(filelist[-1] == 'manyfiles_alphanum/page 99.txt')
    print(filelist)

def test_mixed_numeric_alphanum_files():
    """alphanum files should appear first and sorted, then sorted numeric files"""
    test_list = ['manyfiles_mixed/aarvarks.txt', 'manyfiles_mixed/apples.txt',
                 'manyfiles_mixed/carrots.txt', 'manyfiles_mixed/zebras.txt',
                 'manyfiles_mixed/1.txt', 'manyfiles_mixed/2.txt',
                 'manyfiles_mixed/4.txt', 'manyfiles_mixed/99.txt']
    filelist = mf.ordered_file_list('manyfiles_mixed')
    print(filelist)
    print(test_list)
    assert(filelist == test_list)

def test_alpahnum_files_with_nums_and_leading_zeroes():
    """files like "page 001.txt" should return like sorted(os.listdir())"""
    filelist = mf.ordered_file_list('manyfiles_leading_zeroes')
    test_list = []
    for test_file in os.listdir('manyfiles_leading_zeroes'):
        test_list.append('manyfiles_leading_zeroes/' + test_file)
    print(filelist)
    assert(filelist == sorted(test_list))
