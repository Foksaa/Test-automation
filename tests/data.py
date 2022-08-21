import random
import string

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

def generate_string(n):
    return n*'x'

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

correct_email="irinka48@yandex.ru"
correct_pass="516035"
incorrect_email={'':'empty string',
                 ' ':'whitespace',
                 'irinka48@yandex.ru':'uncorrect email',
                 generate_string(255):'255 symbols',
                 russian_chars():'russian',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123':'digit'}
incorrect_pass={'':'empty string',
                 ' ':'whitespace',
                 'Qwerty':'uncorrect pass',
                 generate_string(255):'255 symbols',
                 russian_chars():'russian',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123':'digit'}
correct_product=['телевизор','кофеварка','чайник','тостер','пылесос']
incorrect_product_title={
'Телевизор':'first capital letter',
    'ТеЛеВиЗоР':'fence',
    'ТЕЛЕВИЗОР':'all lower case',
    ' телевизор':'space at the beginning',
    'теле визор':'space in the middle',
    'телевизор ':'space at the end',
    'тлевизор':'missing letter',
    'телефизор':'spelling mistake',
    'телевизор)))':'special characters at the end',
    ')))телевизор':'space at the beginning',
    'теле.визор':'space in the middle',
    'ntktdbpjh':'English layout',
    'televizor':'Latin alphabet'
}
other_value_for_search={
                 generate_random_string(10): 'non-existent product',
                 generate_string(255):'255 symbols',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123456789':'digit'
}