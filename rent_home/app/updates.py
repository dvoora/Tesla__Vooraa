import json
from rest_framework.views import APIView
from django.shortcuts import HttpResponse
from models import Owner,HomeAssests,Renter,Bookings

class BookRoom(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to book room.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		if 'id' in request.data:
			id_ = request.data['id']
		else:
			data = {'status':500,'msg':'id must required to book room.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		if 'date_of_booking' in request.data:
			date_of_booking = request.data['date_of_booking']
		else:
			data = {'status':500,'msg':'date_of_booking must required to book room.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		try:
			renter_object = Renter.objects.get(username=username)
		except Exception, e:
			data = {'status':500,'msg':'invalid username.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		try:
			home_assest_object = HomeAssests.objects.get(id=id_)
		except Exception, e:
			data = {'status':500,'msg':'invalid home assest id.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		
		try:
			bookings_objects = Bookings.objects.get(home=home_assest_object,date_of_booking=date_of_booking)
			data = {'status':200,'msg':'Home assest already booked'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except Exception, e:
			bookings_objects = Bookings(home=home_assest_object,renter_person=renter_object,
			date_of_booking=date_of_booking)
			bookings_objects.save()
			data = {'status':200,'msg':'Home assest booked succesfully'}
			return HttpResponse(json.dumps(data),content_type="application/json")

class CheckAvailabilty(APIView):

	def post(self, request, format=None):

		if 'id' in request.data:
			id_ = request.data['id']
		else:
			data = {'status':500,'msg':'id must required to Check Availabilty.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		if 'date_to_check' in request.data:
			date_to_check = request.data['date_to_check']
		else:
			data = {'status':500,'msg':'date_to_check must required to Check Availabilty.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		try:
			home_assest_object = HomeAssests.objects.get(id=id_)
		except Exception, e:
			data = {'status':500,'msg':'invalid home assest id.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		
		try:
			bookings_objects = Bookings.objects.get(home=home_assest_object,date_of_booking=date_to_check)
			data = {'status':200,'msg':'Home assest Unavailable','value':False}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except Exception, e:
			data = {'status':200,'msg':'Home assest is avilable','value':True}
			return HttpResponse(json.dumps(data),content_type="application/json")

class CancelBookedRoom(APIView):

	def post(self, request, format=None):
		if 'username' in request.data:
			username = request.data['username']
		else:
			data = {'status':500,'msg':'usernmae must required to cancel room.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		if 'id' in request.data:
			id_ = request.data['id']
		else:
			data = {'status':500,'msg':'id must required to cancel room.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		try:
			renter_object = Renter.objects.get(username=username)
		except Exception, e:
			data = {'status':500,'msg':'invalid username.'}
			return HttpResponse(json.dumps(data),content_type="application/json")

		try:
			home_assest_object = HomeAssests.objects.get(id=id_)
		except Exception, e:
			data = {'status':500,'msg':'invalid home assest id.'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		
		try:
			bookings_objects = Bookings.objects.get(home=home_assest_object,renter_person=renter_object)
			bookings_objects.delete()
			data = {'status':200,'msg':'Booking succesfully cancelled'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except Exception, e:
			data = {'status':200,'msg':'invalide cancelling parameters'}
			return HttpResponse(json.dumps(data),content_type="application/json")