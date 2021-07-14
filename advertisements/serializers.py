from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user

        creator_id = validated_data['creator'].id

        status_open = Advertisement.objects.filter(
            creator_id=creator_id,
            status='OPEN'
        ).count()

        print(status_open)
        if status_open == 10:
            raise serializers.ValidationError("Слишком много окрытых объяалений")

        return super().create(validated_data)

    # def validate(self, data):
    #     """Метод для валидации. Вызывается при создании и обновлении."""
    #
    #     # TODO: добавьте требуемую валидацию
    #
    #     return data
