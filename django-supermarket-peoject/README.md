
## Usage

```bash
sudo docker-compose -f docker-compose.dev.yml up -d
manage.py runserver
```
endpoints:
```bash
/supermarket/products/  #lookup field: product_id
/supermarket/categories/  #lookup field: cat_id
/supermarket/brands/  #lookup field: pk
/supermarket/vendors/  #lookup field: name
/supermarket/mainimages/  
/supermarket/otherimages/
/accounts/  #lookup field: username
```
other endpoints:
```bash
/register/
/account-confirm-email/<str:key>/
/resend-email/
#After confirm will be redirect to login url
/login/
/logout/
/password/reset/
/password-reset-confirm/<uidb64>/<token>/
/password/change/ 
/user/

```

Note that permission_classes in the views are commented(for test). If you uncomment it, you have to provide authentication headers in the crawler pipleline.
