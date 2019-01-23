from rest_framework import serializers

from users.models import User , Relationship


class FollowerSerializer(serializers.ModelSerializer):
    from_user = serializers.StringRelatedField()
    class Meta:
        model = Relationship
        fields = [
            'from_user_id','from_user','is_deleted','is_agree']

class FollowingSerializer(serializers.ModelSerializer):
    to_user = serializers.StringRelatedField()
    class Meta:
        model = Relationship
        fields = [
            'to_user_id','to_user','is_agree','is_deleted'
        ]





class UserSerializer(serializers.ModelSerializer):
    following = FollowingSerializer(read_only=True, many=True)
    follower = FollowerSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','is_public','introduction','password','follower','following']

    def create(self, validated_data):
        user = super().create(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()

        return user

    def update(self, instance,vallidated_data):
        user =super().update(instance, vallidated_data)
        self.set_password(User, vallidated_data)
        return  user

class RelationshipSerializer():

    class Meta:
        model = Relationship
        fields = '__all__'

    def validate(self,data):
        if data['from_user'] == data['to_user']:
            raise serializers.ValidationError('不可以追蹤自己')

        return data


