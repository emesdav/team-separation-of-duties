from internet_forensics.validation import Validate

print(Validate("dummy_user@dummy_domain.com").IfEmail())
print(Validate("1234").IfInt())
