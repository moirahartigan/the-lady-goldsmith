

# Code Validators and Website Analysis
The website's pages was tested against the following validators:

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
bag/templates/bag/bag.html  | 0 errors and 0 contrast errors| [Results](readme/html_validation/bag-page.png) 
bag/templates/bag/bag.html (Empty)  | 0 errors and 0 contrast errors| [Results](readme/html_validation/bag-page-empty.png) 
checkout/templates/checkout/checkout.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/checkout-page.png)  
checkout/templates/checkout/checkout_success.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/checkout-success.png)    
contact/templates/contact/contact.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/contact-page.png)    
home/templates/home/index.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/home-page.png)
products/templates/products/add_product.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/add-products-page.png)
products/templates/products/edit_product.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/edit-products-page.png)  
products/templates/products/product_detail.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/edit-products-detail-page.png) 
products/templates/products/products.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/products-page.png)   
products/templates/products/sale_items.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/sale-page.png)     
profile/templates/profile/profile.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/profile-page.png)    
templates/allauth/account/login.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/login-page.png)
templates/allauth/account/logout.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/logout-page.png)
templates/allauth/account/register.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/register-page.png)
wishlist/templates/wishlist/wishlist.html | 0 errors and 0 contrast errors| [Results](readme/html_validation/wishlist-page.png) 
<br>
## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/css/base.css | Passed, No errors found | [Results](readme/css_validation/css-validation.png) 
checkout/static/checkout/css/checkout.css | Passed, No errors found | [Results](readme/css_validation/css-validation-checkout.png)  


<br>

## Chrome Dev tools Lighthouse 

- I used Lighthouse (https://developers.google.com/web/tools/lighthouse) to test the performance, seo, best practices and accessibility of the site
- Overall the results are very good for the 4 values: Performance, Accessibility, Best Practices and SEO

### Desktop
Page  | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%)
------------  | ------------ | ------------- | ------------- | -------------
bag/templates/bag/bag.html | 96 | 93 | 90 | 89 |
checkout/templates/checkout/checkout.html | 82 | 100 | 80 | 100 |
checkout/templates/checkout/checkout_success.html | 95 | 100 | 87 | 100 ||
contact/templates/contact/contact.html | 95 | 100 | 87 | 100 |
home/templates/home/index.html | 90 | 94 | 87 | 90 ||
products/templates/products/add_product.html | 94 | 92 | 87 | 100 |
products/templates/products/edit_product.html | 97 | 92 | 87 | 100 |
products/templates/products/product_detail.html | 96 | 100 | 80 | 100 |
products/templates/products/products.html  | 96 | 100 | 87 | 100 |
products/templates/products/sale_items.html | 96 | 100 | 87 | 100 |
profile/templates/profile/profile.html | 97 | 100 | 87 | 100 |
templates/allauth/account/login.html | 94 | 100 |87 | 100 |
templates/allauth/account/logout.html | 93 | 100 | 87 | 100 |
templates/allauth/account/register.html | 98| 100 | 87 | 100 |
wishlist/templates/wishlist/wishlist.html | 97 | 100 | 87 | 90 |

### Mobile
Page  | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%)
------------  | ------------ | ------------- | ------------- | -------------
bag/templates/bag/bag.html | 96 | 96 | 80 | 100 |
checkout/templates/checkout/checkout.html | 82 | 100 | 80 | 100 |
checkout/templates/checkout/checkout_success.html | 95 | 100 | 87 | 100 ||
contact/templates/contact/contact.html | 95 | 100 | 87 | 100 |
home/templates/home/index.html | 91 | 100 | 87 | 100 ||
products/templates/products/add_product.html | 94 | 92 | 87 | 100 |
products/templates/products/edit_product.html | 97 | 92 | 87 | 100 |
products/templates/products/product_detail.html | 96 | 100 | 80 | 100 |
products/templates/products/products.html  | 96 | 100 | 87 | 100 |
products/templates/products/sale_items.html | 96 | 100 | 87 | 100 |
profile/templates/profile/profile.html | 97 | 100 | 87 | 100 |
templates/allauth/account/login.html | 94 | 100 |87 | 100 |
templates/allauth/account/logout.html | 93 | 100 | 87 | 100 |
templates/allauth/account/register.html | 98| 100 | 87 | 100 |
wishlist/templates/wishlist/wishlist.html | 97 | 100 | 87 | 90 ||

<br>

## JSHint
I checked the all the JavaScript files using [JSHint](https://jshint.com/)

There were a few missing semicolons and ES6 version issues but they were easy fixes. 

<br>

## PEP8online
I checked the Py files using [PEP8 online](http://pep8online.com/)

The code passed all checks.

Page | Result 
------------ | ------------- 
bag/admin.py | No errors/warnings 
bag/apps.py | No errors/warnings 
bag/contexts.py | No errors/warnings 
bag/models.py | No errors/warnings 
bag/urls.py | No errors/warnings 
bag/views.py | No errors/warnings 
checkout/admin.py | No errors/warnings 
checkout/apps.py | No errors/warnings 
checkout/forms.py | No errors/warnings 
checkout/models.py | No errors/warnings 
checkout/signals.py | No errors/warnings 
checkout/urls.py | No errors/warnings 
checkout/views.py | No errors/warnings 
contact/apps.py | No errors/warnings 
contact/forms.py | No errors/warnings 
contact/models.py | No errors/warnings 
contact/urls.py | No errors/warnings 
contact/views.py | No errors/warnings 
contact/webhook_handler.py | No errors/warnings 
contact/webhooks.py | No errors/warnings  
home/admin.py | No errors/warnings 
home/apps.py | No errors/warnings 
home/models.py | No errors/warnings  
home/urls.py | No errors/warnings 
home/views.py | No errors/warnings 
products/admin.py | No errors/warnings 
products/apps.py | No errors/warnings 
products/forms.py | No errors/warnings 
products/models.py | No errors/warnings 
products/urls.py | No errors/warnings 
products/views.py | line 55 is 1 character too long, |
..................| I was unable to split this line without breaking my code so I left it as it was.
products/widgets.py | No errors/warnings 
profiles/admin.py | No errors/warnings 
profiles/apps.py | No errors/warnings 
profiles/forms.py | No errors/warnings 
profiles/models.py | No errors/warnings 
profiles/urls.py | No errors/warnings 
profiles/views.py | No errors/warnings
wishlist/admin.py | No errors/warnings 
wishlist/apps.py | No errors/warnings 
wishlist/contexts.py | No errors/warnings 
wishlist/models.py | No errors/warnings 
wishlist/urls.py | No errors/warnings 
wishlist/views.py | No errors/warnings 
custom_storages.py | No errors/warnings
manage.py | No errors/warnings
