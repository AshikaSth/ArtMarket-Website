
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new user instance, making sure to preserve our custom fields.
        """
        user = super(CustomAccountAdapter, self).save_user(request, user, form, commit=False)
        user.is_artist = form.cleaned_data.get('is_artist', False)
        user.is_gallery = form.cleaned_data.get('is_gallery', False)

        if commit:
            user.save()
        return user