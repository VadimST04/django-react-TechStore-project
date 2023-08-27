from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from base.models import Product


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    This serializer extends the TokenObtainPairSerializer from the SimpleJWT library.
    It adds user-specific data to the token response, expanding the default return.
    """

    def validate(self, attrs):
        """
        This method extends the base validation provided by TokenObtainPairSerializer.
        It includes additional user-specific data in the response data.
        :param attrs: The dictionary which contains token and user data.
        :return: Returns token data and additional fields.
        """
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for key, value in serializer.items():
            data[key] = value

        return data


class UserSerializer(serializers.ModelSerializer):
    """
    This serializer converts User model instances to JSON representation and includes additional
    fields, such as the user's name and admin status.
    """

    name = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """
        model: The User model class to be serialized.
        fields: The list of fields to be included in the serialized representation.
        """

        model = User
        fields = ['id', 'username', 'email', 'name', 'is_admin']

    def get_name(self, obj):
        """
        Get the user's name.
        :param obj: The User instances.
        :return: Returns the user's name based on their first name or email.
        """
        return obj.first_name if obj.first_name else obj.email

    def get_is_admin(self, obj):
        """
        Get is_admin status.
        :param obj: The User instances.
        :return: Returns True if the user is an admin user, otherwise, returns False.
        """
        return obj.is_staff


class UserSerializerWithToken(serializers.ModelSerializer):
    """
    Serializer for user data with authentication token.
    This serializer converts User model instances to JSON representation and includes additional
    fields, such as the user's name, admin status, and an authentication token.
    """

    name = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """
        model: The User model class to be serialized.
        fields: The list of fields to be included in the serialized representation.
        """

        model = User
        fields = ['id', 'username', 'email', 'name', 'is_admin', 'token']

    def get_name(self, obj):
        """
        Get the user's name.
        :param obj: The User instances.
        :return: Returns the user's name based on their first name or email.
        """
        return obj.first_name if obj.first_name else obj.email

    def get_is_admin(self, obj):
        """
        Get is_admin status.
        :param obj: The User instances.
        :return: Returns True if the user is an admin user, otherwise, returns False.
        """
        return obj.is_staff

    def get_token(self, obj):
        """
        Get an authentication token for the user.
        :param obj:
        :return: Returns a generated authentication token for the user.
        """
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    """
    This serializer converts Product model instances to JSON representation.
    """

    class Meta:
        """
        model: The Product model class to be serialized.
        fields: The list of fields to be included in the serialized representation
        (in this case all fields).
        """

        model = Product
        fields = '__all__'
