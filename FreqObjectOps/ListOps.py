class ListOps(object):

	def __init__(self):
		pass

	@classmethod
	def get_unique_list(cls, list_with_duplicates=None, sorted=None, reversed=None):
		if sorted is None:
			sorted = False
		if reversed is None:
			reversed = False

		unique_list = list(set(list_with_duplicates))
		if sorted:
			unique_list.sort(reverse=reversed)

		return unique_list

	@classmethod
	def get_common_items(cls, list_one=None, list_two=None):
		return list(set(list_one).intersection(list_two))

	@classmethod
	def get_all_items(cls, list_one=None, list_two=None):
		return list(set(list_one).union(list_two))

	@classmethod
	def get_flat_list(cls, list_of_lists=None):
		flat_list = [item for sub_list in list_of_lists for item in sub_list]
		return flat_list
