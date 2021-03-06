from django.contrib import admin

from models import *
from forms import *
from django.utils.translation import ugettext, ugettext_lazy as _

# class accomodationTypeAdminCreation(admin.ModelAdmin):
# 	model = accomodationTypeCreation

# class accomodationStarAdminCreation(admin.ModelAdmin):
# 	model = accomodationStarCreation

# class accomodationTypeAdmin(admin.ModelAdmin):
# 	model = accomodationType
# 	form = accomodationTypeForm

# class modeOfTransportCreationAdmin(admin.ModelAdmin):
# 	model = modeOfTransportCreation

# class modeOfTransportAdmin(admin.ModelAdmin):
# 	model = modeOfTransport

# class transportTypeCreationAdmin(admin.ModelAdmin):
# 	model = transportTypeCreation

# admin.site.register(accomodationTypeCreation,accomodationTypeAdminCreation)
# admin.site.register(accomodationStarCreation,accomodationStarAdminCreation)
# admin.site.register(accomodationType,accomodationTypeAdmin)
# admin.site.register(modeOfTransportCreation,modeOfTransportCreationAdmin)
# admin.site.register(modeOfTransport,modeOfTransportAdmin)
# admin.site.register(transportTypeCreation,transportTypeCreationAdmin)
class AccomodationStarAndTypeInline(admin.TabularInline):
	# model = AccomodationType.accomodation_type.through
	model = AccomodationStarAndType

class AccomodationTypeAdmin(admin.ModelAdmin):
	pass

class AccomodationStarAdmin(admin.ModelAdmin):
	fieldsets = (
	(_('Customer Details'), {'fields': ['accomodation_star']}),
	# (_('Status and Dates'), {'fields': ('accomodation_star')}),
	)

	inlines = [AccomodationStarAndTypeInline]

class ModeOfTransportAdmin(admin.ModelAdmin):
	pass

class TransportTypeAdmin(admin.ModelAdmin):
	pass

# class AccomodationStarAndTypeAdmin(admin.ModelAdmin):
# 	pass
	
admin.site.register(AccomodationType,AccomodationTypeAdmin)
admin.site.register(AccomodationStar,AccomodationStarAdmin)
admin.site.register(ModeOfTransport,ModeOfTransportAdmin)
admin.site.register(TransportType,TransportTypeAdmin)
# admin.site.register(AccomodationStarAndType,AccomodationStarAndTypeAdmin)