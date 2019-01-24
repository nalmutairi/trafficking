from rest_framework import serializers

from service.models import Company, Day, Slot, Appointment

from django.contrib.auth.models import User

# class UserCreateSerializer(serializers.ModelSerializer):
# 	password = serializers.CharField(write_only=True)
# 	class Meta:
# 		model = User
# 		fields = ['first_name', 'last_name', 'email', 'password']

# 	def create(self, validated_data):
# 		user = validated_data['username']
# 		_pass = validated_data['password']
# 		new_user = User(username = user)
# 		new_user.set_password(_pass)
# 		new_user.save()
# 		return validated_data


# check the below codes


#================== LIST SERIALIZERS ======================
class CompanyListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'companydetail',
		lookup_field = 'id',
		lookup_url_kwarg = 'companydetail_id'
		)

	slogan = serializers.SerializerMethodField()

	class Meta:
		model = Company
		fields = ['name', 'logo', 'detail', 'slogan',]

	def get_slogan(self, obj):
		return "anything"

# -----------------------

class DayListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'daydetail',
		lookup_field = 'id',
		lookup_url_kwarg = 'daydetail_id'
		)

	class Meta:
		model = Day
		fields = ['company', 'name', 'detail',]

# ------------------------

class SlotListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'slotdetail',
		lookup_field = 'id',
		lookup_url_kwarg = 'slotdetail_id'
		)

	class Meta:
		model = Slot
		fields = ['day', 'is_available', 'detail',]

# ------------------------

class AppointmentListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'appointmentdetail',
		lookup_field = 'id',
		lookup_url_kwarg = 'appointmentdetail_id'
		)

	class Meta:
		model = Appointment
		fields = ['user', 'slot', 'detail',]


#==========================================================
#==========================================================



#================== DETAIL SERIALIZERS ====================
class CompanyDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'

# ------------------

class DayDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Day
		fields = '__all__'

# ----------------

class SlotDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Slot
		fields = '__all__'

# ----------------

class AppointmentDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = '__all__'
#==========================================================
#==========================================================


#================== CREATE SERIALIZERS ====================
class CompanyCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'

# ----------------

class DayCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Day
		exclude = ['company',]

# ----------------

class SlotCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Slot
		fields = '__all__'

# ----------------

class AppointmentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		exclude = 'user'
#==========================================================
#==========================================================

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password")

        return data

class UserListSerializer(serializers.ModelSerializer):
    details = serializers.HyperlinkedIdentityField(
        view_name = "userDetail",
        lookup_field = "id",
        lookup_url_kwarg = "user_id"
        )

    class Meta:
        model = User
        fields = ['username' , 'details']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

