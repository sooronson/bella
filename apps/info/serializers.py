from rest_framework import serializers

from .models import About, Image, Contact, AboutDescription


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'about', 'image')


class AboutDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutDescription
        fields = ('description',)


class AboutSerializer(serializers.ModelSerializer):
    images_about = ImageSerializer(
        many=True, read_only=True
    )
    about_descriptions = AboutDescriptionSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = About
        fields = (
            'id', 'title',
            'images_about', 'about_descriptions'
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'phone_number', 'email', 'address', 'ok', 'instagram',
            'facebook', 'vk'
        )
