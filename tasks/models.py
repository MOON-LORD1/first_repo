from django.db import models
from django.contrib.auth.models import User

default_title = "This is tasks title"
default_description = "This is Default Description. Lorem ipsum dolor"
default_code = "# write your code here"

DIFFICULTY_CHOICES = (
    ("1st Dan", "1st Dan"),
    ("2nd Dan", "2nd Dan"),
    ("3rd Dan", "3rd Dan"),
    ("4th Dan", "4th Dan"),
    ("5th Dan", "5th Dan"),
)

COURSES_GROUPS = (
    ("Python 1", "Python 1"),
    ("Python 2", "Python 2"),
    ("Python 3", "Python 3"),
    ("Python 4", "Python 4"),
)

STATUS_CHOICES = (
    ("Все верно", "Все верно"),
    ("Неверное решение", "Неверное решение"),
    ("На проверке","На проверке")
)



class Task(models.Model):
    title = models.CharField("Название", max_length=80, default=default_title)
    description = models.TextField("Описание", max_length=8000, default=default_description)
    difficulty = models.CharField("Сложность", choices=DIFFICULTY_CHOICES, default="1st Dan", max_length=10)
    created_at = models.DateField("Дата", auto_created=True)
    input_data = models.TextField("Входные данные", max_length=200, default="Введите входные данные" )
    output_data = models.TextField("Выходные данные", max_length=200, default="Введите выходные данные")


    def __str__(self):
        return f'{self.difficulty}: {self.title}'

# class Answer(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
#     code = models.TextField("Код", max_length=3000, default=default_code)
#     stat = models.CharField("Статус кода", choices=STATUS_CHOICES, default="Нет статуса", max_length=60)

#     def __str__(self):
#         return f'{self.author}, {self.task.title}'
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if self.stat == "Все верно":
#             profile = Profile.objects.get(user=self.author)
#             profile.solved_problems += 1
#             profile.save()

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    code = models.TextField("Код", max_length=3000, default=default_code)
    stat = models.CharField("Статус кода", choices=STATUS_CHOICES, default="Нет статуса", max_length=60)

    def save(self, *args, **kwargs):
        # Check if the answer is marked as "Все верно" and if the user has not already solved this task
        if self.stat == "Все верно" and not Answer.objects.filter(author=self.author, task=self.task, stat="Все верно").exists():
            # Increment solved_problems only if the user has not already solved this task
            profile = Profile.objects.get(user=self.author)
            profile.solved_problems += 1
            profile.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author} -> {self.task}'


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    solved_problems = models.IntegerField("Решенные задачи", default=0)
    groups = models.CharField("Группа", choices=COURSES_GROUPS, max_length=20)
    birth_date = models.DateField("День рождение", null=True, blank=True)
    schedule_day = models.CharField("Расписание(дни)", max_length=100, blank=False, default="ПН-СР-ПТ")
    schedule_time = models.CharField("Расписание(часы)", max_length=100, blank=False, default="13:00-18:00")
    pfp = models.ImageField("Аватарка", default='/profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f"Profile {self.user.username}"

    
