from django.db import models


class Cursus(models.Model):
  name = models.CharField(
    max_length = 50,
    blank = False,
    null  = True,
  )
  def __str__(self):
    return self.name


class Etudiant(models.Model):
  firstName = models.CharField(
    verbose_name = "Firstname",
    max_length = 255,
    blank = False,
    null = False
  )
  lastName = models.CharField(
    verbose_name = "Lastname",
    help_text = "last name of student",
    default = "???",
    max_length=255,
    blank = False,
    null = False
  )
  dateOfBirth = models.DateField(
    verbose_name = 'Date of birth',
    blank = False,
    null=  False
  )
  email = models.EmailField(
    verbose_name="Email",
    help_text = "mail of thee student",
    default = "x@y.z",
    max_length = 255,
    blank = False,
    null = False
  )
  phoneNumber = models.CharField(
    verbose_name = "Phonenumber",
    help_text = "phone number of the student",
    default = "0999999999",
    max_length = 10,
    blank = False,
    null = False
  )
  comment = models.CharField(
    verbose_name = "Comments",
    help_text = "some comment abount the student",
    default = "",
    max_length = 255,
    blank = True,
    null = False,
  )
  cursus = models.ForeignKey(
    Cursus,
    on_delete = models.CASCADE,
    null = True
  )
  def __str__(self):
    return self.first_name + " " + self.last_name


class Presence(models.Model):
  dateOfCall = models.DateField(
    verbose_name = "Date of call",
    blank = False,
    null = False
  )
  isMissing = models.BooleanField(
    verbose_name = "isMissing",
    blank = False,
    null = True
  )
  reason = models.CharField(
    verbose_name = "Reason",
    max_length = 50,
    blank = False,
    null = False
  )
  student = models.ForeignKey(
    Etudiant,
    on_delete = models.CASCADE,
    null = True
  )
  start_time = models.TimeField(
    blank = False,
    null = False
  )
  stop_time = models.TimeField(
    blank = False,
    null = False
  )