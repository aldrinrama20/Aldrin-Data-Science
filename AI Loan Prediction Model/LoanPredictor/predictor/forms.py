from django import forms

class LoanForm(forms.Form):
    GENDER_CHOICES = [('0', 'Male'), ('1', 'Female')]
    DEPENDENTS_CHOICES = [('0', 'No'), ('1', 'Yes')]
    MARRIED_CHOICES = [('1', 'Yes'), ('0', 'No')]
    EDUCATION_CHOICES = [('0', 'Graduate'), ('1', 'Not Graduate')]
    SELF_EMPLOYED_CHOICES = [('0', 'No'), ('1', 'Yes')]
    PROPERTY_AREA_CHOICES = [('2', 'Urban'), ('1', 'Semiurban'), ('0', 'Rural')]


    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    Dependents = forms.ChoiceField(choices=DEPENDENTS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    Married = forms.ChoiceField(choices=MARRIED_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    Education = forms.ChoiceField(choices=EDUCATION_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    ApplicantIncome = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    CoapplicantIncome = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    LoanAmount = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Loan_Amount_Term = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Credit_History = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Self_Employed = forms.ChoiceField(choices=SELF_EMPLOYED_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    Property_Area = forms.ChoiceField(choices=PROPERTY_AREA_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))