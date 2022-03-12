from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField("Наименование", max_length=200)
    slug = models.SlugField("Адрес", unique=True, null=True)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Группa"
        verbose_name_plural = "Группы"
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Группа",
        help_text="Выберите группу",
    )
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self) -> str:
        return self.text[:15]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self) -> str:
        return self.text[:20]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Избранный автор",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "author"], name="unique_relationships"
            ),
            models.CheckConstraint(
                name="prevent_self_follow",
                check=~models.Q(user=models.F("author")),
            ),
        ]

    def __str__(self) -> str:
        return f"{self.user} подписан на {self.author}"
