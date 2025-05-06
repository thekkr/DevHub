from django.db import models

class SoftwareProduct(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class SoftwareImage(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(
        SoftwareProduct, 
        on_delete=models.CASCADE,
        related_name='software_images'
    )
    kernel_compilation_flag = models.BooleanField(default=False)
    super_image_flag = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('name', 'product')
    
    def __str__(self):
        return f"{self.name} ({self.product.name})"

class RepoSync(models.Model):
    command = models.TextField()
    software_image = models.OneToOneField(
        SoftwareImage,
        on_delete=models.CASCADE,
        related_name='repo_sync'
    )
    
    def __str__(self):
        return f"RepoSync for {self.software_image.name}"

class KernelCompilation(models.Model):
    VARIANT_CHOICES = [
        ('def', 'Debug'),
        ('perf', 'Performance'),
        # Add more variants if needed
    ]
    
    command = models.TextField()
    variant = models.CharField(
        max_length=255,
        choices=VARIANT_CHOICES
    )
    software_image = models.ForeignKey(
        SoftwareImage,
        on_delete=models.CASCADE,
        related_name='kernel_compilations'  # Note plural name now
    )
    
    class Meta:
        unique_together = ('variant', 'software_image')  # Ensures one command per variant per image
    
    def __str__(self):
        return f"{self.get_variant_display()} Kernel for {self.software_image.name}"

class BuildCompilation(models.Model):
    command = models.TextField()
    software_image = models.OneToOneField(
        SoftwareImage,
        on_delete=models.CASCADE,
        related_name='vendor_compilation'
    )
    
    def __str__(self):
        return f"VendorCompilation for {self.software_image.name}"


class SuperImage(models.Model):
    command = models.TextField()
    software_image = models.OneToOneField(
        SoftwareImage,
        on_delete=models.CASCADE,
        related_name='super_image',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"SuperImage for {self.software_image.name}"