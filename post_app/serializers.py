from rest_framework import serializers
from post_app.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    post_images = serializers.ListSerializer(
        child=serializers.ImageField(),
        write_only=True
    )

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        post_images = validated_data.pop("post_images")
        instance = super().create(validated_data)
        for post_image in post_images:
            PostImage.objects.create(post=instance, image=post_image)
        return instance


class PostListSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

