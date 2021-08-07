import phonenumbers
from phonenumbers import geocoder, timezone

phone = input('Digite o telefone no formato +551140028922: ')

phone_number = phonenumbers.parse(phone)
lugar = timezone.time_zones_for_number(phone_number)

print(geocoder.description_for_valid_number(phone_number, lugar, 'pt'))
