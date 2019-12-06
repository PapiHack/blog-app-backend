from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
          model  = Article
        # fields = '__all__'
          fields = ['id', 'titre', 'contenu', 'auteur', 'created_at']