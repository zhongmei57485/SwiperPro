from django import forms


from user.models import Profile



class ProfileForm(forms.ModelForm):

    def _clean_max_distance(self):
        max_distance = self._clean_data.get('max_distance')
        min_distance = self._clean_data.get('min_distance')

        if max_distance < min_distance:
            raise forms.ValidationError('最大匹配距离必须大于最小匹配距离')

        return max_distance

    def _clean_max_dating_age(self):
        max_dating_age = self._clean_data.get('max_dating_age')
        min_dating_age = self._clean_data.get('min_dating_age')

        if max_dating_age < min_dating_age:
            raise forms.ValidationError('最大匹配年龄必须大于最小匹配年龄')

        return max_dating_age

    class meta:
        model = Profile

        fields = [

            'location',
            'min_distance',
            'max_distance',
            'min_dating_age',
            'max_dating_age',
            'dating_sex'

        ]

        #fields = __all__