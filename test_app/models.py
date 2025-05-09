from django.db import models
from datetime import date



# Create your models here.
from django.contrib.auth.models import User
from .managers import CustomUserManager


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
#from django.utils.translation import ugettext_lazy as _



class CustomUser(AbstractUser, PermissionsMixin):
    #username=None
    email=models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    def __str__(self):
        return self.email
    
    
class geomap(models.Model):  
    map_id = models.AutoField(primary_key=True)
    map_name = models.CharField(max_length=100,blank=True, null=True)
    geodata=models.FileField(null=True, blank=True, upload_to='maps/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # Add user field activity_name


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100,blank=True, null=True)
    organization = models.CharField(max_length=100,blank=True, null=True)
    type = models.CharField(max_length=20, choices=[('Meeting', 'Meeting'), ('Training', 'Training'),('Exposure Visit', 'Exposure Visit'), ('Workshop', 'Workshop'),('Demonstration', 'Demonstration'), ('External Visit', 'External Visit'), ('Other', 'Other')],blank=True, null=True)
    from_date = models.DateField(default=date.today)
    to_date = models.DateField(default=date.today)
    location = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    resource_persons = models.CharField(max_length=100,blank=True, null=True)
    male_participants = models.IntegerField(default=0)
    female_participants = models.IntegerField(default=0)
    total_participants = models.IntegerField(default=0)
    photo=models.ImageField(null=True, blank=True, upload_to='images/' )
    document=models.FileField(null=True, blank=True, upload_to='documents/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # Add user field



class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=100,blank=True, null=True)
    type = models.CharField(max_length=20, choices=[('Photos', 'Photos'), ('Videos', 'Videos'),('Media Coverage', 'Media Coverage')],blank=True, null=True)
    date = models.DateField(default=date.today)

    location = models.CharField(max_length=100,blank=True, null=True)

    document=models.ImageField(null=True, blank=True, upload_to='images/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # Add user field activity_name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    contact_no = models.PositiveIntegerField(blank=True, null=True)
    email_id = models.EmailField(max_length=50,blank=True, null=True)
    work_location = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    photo=models.ImageField(null=True, blank=True, upload_to='images/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # 

class Resources(models.Model):
    resource_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, choices=[('IEC Material', 'IEC Material'), ('Training Modules', 'Training Modules'),('Training Material', 'Training Material'),('Reports', 'Reports')],blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=100,blank=True, null=True)
    document=models.FileField(null=True, blank=True, upload_to='documents/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # 


class Farmersdata(models.Model):
    id = models.CharField(max_length=41, primary_key=True)
    date_widget = models.DateTimeField(blank=True, null=True)
    district = models.CharField(max_length=9,blank=True, null=True)
    ngo = models.CharField(max_length=4,blank=True, null=True)
    surveyer_name = models.CharField(max_length=17,blank=True, null=True)
    designation = models.CharField(max_length=16,blank=True, null=True)
    sub_district = models.CharField(max_length=10,blank=True, null=True)
    revenue_village = models.CharField(max_length=10,blank=True, null=True)
    gp = models.CharField(max_length=12,blank=True, null=True)  # Gram Panchayat
    village = models.CharField(max_length=12,blank=True, null=True)
    farmer_name = models.CharField(max_length=28,blank=True, null=True)
    father_husband_name = models.CharField(max_length=25,blank=True, null=True)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=2,blank=True, null=True)
    sub_classification = models.CharField(max_length=8,blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    primary_occupation = models.CharField(max_length=13,blank=True, null=True)
    primary_occupation_other = models.CharField(max_length=28, blank=True, null=True)
    job_card_number = models.IntegerField(blank=True, null=True)
    income_sources = models.CharField(max_length=64,blank=True, null=True)
    income_sources_other = models.CharField(max_length=27, blank=True, null=True)
    land_owned = models.CharField(max_length=3,blank=True, null=True)
    total_land_owned = models.DecimalField(max_digits=19, decimal_places=17,blank=True, null=True)
    land_leased_in = models.CharField(max_length=3,blank=True, null=True)
    land_leased_out = models.CharField(max_length=3,blank=True, null=True)
    livestock_owned = models.CharField(max_length=3,blank=True, null=True)
    irrigation_sources = models.CharField(max_length=3,blank=True, null=True)
    type_irrigation_sources = models.CharField(max_length=25,blank=True, null=True)
    type_irrigation_sources_other = models.CharField(max_length=12, blank=True, null=True)
    job_card_owned = models.CharField(max_length=3,blank=True, null=True)
    is_women_headed_family = models.CharField(max_length=3,blank=True, null=True)
    is_single_women_family = models.CharField(max_length=3,blank=True, null=True)
    migration_from_family = models.CharField(max_length=3,blank=True, null=True)
    member_in_institution = models.CharField(max_length=3,blank=True, null=True)
    in_which_institution = models.CharField(max_length=75,blank=True, null=True)
    in_which_institution_other = models.CharField(max_length=31, blank=True, null=True)
    hh_has_kitchen_garden = models.CharField(max_length=3,blank=True, null=True)
    hh_head_family_photo = models.CharField(max_length=17, blank=True, null=True)

    
    class Meta:
        ordering = [
            "id", "date_widget", "district", "ngo", "surveyer_name", "designation",
            "sub_district", "revenue_village", "gp", "village", "farmer_name",
            "father_husband_name", "gender", "age", "category", "sub_classification",
            "phone_number", "primary_occupation", "primary_occupation_other",
            "job_card_number", "income_sources", "income_sources_other", "land_owned",
            "total_land_owned", "land_leased_in", "land_leased_out", "livestock_owned",
            "irrigation_sources", "type_irrigation_sources", "type_irrigation_sources_other",
            "job_card_owned", "is_women_headed_family", "is_single_women_family",
            "migration_from_family", "member_in_institution", "in_which_institution",
            "in_which_institution_other", "hh_has_kitchen_garden", "hh_head_family_photo"
        ]

    def __str__(self):
        return f"{self.farmer_name} ({self.village})"
    


from django.db import models

class hhdata(models.Model):
    s_no = models.IntegerField(null=True, blank=True)
    village = models.CharField(max_length=50, blank=True)
    head_of_the_family = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    contact_no = models.BigIntegerField(null=True, blank=True)
    sc_st_bc_oc = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=50, blank=True)
    male = models.IntegerField(null=True, blank=True)
    female = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, blank=True)
    age2 = models.IntegerField(null=True, blank=True)
    gender3 = models.CharField(max_length=50, blank=True)
    relation_with_family_head = models.CharField(max_length=50, blank=True)
    name_4 = models.CharField(max_length=50, blank=True)
    age5 = models.IntegerField(null=True, blank=True)
    gender6 = models.CharField(max_length=50, blank=True)
    relation_with_family_head7 = models.CharField(max_length=50, blank=True)
    name_8 = models.CharField(max_length=50, blank=True)
    age9 = models.IntegerField(null=True, blank=True)
    gender10 = models.CharField(max_length=50, blank=True)
    relation_with_family_head11 = models.CharField(max_length=50, blank=True)
    name_12 = models.CharField(max_length=50, blank=True)
    age13 = models.CharField(max_length=50, blank=True)
    gender14 = models.CharField(max_length=50, blank=True)
    relation_with_family_head15 = models.CharField(max_length=50, blank=True)
    name_16 = models.CharField(max_length=50, blank=True)
    age17 = models.CharField(max_length=50, blank=True)
    gender18 = models.CharField(max_length=50, blank=True)
    relation_with_family_head19 = models.CharField(max_length=50, blank=True)
    own_bore_public_bore_dug_well_pipeline = models.CharField(max_length=50, blank=True)
    normal_salty_medium_salt_low_salt = models.CharField(max_length=50, blank=True)
    in_which_month_water_availability_becomes_low = models.CharField(max_length=50, blank=True)
    domestic_drinking_purpose = models.CharField(max_length=50, blank=True)
    column_50000_to_600000 = models.CharField(max_length=50, blank=True)
    agriculture = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    milch_animals = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sheep_goat_byp = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    bullocks = models.IntegerField(null=True, blank=True)
    labour_work = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    job = models.IntegerField(null=True, blank=True)
    business = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    other_sources = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    total_percentage_100 = models.IntegerField(null=True, blank=True)
    are_you_a_member_in_any_institution_yes_no = models.CharField(max_length=50, blank=True)
    if_yes_shg_pacs_fpo = models.CharField(max_length=50, blank=True)
    vo = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    bank = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pacs = models.IntegerField(null=True, blank=True)
    fertilizers_shop = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    money_lendors = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    neighbours_relations = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    land_type_ups_and_downs_plane = models.CharField(max_length=50, blank=True)
    soil_name_local = models.CharField(max_length=50, blank=True)
    soil_depth_in_cm = models.CharField(max_length=50, blank=True)
    cultivation_fallow_land = models.CharField(max_length=50, blank=True)
    main_crop = models.CharField(max_length=50, blank=True)
    mono_crop_poly_crop = models.CharField(max_length=50, blank=True)
    water_source = models.CharField(max_length=50, blank=True)
    crop_1 = models.CharField(max_length=50, blank=True)
    area_in_ac = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated = models.CharField(max_length=50, blank=True)
    yield_qtl_ac = models.CharField(max_length=50, blank=True)
    average_price = models.IntegerField(null=True, blank=True)
    total_income = models.IntegerField(null=True, blank=True)
    crop_2 = models.CharField(max_length=50, blank=True)
    area_in_ac20 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated21 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_22 = models.IntegerField(null=True, blank=True)
    average_price23 = models.IntegerField(null=True, blank=True)
    total_income24 = models.IntegerField(null=True, blank=True)
    crop_3 = models.CharField(max_length=50, blank=True)
    area_in_ac25 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated26 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_27 = models.CharField(max_length=50, blank=True)
    average_price28 = models.IntegerField(null=True, blank=True)
    total_income29 = models.IntegerField(null=True, blank=True)
    crop_4 = models.CharField(max_length=50, blank=True)
    area_in_ac30 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated31 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_32 = models.IntegerField(null=True, blank=True)
    average_price33 = models.IntegerField(null=True, blank=True)
    total_income34 = models.IntegerField(null=True, blank=True)
    crop_5 = models.CharField(max_length=50, blank=True)
    area_in_ac35 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated36 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_37 = models.CharField(max_length=50, blank=True)
    average_price38 = models.IntegerField(null=True, blank=True)
    total_income39 = models.IntegerField(null=True, blank=True)
    crop_140 = models.CharField(max_length=50, blank=True)
    area_in_ac41 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated42 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_43 = models.CharField(max_length=50, blank=True)
    average_price44 = models.IntegerField(null=True, blank=True)
    total_income45 = models.IntegerField(null=True, blank=True)
    crop_246 = models.CharField(max_length=50, blank=True)
    area_in_ac47 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated48 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_49 = models.CharField(max_length=50, blank=True)
    average_price50 = models.IntegerField(null=True, blank=True)
    total_income51 = models.IntegerField(null=True, blank=True)
    crop_352 = models.CharField(max_length=50, blank=True)
    area_in_ac53 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated54 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_55 = models.IntegerField(null=True, blank=True)
    average_price56 = models.IntegerField(null=True, blank=True)
    total_income57 = models.IntegerField(null=True, blank=True)
    crop_458 = models.CharField(max_length=50, blank=True)
    area_in_ac59 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated60 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_61 = models.CharField(max_length=50, blank=True)
    average_price62 = models.IntegerField(null=True, blank=True)
    total_income63 = models.IntegerField(null=True, blank=True)
    crop_564 = models.CharField(max_length=50, blank=True)
    area_in_ac65 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rainfed_irrigated66 = models.CharField(max_length=50, blank=True)
    yield_qtl_ac_67 = models.CharField(max_length=50, blank=True)
    average_price68 = models.CharField(max_length=50, blank=True)
    total_income69 = models.CharField(max_length=50, blank=True)
    crop = models.CharField(max_length=50, blank=True)
    area_in_ac70 = models.CharField(max_length=50, blank=True)
    rainfed_irrigated71 = models.CharField(max_length=50, blank=True)
    yield_kg_ac = models.CharField(max_length=50, blank=True)
    average_price72 = models.CharField(max_length=50, blank=True)
    total_income73 = models.CharField(max_length=50, blank=True)
    crop74 = models.CharField(max_length=50, blank=True)
    area_in_ac75 = models.CharField(max_length=50, blank=True)
    rainfed_irrigated76 = models.CharField(max_length=50, blank=True)
    yield_kg_ac_77 = models.CharField(max_length=50, blank=True)
    average_price78 = models.CharField(max_length=50, blank=True)
    total_income79 = models.CharField(max_length=50, blank=True)
    source_1 = models.CharField(max_length=50, blank=True)
    source_2 = models.IntegerField(null=True, blank=True)
    source_3 = models.IntegerField(null=True, blank=True)
    column80 = models.CharField(max_length=50, blank=True)
    column81 = models.IntegerField(null=True, blank=True)
    column82 = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    column83 = models.CharField(max_length=50, blank=True)
    column84 = models.CharField(max_length=50, blank=True)
    column85 = models.CharField(max_length=50, blank=True)
    column86 = models.CharField(max_length=50, blank=True)
    column87 = models.CharField(max_length=50, blank=True)
    column88 = models.CharField(max_length=50, blank=True)
    column89 = models.CharField(max_length=50, blank=True)
    crops = models.CharField(max_length=50, blank=True)
    manure_per_ac = models.CharField(max_length=50, blank=True)
    investment = models.CharField(max_length=50, blank=True)
    following_methods = models.CharField(max_length=50, blank=True)
    crops90 = models.CharField(max_length=50, blank=True)
    manure_per_ac91 = models.CharField(max_length=50, blank=True)
    investment92 = models.CharField(max_length=50, blank=True)
    following_methods93 = models.CharField(max_length=50, blank=True)
    crops94 = models.CharField(max_length=50, blank=True)
    silt_per_ac = models.CharField(max_length=50, blank=True)
    investment95 = models.IntegerField(null=True, blank=True)
    following_methods96 = models.CharField(max_length=50, blank=True)
    crops97 = models.CharField(max_length=50, blank=True)
    fertlizers_per_ac = models.CharField(max_length=50, blank=True)
    investment98 = models.CharField(max_length=50, blank=True)
    following_methods99 = models.CharField(max_length=50, blank=True)
    crops100 = models.CharField(max_length=50, blank=True)
    manure_per_ac101 = models.CharField(max_length=50, blank=True)
    investment102 = models.CharField(max_length=50, blank=True)
    following_methods103 = models.CharField(max_length=50, blank=True)
    crops104 = models.CharField(max_length=50, blank=True)
    manure_per_ac105 = models.CharField(max_length=50, blank=True)
    investment106 = models.CharField(max_length=50, blank=True)
    following_methods107 = models.CharField(max_length=50, blank=True)
    crops108 = models.CharField(max_length=50, blank=True)
    per_ac = models.CharField(max_length=50, blank=True)
    investment109 = models.CharField(max_length=50, blank=True)
    following_methods110 = models.CharField(max_length=50, blank=True)
    crop_1111 = models.CharField(max_length=50, blank=True)
    irrigation_methods_followed = models.CharField(max_length=50, blank=True)
    crop_2112 = models.CharField(max_length=50, blank=True)
    irrigation_methods_followed113 = models.CharField(max_length=50, blank=True)
    crop_3114 = models.CharField(max_length=50, blank=True)
    irrigation_methods_followed115 = models.CharField(max_length=50, blank=True)
    crop_4116 = models.CharField(max_length=50, blank=True)
    irrigation_methods_followed117 = models.CharField(max_length=50, blank=True)
    crop_5118 = models.IntegerField(null=True, blank=True)
    irrigation_methods_followed119 = models.IntegerField(null=True, blank=True)
    is_there_farm_pond_in_the_field_yes_no = models.CharField(max_length=50, blank=True)
    if_exist_year_of_ewxcavation = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    was_the_farm_pond_dug_irrigation_ground_water_fisheries_others = models.CharField(max_length=50, blank=True)
    crop_rotation_yes_no = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    crop_method_mono_crop_poly_crop = models.CharField(max_length=50, blank=True)
    description120 = models.CharField(max_length=50, blank=True)
    seeds_grow_yourself = models.CharField(max_length=50, blank=True)
    purchase_of_seeds_from_vendors = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    seed_cost = models.IntegerField(null=True, blank=True)
    crop_1121 = models.CharField(max_length=50, blank=True)
    purchase_at_vendors_yes_no = models.CharField(max_length=50, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    crop_2122 = models.CharField(max_length=50, blank=True)
    purchase_at_vendors_yes_no_123 = models.CharField(max_length=50, blank=True)
    cost124 = models.IntegerField(null=True, blank=True)
    crop_3125 = models.CharField(max_length=50, blank=True)
    purchase_at_vendors_yes_no_126 = models.CharField(max_length=50, blank=True)
    cost127 = models.CharField(max_length=50, blank=True)
    crop_4128 = models.CharField(max_length=50, blank=True)
    purchase_at_vendors_yes_no_129 = models.CharField(max_length=50, blank=True)
    cost130 = models.CharField(max_length=50, blank=True)
    crop_5131 = models.CharField(max_length=50, blank=True)
    purchase_at_vendors_yes_no_132 = models.CharField(max_length=50, blank=True)
    cost133 = models.CharField(max_length=50, blank=True)
    crop_1134 = models.CharField(max_length=50, blank=True)
    following_yes_no = models.CharField(max_length=50, blank=True)
    details_of_methods_following = models.CharField(max_length=50, blank=True)
    crop_2135 = models.CharField(max_length=50, blank=True)
    following_yes_no_136 = models.CharField(max_length=50, blank=True)
    details_of_methods_following137 = models.CharField(max_length=50, blank=True)
    crop_3138 = models.CharField(max_length=50, blank=True)
    following_yes_no_139 = models.CharField(max_length=50, blank=True)
    details_of_methods_following140 = models.CharField(max_length=50, blank=True)
    column141 = models.CharField(max_length=50, blank=True)
    desi_cow = models.IntegerField(null=True, blank=True)
    hf_cow = models.IntegerField(null=True, blank=True)
    desi_buffalo = models.IntegerField(null=True, blank=True)
    murra_buffalo = models.IntegerField(null=True, blank=True)
    column142 = models.IntegerField(null=True, blank=True)
    column143 = models.IntegerField(null=True, blank=True)
    column144 = models.IntegerField(null=True, blank=True)
    column145 = models.IntegerField(null=True, blank=True)
    crop_1146 = models.CharField(max_length=50, blank=True)
    market = models.CharField(max_length=50, blank=True)
    crop_2147 = models.CharField(max_length=50, blank=True)
    market_148 = models.CharField(max_length=50, blank=True)
    crop_3149 = models.CharField(max_length=50, blank=True)
    market_150 = models.CharField(max_length=50, blank=True)
    crop_4151 = models.CharField(max_length=50, blank=True)
    market_152 = models.CharField(max_length=18, blank=True)
    crop_5153 = models.CharField(max_length=50, blank=True)
    market_154 = models.CharField(max_length=50, blank=True)

    
    def __str__(self):
        return f"{self.village}"


    