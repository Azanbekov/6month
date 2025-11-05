from rest_framework.exceptions import ValidationError
from datetime import datetime

def validate_user_age_from_token(request):
    birthdate = request.auth.get('birthdate') if request.auth else None

    if not birthdate:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")

    birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d").date()
    today = datetime.today().date()
    age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))

    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")
