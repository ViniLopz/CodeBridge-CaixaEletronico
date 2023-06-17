from django import forms

class DepositarForm(forms.Form):
    cliente = forms.IntegerField(label="ID do Cliente", required=True)
    valor = forms.DecimalField(label="Valor", required=True)

class DebitarForm(DepositarForm):
    pass