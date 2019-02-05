from rest_framework import serializers

from service.models import (
	Category,
	Company, 
	Day, 
	Slot, 
	Address)

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


class CategoryListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):
	category = serializers.SerializerMethodField()
	class Meta: 
		model = Company
		fields = '__all__'


	def get_category(self, obj):
		return obj.category.name


class SlotListSerializer(serializers.ModelSerializer):
	date = serializers.SerializerMethodField()
	class Meta:
		model = Slot
		exclude = ['day',]

	def get_date(self, obj):
		return obj.day.name

class SlotDetailSerializer(serializers.ModelSerializer):
	date = serializers.SerializerMethodField()
	class Meta:
		model = Slot
		exclude = ['day' ,]

	def get_date(self, obj):
		return obj.day.name

class DayDetailSerializer(serializers.ModelSerializer):
	slots = SlotDetailSerializer(many=True)
	class Meta:
		model = Day
		fields = '__all__'


class CompanyDetailSerializer(serializers.ModelSerializer):
	days = DayDetailSerializer(many = True)
	class Meta:
		model = Company
		fields = '__all__'


class AddressDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'


## used for slot update view 
class SlotCreateSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Slot
		fields = '__all__'

class SlotUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Slot
		fields = ['user',]

class AddressCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		exclude = ['user', ]

class AddressListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, email= email, first_name = first_name, last_name = last_name)
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



