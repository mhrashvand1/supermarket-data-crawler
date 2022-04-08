def digikala_category_adapter(category_id):
    if category_id in [8896, 10612]:
        return {
            'cat_id':'canned-food',
            'title': 'کنسرو و غذا های آماده'
        }
    if category_id == 8907:
        return {
            'cat_id':'drinks',
            'title': 'نوشیدنی'       
        }
    if category_id == 8915:
        return {
            'cat_id':'breakfast',
            'title': 'صبحانه',    
        }
    if category_id == 9218:
        return {
            'cat_id':'proteins',
            'title': 'مواد پروتینی',    
        }
    if category_id == 9208:
        return {
            'cat_id':'dairy',
            'title': 'لبنیات',    
        }
    if category_id == 8899:
        return {
            'cat_id':'grocery',
            'title': 'خوار و بار',    
        }
    if category_id == 9229:
        return {
            'cat_id':'fruit-and-vegtable',
            'title': 'صبحانه',    
        }
    if category_id == 8898:
        return {
            'cat_id':'snacks',
            'title': 'تنقلات',    
        }
    if category_id == 8897:
        return {
            'cat_id':'nuts',
            'title': 'خشک بار',    
        }
    if category_id == 10285:
        return {
            'cat_id':'detergent',
            'title': 'مواد شوینده و دستمال',    
        }
    if category_id == 10284:
        return {
            'cat_id':'health-and-beauty',
            'title': 'آرایشی و بهداشتی',    
        }
    if category_id == 10571:
        return {
            'cat_id':'condiments',
            'title': 'افزودنی ها',    
        }
    if category_id == 10286:
        return {
            'cat_id':'kids',
            'title': 'مادر و کودک',    
        }        
    if category_id == 10150:
        return {
            'cat_id':'Fresh-Pastry',
            'title': 'قنادی',    
        }
    if category_id == 10125:
        return {
            'cat_id':'Finger-Food',
            'title': 'فینگر فود و پذیرایی',    
        }     
    if category_id == 10119:
        return {
            'cat_id':'Dietary-and-medicinal-supplements',
            'title': 'مکمل غذایی و دارویی',    
        }
    return {
        'cat_id':'unknown',
        'title': 'unknown',         
    }