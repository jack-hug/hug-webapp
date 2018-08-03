import json,logging,inspect,functools

class APIError(Exception):
	def __init__(self,error,data='',message=''):
		super(APIError,self).__init__(message)
		self.error = error
		self.data = data
		self.message = message

class APIValueError(APIError):
	def __init__(self, field,message=''):
		super(APIValueError, self).__init__('value:invalid',field,message)

class APIResourceNotFoundError(APIError):
	def __init__(self, message=''):
		super(APIResourceNotFoundError, self).__init__('permission:forbidden','permission',message)
			
class APIPermissionError(APIError):
	def __init__(self, message = ''):
		super(APIPermissionError, self).__init__('permission:forbidden','permission',message)
		
class Page(object):
	"""
	"""
	def __init__(self, item_count,page_index = 1,page_size = 10):
		self.item_count = item_count
		self.page_size = page_size
		