class ListOps(object):

	def __init__(self):
		pass

	@classmethod
	def remove_duplicates(cls, unfiltered_list=None, sorted=None, reversed=None):
		"""
		:param unfiltered_list: list
		:param sorted: bool
			whether returned list should be sorted
		:param reversed: bool
			whether returned list should be reverse sorted
		:return:
			list with unique items
		"""
		if sorted is None:
			sorted = False
		if reversed is None:
			reversed = False

		unique_list = list(set(unfiltered_list))
		if sorted:
			unique_list.sort(reverse=reversed)

		return unique_list

	@classmethod
	def get_intersection(cls, list_one=None, list_two=None):
		"""
		:param list_one: list
		:param list_two: list
		:return:
			list with common items
		"""
		return list(set(list_one).intersection(list_two))

	@classmethod
	def get_union(cls, list_one=None, list_two=None):
		"""
		:param list_one: list
		:param list_two: list
		:return:
			list with all items
		"""
		return list(set(list_one).union(list_two))

	@classmethod
	def get_flat_list(cls, list_of_lists=None):
		"""
		:param list_of_lists: list of list
		:return:
			flattened list
		"""
		flat_list = [item for sub_list in list_of_lists for item in sub_list]
		return flat_list
