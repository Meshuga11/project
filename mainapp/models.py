from django.db import models


class MainPageEls(models.Model):
    title = models.CharField("Название профессии", max_length=100)
    description = models.TextField("Описание", default=None)
    draft = models.BooleanField("Черновик", default=False)


class DemandPageEls(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    slr_img = models.ImageField("Динамика оклада по годам", upload_to="stat_img/")
    count_vac_img = models.ImageField("Количество вакансий по годам", upload_to="stat_img/")
    table = models.FileField("Таблица динамики оклада и количества вакансий по годам", upload_to="CSVs/", default=None)
    draft = models.BooleanField("Черновик", default=False)


class GeographyPageEls(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    slr_img = models.ImageField("Динамика оклада по городам", upload_to="stat_img/")
    count_vac_img = models.ImageField("Количество вакансий по городам", upload_to="stat_img/")
    slr_table = models.FileField("Таблица уровня оклада по городам", upload_to="CSVs/", default=None)
    count_vac_table = models.FileField("Таблица долей вакансий по городам", upload_to="CSVs/", default=None)
    draft = models.BooleanField("Черновик", default=False)


class KeySkillsPageEls(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    key_skills_img = models.ImageField("Топ 10 навыков", upload_to="stat_img/")
    draft = models.BooleanField("Черновик", default=False)