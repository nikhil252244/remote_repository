from django import forms
class InsertingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Product ID',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your product id',
                'class':'form-control'
            }
        )
    )
    product_name=forms.CharField(
        label= 'Enter Your Product Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'your product name',
                'class':'form-control'
            }
        )
    )
    product_cost=forms.IntegerField(
        label='Enter Your Product Cost ',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your product cost',
                'class':'form-control'
            }
        )
    )
    product_class=forms.CharField(
        label='Enter Your Product Class',
        widget=forms.TextInput(
            attrs={
                'placeholder':'your product class',
                'class':'form-control'
            }
        )
    )
    no_of_products=forms.IntegerField(
        label='Enter Your no_of_products',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your totoal no of product',
                'class':'form-control'
            }
        )
    )
    y=range(2000,2020)
    manufacture_date=forms.DateField(
        widget=forms.SelectDateWidget(years=y),
        label='Select Product Manfacturing Date'
    )

    expiry_date=forms.DateField(
        widget=forms.SelectDateWidget(),
        label='select Product Expiry Date'
    )


    customer_name=forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'customer name',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'mobile number',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'your email id',
                'class':'form-control'
            }
        )
    )

class UpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Product ID',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'your product id',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter Your Product Cost ',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'your product cost',
                'class': 'form-control'
            }
        )
    )

class DeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Product ID',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'your product id',
                'class': 'form-control'
            }
        )
    )




