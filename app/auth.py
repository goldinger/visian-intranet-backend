from django_auth_ldap.backend import LDAPBackend


class CustomLDAPBackend(LDAPBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(self, username, password)
        if user:
            user.set_password(password)
            # user.is_staff = True
            # user.is_superuser = True
            user.save()
            return user
