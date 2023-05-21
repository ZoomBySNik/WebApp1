from django.contrib import admin

# Register your models here.
from .models import Company, Product, ProductInstance, Status

class ProductInstanceInLine(admin.TabularInline):
    model=ProductInstance
class ProductAdmin(admin.ModelAdmin):
    list_display=('title','description', 'weight', 'company', 'show_count')
    list_filter=('title','company')
    inlines=[ProductInstanceInLine]
    search_fields = ('title__startswith',)
    def show_count(self, obj):
        from django.db.models import Count
        result = ProductInstance.objects.filter(product=obj).aggregate(Count('product'))
        return result['product__count']
    show_count.short_desription = 'Количество, шт'
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display=('inv_number','product','status')
    list_filter=('product','status')
    fieldsets=(
        ('Экземпляр продукта',{
            'fields':('inv_number', 'product')
        }),
        ('Статус и окончание его действия',{
            'fields':('custumer','status','due_back')
        })
    )
admin.site.register(Product, ProductAdmin)
admin.site.register(Company)
admin.site.register(Status)
admin.site.register(ProductInstance, ProductInstanceAdmin)