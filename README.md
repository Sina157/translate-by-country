# translate-by-country

With this library, you can translate the text without choosing the language and with the characteristics of the countries
<hr>

# installation:

```
pip install translate-by-country
```
<hr>

# Usage:
<br>

Translates text based on country alpha2
```python
from translate_by_country import translate_text_by_alpha2

print(translate_text_by_alpha2("translate by country","ax")) # Översätt efter land
```
<br>
Translates text based on country alpha3

```python
from translate_by_country import translate_text_by_alpha3

print(translate_text_by_alpha3("translate by country","aut")) # nach Land übersetzt
```

<br>
Translates text based on country code

```python
from translate_by_country import translate_text_by_code

print(translate_text_by_code("translate by country",98)) # ترجمه توسط کشور
```
<br>
Translates text based on country name

```python
from translate_by_country import translate_text_by_name

print(translate_text_by_name("translate by country","albania")) # Përkthejeni sipas vendit
```
<br>
Translates text based on country emoji

```python
from translate_by_country import translate_text_by_emoji

print(translate_text_by_emoji("translate by country","🇹🇼")) # 按国家翻译
```

It can be a good complement to the <a href="https://pypi.org/project/pycountry">pycountry</a> library.
<br>
If there was any problem, please <a href="https://github.com/Sina157/translate-by-country/issues">open an issue</a> for them on github.


