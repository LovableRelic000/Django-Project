from django.db.backends.mysql.features import DatabaseFeatures

# Permitir compatibilidad con MySQL 8.0 en Django 6
DatabaseFeatures.minimum_database_version = (8, 0, 0)
