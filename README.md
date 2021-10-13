# Preprocessing Text Python Package

This python package is prepared by Joshua N.

Install

`pip install git+ssh://git@github.com/Joshuaakaspace/joshnator.git`

Uninstall

`pip uninstall joshnator`


For shortcut functions to clean your data, kindly use the below code:
`` def get_clean(x):
    x = str(x).lower()
    x =  js.cont_exp(x)
    x = js.remove_emails(x)
    x = js.remove_html_tags(x)
    x = js.remove_urls(x)
    x =  js.remove_special_chars(x)
    x = js.remove_accented_chars(x)
    x = js.remove_stopwords(x)
    return x ``
