from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(Base):
    tittle = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.tittle


class Avaliable(Base):
    course = models.ForeignKey(Course, related_name='avaliables', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comments = models.TextField(blank=True, default='')
    avaliable = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliable'
        verbose_name_plural = 'Avaliables'
        unique_together = ['email', 'course']

    def __str__(self):
        return f'{self.name} is available for the course {self.course} with a grade of {self.available}'

