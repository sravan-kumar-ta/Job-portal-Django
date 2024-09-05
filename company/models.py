from django.contrib.auth import get_user_model
from django.db import models


def standardize_location_name(location):
    return location.strip().title()


class Company(models.Model):
    title = models.CharField(max_length=150)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    description = models.TextField()
    website = models.URLField(null=True)
    established_date = models.DateField(null=True)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.location = standardize_location_name(self.location)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Job(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    salary = models.PositiveIntegerField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_date_to_apply = models.DateField(null=True)
    vacancy = models.PositiveIntegerField(default=1)
    employment_type = models.CharField(
        max_length=50,
        choices=[
            ('Full-time', 'Full-time'),
            ('Part-time', 'Part-time'),
            ('Contract', 'Contract'),
            ('Freelance', 'Freelance'),
            ('Internship', 'Internship'),
        ],
        default='Full-time'
    )

    def __str__(self):
        return f"{self.title} at {self.company.title}"

    class Meta:
        ordering = ['-date_posted']
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
