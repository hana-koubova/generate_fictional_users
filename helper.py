from random import random, randint
from faker import Faker

locales = [
'ar_AA',
'ar_AE',
'ar_BH',
'ar_JO',
'ar_PS',
'ar_SA',
'az_AZ',
'bg_BG',
'bn_BD',
'bs_BA',
'cs_CZ',
'da_DK',
'de',
'de_AT',
'de_CH',
'de_DE',
'dk_DK',
'el_CY',
'el_GR',
'en',
'en_AU',
'en_BD',
'en_CA',
'en_GB',
'en_IE',
'en_IN',
'en_NZ',
'en_PH',
'en_TH',
'en_US',
'es',
'es_AR',
'es_CA',
'es_CL',
'es_CO',
'es_ES',
'es_MX',
'et_EE',
'fa_IR',
'fi_FI',
'fil_PH',
'fr_BE',
'fr_CA',
'fr_CH',
'fr_FR',
'fr_QC',
'ga_IE',
'he_IL',
'hi_IN',
'hr_HR',
'hu_HU',
'hy_AM',
'id_ID',
'it_CH',
'it_IT',
'ja_JP',
'ka_GE',
'ko_KR',
'la',
'lb_LU',
'lt_LT',
'lv_LV',
'mt_MT',
'ne_NP',
'nl_BE',
'nl_NL',
'no_NO',
'or_IN',
'pl_PL',
'pt_BR',
'pt_PT',
'ro_RO',
'ru_RU',
'sk_SK',
'sl_SI',
'sq_AL',
'sv_SE',
'ta_IN',
'th',
'th_TH',
'tl_PH',
'tr_TR',
'tw_GH',
'uk_UA',
'vi_VN',
'zh_CN',
'zh_TW',
'zu_ZA']

locales_dict = {'ar_AA',
'ar_AE',
'ar_BH',
'ar_EG',
'ar_JO',
'ar_PS',
'ar_SA',
'az_AZ',
'bg_BG',
'bn_BD',
'bs_BA',
'cs_CZ',
'da_DK',
'de',
'de_AT',
'de_CH',
'de_DE',
'dk_DK',
'el_CY',
'el_GR',
'en',
'en_AU',
'en_BD',
'en_CA',
'en_GB',
'en_IE',
'en_IN',
'en_NZ',
'en_PH',
'en_TH',
'en_US',
'es',
'es_AR',
'es_CA',
'es_CL',
'es_CO',
'es_ES',
'es_MX',
'et_EE',
'fa_IR',
'fi_FI',
'fil_PH',
'fr_BE',
'fr_CA',
'fr_CH',
'fr_FR',
'fr_QC',
'ga_IE',
'he_IL',
'hi_IN',
'hr_HR',
'hu_HU',
'hy_AM',
'id_ID',
'it_CH',
'it_IT',
'ja_JP',
'ka_GE',
'ko_KR',
'la',
'lb_LU',
'lt_LT',
'lv_LV',
'mt_MT',
'ne_NP',
'nl_BE',
'nl_NL',
'no_NO',
'or_IN',
'pl_PL',
'pt_BR',
'pt_PT',
'ro_RO',
'ru_RU',
'sk_SK',
'sl_SI',
'sq_AL',
'sv_SE',
'ta_IN',
'th',
'th_TH',
'tl_PH',
'tr_TR',
'tw_GH',
'uk_UA',
'vi_VN',
'zh_CN',
'zh_TW',
'zu_ZA'}

print(len(locales))


def random_locale(arr):
    len_arr = len(arr)
    index = randint(0, len_arr-1)
    print(index)
    print(locales[index])
    return locales[index]

def print_all(arr):
    for a in arr:
        fake = Faker(a)
        try:
            print(fake.name)
        except:
            print(f'Name not available for {a}')

        try:
            print(fake.address)
        except:
            print(f'Address not available for {a}')

        try:
            print(fake.phone_number)
        except:
            print(f'Phone number not available for {a}')

        try:
            print(fake.job)
        except:
            print(f'Job not available for {a}')



