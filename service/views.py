from django.shortcuts import render


#======================== Authorization =========
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
#========================== =======================

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

# ======================= filters ===============
from rest_framework.filters import SearchFilter, OrderingFilter
# ===============================================


# ===================== My Models ===============
from service.models import Company, Day, Slot, Appointment
# ===============================================

# ===================== My Serializers (LIST / DETAIL)===============
from .serializers import (
	CompanyListSerializer, 
	DayListSerializer, 
	SlotListSerializer, 
	AppointmentListSerializer, 
	CompanyDetailSerializer, 
	DayDetailSerializer, 
	SlotDetailSerializer, 
	AppointmentDetailSerializer
	)
# =======================My Serializers (CREATE)=====================
from .serializers import (
	CompanyCreateSerializer,
	DayCreateSerializer,
	SlotCreateSerializer,
	AppointmentCreateSerializer
	)
# ===================================================================



#============== LIST API =============================
class CompanyListView(ListAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name',]

# --------------------

class DayListView(ListAPIView):
	queryset = Day.objects.all()
	serializer_class = DayListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['company',]

# --------------------

class SlotListView(ListAPIView):
	queryset = Slot.objects.all()
	serializer_class = SlotListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['day',]

# --------------------

class AppointmentListView(ListAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['user',]
#=====================================================



#============= DETAIL API ============================
class CompanyDetailView(RetrieveAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'companydetail_id'

# --------------------

class DayDetailView(RetrieveAPIView):
	queryset = Day.objects.all()
	serializer_class = DayDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'daydetail_id'

# --------------------

class SlotDetailView(RetrieveAPIView):
	queryset = Slot.objects.all()
	serializer_class = SlotDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'slotdetail_id'

# --------------------

class AppointmentDetailView(RetrieveAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'appointmentdetail_id'
#=====================================================


#============= CREATE API ============================
class CompanyCreateView(CreateAPIView):
	serializer_class = CompanyCreateSerializer
	permission_classes = [IsAuthenticated]

# -----------------

class DayCreateView(CreateAPIView):
	serializer_class = DayCreateSerializer
	permission_classes = [IsAuthenticated]

# -----------------

class SlotCreateView(CreateAPIView):
	serializer_class = SlotCreateSerializer
	permission_classes = [IsAuthenticated]

# -----------------

class AppointmentCreateView(CreateAPIView):
	serializer_class = AppointmentCreateSerializer
	permission_classes = [IsAuthenticated]

#=====================================================

#============= UPDATE API ============================
class CompanyUpdateView(RetrieveUpdateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'companyupdate_id'

# -----------------

class DayUpdateView(RetrieveUpdateAPIView):
	queryset = Day.objects.all()
	serializer_class = DayCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'dayupdate_id'

# -----------------

class SlotUpdateView(RetrieveUpdateAPIView):
	queryset = Slot.objects.all()
	serializer_class = SlotCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'slotupdate_id'

# -----------------

class AppointmentUpdateView(RetrieveUpdateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'appointmentupdate_id'



#=====================================================

#============= DELETE API ============================
class CompanyDeleteView(DestroyAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'companydelete_id'
	permission_classes = [IsAuthenticated]

# ------------------

class DayDeleteView(DestroyAPIView):
	queryset = Day.objects.all()
	serializer_class = DayListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'daydelete_id'
	permission_classes = [IsAuthenticated]

# ------------------

class SlotDeleteView(DestroyAPIView):
	queryset = Slot.objects.all()
	serializer_class = SlotListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'slotdelete_id'
	permission_classes = [IsAuthenticated]

# ------------------

class AppointmentDeleteView(DestroyAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'appointmentdelete_id'
	permission_classes = [IsAuthenticated]

#=====================================================


