from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    # inherit from BaseUserCreateSerializer
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "email", "password", "first_name", "last_name"]
        

class UserSerializer(BaseUserSerializer):
    # inherit from BaseUserSerializer
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]