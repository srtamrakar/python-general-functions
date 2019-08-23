import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import re
import glob


class DirOps(object):

	def __init__(self):
		pass

	@classmethod
	def get_directory_from_filepath(cls, filepath=None):
		if filepath is None: return None
		return os.path.dirname(filepath)

	@classmethod
	def get_basename_from_filepath(cls, filepath=None):
		if filepath is None: return None
		return os.path.splitext(os.path.basename(filepath))[0]

	@classmethod
	def get_file_extension_from_filepath(cls, filepath=None):
		if filepath is None: return None
		return os.path.splitext(os.path.basename(filepath))[-1]

	@classmethod
	def exists_folder(cls, folder_path=None):
		if folder_path is None: return None
		if os.path.exists(folder_path):
			return True
		return False

	@classmethod
	def get_filtered_list_without_temporary_files(cls, file_list=None):
		"""
		Gets rid of temporary files, which has filename in the format ~$xyz.ext.
		:param file_list: list of filenames
		:return: filtered list of non-temporary filenames
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
		if folder_path is None: return None
		if not pattern: pattern = '*.*'  # e.g. *.xlsx
		if not recursive: recursive = False
		if recursive:
			file_pattern = os.path.join(folder_path, '**', pattern)
		else:
			file_pattern = os.path.join(folder_path, pattern)
		all_files_list = glob.glob(file_pattern, recursive=recursive)
		all_files_list = cls.get_filtered_list_without_temporary_files(file_list=all_files_list)
		return all_files_list

	@classmethod
	def get_latest_file_in_directory(cls, folder_path=None, pattern=None):
		if folder_path is None: return None
		if not pattern: pattern = '*.*'  # e.g. *.xlsx
		all_files_list = cls.get_all_files_in_directory(folder_path=folder_path, pattern=pattern, recursive=False)
		if len(all_files_list) < 1:
			return None
		latest_file = max(all_files_list, key=os.path.getctime)
		return latest_file

	@classmethod
	def get_abs_path_for_a_filepath(cls, filepath=None):
		if filepath is None: return None
		return os.path.abspath(filepath)
