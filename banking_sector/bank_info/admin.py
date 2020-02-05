from django.contrib import admin

from .models import BankInfo,BranchInfo


class BranchInfoAdmin(admin.ModelAdmin):

	list_display=['branch_name','ifsc','bank','city','district','state','address']





class BankInfoAdmin(admin.ModelAdmin):

	list_display=['bank_id','bank_name']