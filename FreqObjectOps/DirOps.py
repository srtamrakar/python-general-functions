import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import re
import glob


def normalize_returned_path(func):
	def wrapper(*args, **kwargs):
		return DirOps.get_norm_path(func(*args, **kwargs))

	return wrapper


class DirOps(object):

	def __init__(self):
		pass

	@classmethod
	def get_norm_path(cls, filepath=None):
		"""
		:param filepath: str
		:return:
			normalized filepath as str
		"""
		return os.path.normcase(os.path.normpath(filepath))

	@classmethod
	@normalize_returned_path
	def get_abs_path(cls, filepath=None):
		"""
		:param filepath: str
		:return:
			absolute filepath as str
		"""
		if filepath is None: return None
		return os.path.abspath(filepath)

	@classmethod
	@normalize_returned_path
	def get_directory_from_filepath(cls, filepath=None):
		"""
		:param filepath: str
		:return:
			directory as str
		"""
		if filepath is None: return None
		return os.path.dirname(filepath)

	@classmethod
	def get_basename_from_filepath(cls, filepath=None):
		"""
		:param filepath: str
		:return:
			basename as str
		"""
		if filepath is None: return None
		return os.path.splitext(os.path.basename(filepath))[0]

	@classmethod
	def get_file_extension_from_filepath(cls, filepath=None):
		"""
		:param filepath: str
		:return:
			file extension as str
		"""
		if filepath is None: return None
		return os.path.splitext(os.path.basename(filepath))[-1]

	@classmethod
	def exists_folder(cls, folder_path=None):
		"""
		:param folder_path: str
		:return:
			whether the folder exists as bool
		"""
		if folder_path is None: return None
		if os.path.exists(folder_path):
			return True
		return False

	@classmethod
	def get_filtered_list_without_temporary_files(cls, file_list=None):
		"""
		:param file_list: list
			list of filenames
		:return:
			filtered list of non-temporary filenames
		"""
		temp_file_regex = re.compile(r'.*\~\$.*')
		try:
			temporary_files = list(filter(temp_file_regex.search, file_list))
			files_filtered = list(set(file_list) - set(temporary_files))
			return files_filtered
		except:
			return file_list

	@classmethod
	def get_all_files_in_directory(cls, folder_path=None, pattern=None, recursive=None):
		"""
		:param folder_path: str
		:param pattern: str
		:param recursive: bool
			whether to get files from sub-directories as well
		:return:
			list of filenames inside folder_path
		"""
		if folder_path is None: return None
		if not pattern: pattern = '*.*'  # e.g. *.xlsx
		if not recursive: recursive = False
		if recursive:
			file_pattern = os.path.join(folder_path, '**', pattern)
		else:
			file_pattern = os.path.join(folder_path, pattern)
		all_files_list = glob.glob(file_pattern, recursive=recursive)
		all_files_list = list(map(cls.get_norm_path, all_files_list))
		all_files_list = cls.get_filtered_list_without_temporary_files(file_list=all_files_list)
		return all_files_list

	@classmethod
	@normalize_returned_path
	def get_latest_file_in_directory(cls, folder_path=None, pattern=None):
		"""
		:param folder_path: str
		:param pattern: str
		:return:
			filepath of the last updated file from the directory as str
		"""
		if folder_path is None: return None
		if not pattern: pattern = '*.*'  # e.g. *.xlsx
		all_files_list = cls.get_all_files_in_directory(folder_path=folder_path, pattern=pattern, recursive=False)
		if len(all_files_list) < 1:
			return None
		latest_file = max(all_files_list, key=os.path.getctime)
		return latest_file
