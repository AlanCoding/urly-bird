from urlmodel.models import *

def missing_bookmarkers():
	print("filling in missing bookmarkers...")
	for user in User.objects.all():
		if not hasattr(user, 'bookmarker'):
			print("  user: "+user.username)
			bmkr = Bookmarker(age=19, gender="M")
			bmkr.user = user
			bmkr.save()

def demo_solution():
	def model_field_exists(clf, field):
		return hasattr(clf, field)

	for user in User.objects.all():
		print(model_field_exists(user, 'bookmarker'))
	print(' id checking')
	for user in User.objects.all():
		print(model_field_exists(user, 'bookmarke.id'))
	print(' checking asdf')

	for user in User.objects.all():
		print(model_field_exists(user, 'asdf'))
