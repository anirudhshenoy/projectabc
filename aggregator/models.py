from django.db import models


class content (models.Model):

    GRADE_CHOICES = (
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
    )
    grade = models.CharField(
        max_length=3,
        choices=GRADE_CHOICES,
        default='5th',
    )

    SUBJECT_CHOICES = (
        ('Science', 'Science'),
        ('Mathematics', 'Mathematics'),
        ('English', 'English'),
    )

    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        default='Science',
    )

    CONTENT_TYPE_CHOICES = (
        ('Video','Video'),
        ('Article', 'Article'),
        ('Other', 'Other'),
    )
    contentType = models.CharField(
        max_length=10,
        choices=CONTENT_TYPE_CHOICES,
        default='Video',
    )
    chapterNumber = models.CharField(max_length=2)
    contentLink = models.CharField(max_length=1000)
    contentTitle = models.CharField(max_length=1000, default="NA TITLE")
    longDescription = models.TextField(max_length=10000)
    shortDescription = models.TextField(max_length=10000)

    def __str__(self):
        return self.contentTitle
