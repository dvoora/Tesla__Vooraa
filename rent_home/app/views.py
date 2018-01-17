import json
from rest_framework.views import APIView
from django.shortcuts import HttpResponse
from models import Owner,HomeAssests,Renter

class CreateOwner(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to create owner.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		if 'first_name' in request.data:
			first_name = request.data['first_name']
		else:
			first_name = None

		if 'last_name' in request.data:
			last_name = request.data['last_name']
		else:
			last_name = None

		if 'email' in request.data:
			email = request.data['email']
		else:
			email = None

		if 'password' in request.data:
			password = request.data['password']
		else:
			password = None

		owner_object = Owner(status=False,username=username,first_name=first_name,
			last_name=last_name,email=email,password=password)
		owner_object.save()
		data = {'status':200,'msg':'Owner account created succesfully.'}
		return HttpResponse(json.dumps(data),content_type="application/json")

class ListOwners(APIView):

	def get(self, request,format=None):
		all_owners = Owner.objects.all()
		all_owners = list(all_owners)
		all_owners_list = [{'username':item.username,'email':item.email,'first_name':item.first_name,
		'last_name':item.last_name,'status':item.status} for item in all_owners]	
		data = {'status':200,'data':all_owners_list}
		return HttpResponse(json.dumps(data),content_type="application/json")

class DeleteOwner(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to delete owner.'}
			return HttpResponse(json.dumps(data),content_type="application/json")	

		try:
			owner_object = Owner.objects.get(username=username)
			owner_object.delete()
			data = {'status':200,'msg':'Owner account deleted succesfully.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except:
			data = {'status':200,'msg':'User not exits.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

class UpdateOwner(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to update owner.'}
			return HttpResponse(json.dumps(data),content_type="application/json")	
		
		if 'first_name' in request.data:
			first_name = request.data['first_name']
		else:
			first_name = None

		if 'last_name' in request.data:
			last_name = request.data['last_name']
		else:
			last_name = None

		if 'email' in request.data:
			email = request.data['email']
		else:
			email = None

		if 'password' in request.data:
			password = request.data['password']
		else:
			password = None

		try:
			owner_object = Owner.objects.get(username=username)
			if first_name:
				owner_object.first_name = first_name
			if last_name:
				owner_object.last_name = last_name
			if email:
				owner_object.email = email
			if password:
				owner_object.password = password
			owner_object.save()

			data = {'status':200,'msg':'Owner account updated succesfully.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except:
			data = {'status':200,'msg':'User not exits.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

class CreateHomeAssests(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to home assests.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		if 'name' in request.data:
			name = request.data['name']
		else:
			name = None

		if 'availabilty' in request.data:
			availabilty = request.data['availabilty']
		else:
			availabilty = True

		if 'rate_per_day' in request.data:
			rate_per_day = request.data['rate_per_day']
		else:
			rate_per_day = None

		if 'location' in request.data:
			location = request.data['location']
		else:
			location = None

		try:
			owner_object = Owner.objects.get(username=username)
			home_assest_object = HomeAssests(name=name,availabilty=availabilty,rate_per_day=rate_per_day,
				location=location,owner=owner_object)
			home_assest_object.save()
			data = {'status':200,'msg':'Home assest created succesfully.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except:
			data = {'status':200,'msg':'User not exits.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

class ListHomeAssests(APIView):

	def get(self, request,format=None):
		all_home_assests = HomeAssests.objects.all()
		all_home_assests = list(all_home_assests)
		all_home_assests_list = [{'id':item.id,'name':item.name,'availabilty':item.availabilty,'location':item.location,
		'rate_per_day':item.rate_per_day} for item in all_home_assests]	
		data = {'status':200,'data':all_home_assests_list}
		return HttpResponse(json.dumps(data),content_type="application/json")

class DeleteHomeAssests(APIView):

	def post(self, request, format=None):
		if 'id' in request.data:
			id_ = request.data['id']
		else:
			data = {'status':500,'msg':'id must required to delete assests.'}
			return HttpResponse(json.dumps(data),content_type="application/json")	

		try:
			home_assest_object = HomeAssests.objects.get(id=id_)
			home_assest_object.delete()
			data = {'status':200,'msg':'Home assest deleted succesfully.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except:
			data = {'status':200,'msg':'id not exits.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

class UpdateHomeAssests(APIView):

	def post(self, request, format=None):
		print request.data
		if 'id' in request.data:
			id_ = request.data['id']
		else:
			data = {'status':500,'msg':'id must required to update home assests.'}
			return HttpResponse(json.dumps(data),content_type="application/json")	
		
		if 'name' in request.data:
			name = request.data['name']
		else:
			name = None

		if 'availabilty' in request.data:
			availabilty = request.data['availabilty']
		else:
			availabilty = True

		if 'rate_per_day' in request.data:
			rate_per_day = request.data['rate_per_day']
		else:
			rate_per_day = None

		if 'location' in request.data:
			location = request.data['location']
		else:
			location = None

		try:
			home_assest_object = HomeAssests.objects.get(id=id_)
			if name:
				home_assest_object.name = name
			if availabilty:
				home_assest_object.availabilty = availabilty
			if rate_per_day:
				home_assest_object.rate_per_day = rate_per_day
			if location:
				home_assest_object.location = location
			home_assest_object.save()

			data = {'status':200,'msg':'Home assest updated succesfully.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except:
			data = {'status':200,'msg':'id not exits.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

class CreateRenter(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to create renter.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		if 'first_name' in request.data:
			first_name = request.data['first_name']
		else:
			first_name = None

		if 'last_name' in request.data:
			last_name = request.data['last_name']
		else:
			last_name = None

		if 'email' in request.data:
			email = request.data['email']
		else:
			email = None

		if 'password' in request.data:
			password = request.data['password']
		else:
			password = None

		renter_object = Renter(username=username,first_name=first_name,
			last_name=last_name,email=email,password=password)
		renter_object.save()
		data = {'status':200,'msg':'Renter account created succesfully.'}
		return HttpResponse(json.dumps(data),content_type="application/json")

class ListRenter(APIView):

	def get(self, request,format=None):
		all_renters = Renter.objects.all()
		all_renters = list(all_renters)
		all_renters_list = [{'username':item.username,'email':item.email,'first_name':item.first_name,
		'last_name':item.last_name} for item in all_renters]	
		data = {'status':200,'data':all_renters_list}
		return HttpResponse(json.dumps(data),content_type="application/json")

class DeleteRenter(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to delete renter.'}
			return HttpResponse(json.dumps(data),content_type="application/json")	

		try:
			renter_object = Renter.objects.get(username=username)
			renter_object.delete()
			data = {'status':200,'msg':'Renter account deleted succesfully.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except:
			data = {'status':200,'msg':'User not exits.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

class UpdateRenter(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to update Renter.'}
			return HttpResponse(json.dumps(data),content_type="application/json")	
		
		if 'first_name' in request.data:
			first_name = request.data['first_name']
		else:
			first_name = None

		if 'last_name' in request.data:
			last_name = request.data['last_name']
		else:
			last_name = None

		if 'email' in request.data:
			email = request.data['email']
		else:
			email = None

		if 'password' in request.data:
			password = request.data['password']
		else:
			password = None

		try:
			renter_object = Renter.objects.get(username=username)
			if first_name:
				renter_object.first_name = first_name
			if last_name:
				renter_object.last_name = last_name
			if email:
				renter_object.email = email
			if password:
				renter_object.password = password
			renter_object.save()

			data = {'status':200,'msg':'Renter account updated succesfully.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except:
			data = {'status':200,'msg':'User not exits.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
