from django.db import models


class Category(models.Model):
    """
    A class for the category model
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        Args:
            self (object): self.
        Returns:
            The category friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    A class for the product model
    """
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=254
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    colour = models.CharField(
        max_length=254
    )
    sku = models.CharField(
        max_length=254
    )
    description = models.TextField(
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    pre_sale_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the product name
        Args:
            self (object): self.
        Returns:
            The product name string
        """
        return self.name
