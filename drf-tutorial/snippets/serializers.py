from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        fields = [
            "url",
            "id",
            "highlight",
            "creator",
            "title",
            "code",
            "line_no",
            "prog_lang",
            "style",
        ]
        model = Snippet
