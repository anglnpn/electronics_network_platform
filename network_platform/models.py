from django.db import models
from django.core.exceptions import ValidationError


class Contact(models.Model):
    """
    Модель для контактной информации.
    Для завода, розничной сети и
    индивидуального предпринимателя.
    """
    email = models.CharField(
        max_length=200, verbose_name='email')
    country = models.CharField(
        max_length=200, verbose_name='страна')
    city = models.CharField(
        max_length=200, verbose_name='город')
    street = models.CharField(
        max_length=200, verbose_name='улица')
    number_home = models.PositiveIntegerField(
        verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}, {self.country}, ' \
               f'{self.city}, {self.street},' \
               f'{self.number_home}'

    class Meta:
        verbose_name = 'контактные данные'
        verbose_name_plural = 'контактные данные'

    class Meta:
        verbose_name = 'контактные данные'
        verbose_name_plural = 'контактные данные'


class Product(models.Model):
    """
    Модель для продукта.
    """
    name = models.CharField(
        max_length=100, verbose_name='название')
    product_model = models.CharField(
        max_length=100, verbose_name='модель')
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class ElectronicsFactory(models.Model):
    """
    Модель для создания завода.
    Модель завода является поставщиком
    для всех других иерархий.
    """
    name = models.CharField(
        max_length=100, verbose_name='название')
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE,
        verbose_name='контактные данные')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='продукт')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class RetailNetwork(models.Model):
    """
    Модель для создания розничной сети.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='название розничной сети')
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE,
        verbose_name='контактные данные')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='продукт')
    provider_factory = models.ForeignKey(
        ElectronicsFactory, on_delete=models.CASCADE,
        verbose_name='поставки с завода')
    debt = models.DecimalField(
        default=0.00, max_digits=10,
        decimal_places=2, verbose_name='задолженность')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'


class SoleTrader(models.Model):
    """
    Модель для индивидуального предпринимателя.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='название и предпринимателя')
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE,
        verbose_name='контактные данные')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='продукт')
    provider_factory = models.ForeignKey(
        ElectronicsFactory, on_delete=models.CASCADE,
        verbose_name='поставки с завода',
        blank=True, null=True)
    provider_retailer = models.ForeignKey(
        RetailNetwork, on_delete=models.CASCADE,
        verbose_name='поставки с розничной сети',
        blank=True, null=True)
    debt = models.DecimalField(
        default=0.00, max_digits=10,
        decimal_places=2, verbose_name='задолженность')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    def clean(self):
        """
        Метод проверяет, что заполнено
        одно поле: завод или розничная сеть.
        """
        if self.provider_factory and self.provider_retailer:
            raise ValidationError('Может быть только один поставщик!')
        elif not self.provider_factory and not self.provider_retailer:
            raise ValidationError(
                'Необходимо заполнить одно поле: '
                'завод или розничная сеть.'
            )

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'
