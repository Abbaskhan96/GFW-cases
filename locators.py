# These are the locators file that stored all locators that used in test



#the checkout data-------


checkout_fields_path={
            "Email":"//input[@id='checkout_email']",
            "FirstName":"//input[@id='checkout_shipping_address_first_name']",
            "LastName":"//input[@id='checkout_shipping_address_last_name']",
            "Address":"//input[@id='checkout_shipping_address_address1']",
            "City":"//input[@id='checkout_shipping_address_city']",
            "State":"//select[@id='checkout_shipping_address_province']",
            "Zip":"//input[@id='checkout_shipping_address_zip']",
            "Phone":"//input[@id='checkout_shipping_address_phone']"
            }

checkout_field_values={
            "Email":"abbas.khan@codup.co",
            "FirstName":"Abbas",
            "LastName":"Khan",
            "Address":"Florida, USA",
            "City":"FL",
            "State":"Florida",
            "Zip":"33322",
            "Phone":"+923353770290"  
            }


#PDP Plant product CSS selector
products_plants={1:"div[data-alpha='Orange Butterfly Milkweed Plant Sets (I)'] div[class='product-info'] a",
          2:"div[data-alpha='Wetland Wonders'] div[class='product-info'] a"}

product_zip="#cartform-custom"
add_to_cart_button="#validate-prod-zip-sticky"
cart_close_btn="//button[@aria-label='Close cart']//div[@class='icn-close']"
zip_value=["15001","33322"]

zip_btn_plp="li[id='zip-filter-btn'] span[class='slideout__trigger-collection-sidebar']"

product_merch={
    1:"div[data-alpha='Garden For Wildlife E-Gift Card'] div[class='product-info'] a",
    2:"div[data-alpha='Garden for Wildlife Pollinator Garden Crewneck Sweatshirt'] div[class='product-info'] a"
    }

#Cart page
checkout_btn="//section[@id='shopping-cart']//div[contains(@class,'ajax-cart__form-wrapper cart-wrapper js-ajax-cart-content')]//input[@id='checkout']"

#cart value

cart_price="//main[contains(@role,'main')]//div[contains(@class,'js-cart-summary')]//div[3]//p[2]//span[1]"

#checkout_submit
checkout_btn_1="//button[@id='continue_button']"

#remove product
remove_product="//a[@id='checkout-remove-products']"

#continue_checkout
continue_checkout="//a[normalize-space()='Continue shopping']"