import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from FreqObjectOps.DirOps import DirOps

import shutil
import time

# names of folder subfolders and their contents for testing
test_folder = os.path.join(os.path.dirname(__file__), 'test_folder')
test_subfolder = os.path.join(os.path.dirname(__file__), 'test_folder', 'test_subfolder')
test_folder_file_1 = os.path.join(os.path.dirname(__file__), 'test_folder', 'file_1.log')
test_folder_file_2 = os.path.join(os.path.dirname(__file__), 'test_folder', 'file_2.log')
test_subfolder_file_1 = os.path.join(os.path.dirname(__file__), 'test_folder', 'test_subfolder', 'file_1.log')
test_subfolder_file_2 = os.path.join(os.path.dirname(__file__), 'test_folder', 'test_subfolder', 'file_2.log')

# list of filesnames, order is important
test_filename_folder_list = [test_folder_file_1, test_folder_file_2]
test_filename_all_list = [test_folder_file_1, test_folder_file_2, test_subfolder_file_1, test_subfolder_file_2]


def test_001_create_temporary_files_and_folder():
	# delete test folder if exists
	if os.path.exists(test_folder):
		shutil.rmtree(test_folder, ignore_errors=True)

	# make required directories for testing
	os.mkdir(test_folder)
	os.mkdir(test_subfolder)

	# make required files for testing
	for filename in test_filename_all_list:
		f = open(filename, 'w+')
		f.close()
		time.sleep(0.5)  # force delay to ensure files are created in desired order


def test_002_get_file_location():
	assert DirOps.get_directory_from_filepath(
		filepath=os.path.join('test_folder', 'file_1.log')
	) == os.path.join('test_folder')


def test_002_get_base_name_from_file():
	assert DirOps.get_basename_from_filepath(
		filepath=os.path.join('test_folder', 'file_1.log')
	) == 'file_1'


def test_004_get_extension_from_file():
	assert DirOps.get_file_extension_from_filepath(
		filepath=os.path.join('test_folder', 'file_1.log')
	) == '.log'


def test_005_exists_folder_where_exists():
	assert DirOps.exists_folder(folder_path=test_folder) is True


def test_006_exists_folder_where_doesnot_exist():
	assert DirOps.exists_folder(folder_path=os.path.join(os.path.dirname(__file__), 'no_test_folder')) is False


def test_007_removing_temp_files():
	assert DirOps.get_filtered_list_without_temporary_files(
		file_list=['~$abc.xlsx', 'abc.xlsx']
	) == ['abc.xlsx']


def test_008_get_all_files_nonrecursive():
	assert DirOps.get_all_files_in_directory(folder_path=test_folder, pattern='*.log',
											 recursive=False).sort() == test_filename_folder_list.sort()


def test_009_get_all_files_recursive():
	assert DirOps.get_all_files_in_directory(
		folder_path=test_folder, pattern='*.log', recursive=True).sort() == test_filename_all_list.sort()


def test_010_get_latest_file():
	assert DirOps.get_latest_file_in_directory(folder_path=test_folder, pattern='*.log') == test_folder_file_2


def test_011_delete_temporary_files_and_folder():
	# delete directories which were created for testing
	if os.path.exists(test_folder):
		shutil.rmtree(test_folder, ignore_errors=True)
