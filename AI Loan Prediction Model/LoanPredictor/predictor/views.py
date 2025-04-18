from django.shortcuts import render
import joblib
import pandas as pd
from .forms import LoanForm

model = joblib.load('loan_model.pkl')  # path relative to manage.py

def predict_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        print(form)
        if form.is_valid():
            data = pd.DataFrame([form.cleaned_data])
            data = pd.get_dummies(data)
            # Ensure all expected columns exist
            expected_columns = model.get_booster().feature_names
            for col in expected_columns:
                if col not in data:
                    data[col] = 0
            data = data[expected_columns]
            prediction = model.predict(data)[0]
            result = 'Approved' if prediction == 1 else 'Rejected'
            return render(request, 'predictor/result.html', {'result': result})
    else:
        form = LoanForm()
    return render(request, 'predictor/form.html', {'form': form})