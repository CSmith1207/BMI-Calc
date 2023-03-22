from main import BMICalc
from main import BMICategory

#Make sure that BMI is being calculated correctly, using the example from the website
def test_BMI_calculation():
    assert BMICalc(5, 3, 125) == 22.7

#testing underweight boundary
def test_under_interior():
    assert BMICategory(5) == "You are underweight"

def test_under_off():
    assert BMICategory(18.4) == "You are underweight"

def test_under_on():
    assert BMICategory(18.5) != "You are underweight"


#testing normal weight boundaries
def test_normal_off_lower():
    assert BMICategory(18.4) != "You are normal weight"

def test_normal_on_lower():
    assert BMICategory(18.5) == "You are normal weight"

def test_normal_interior():
    assert BMICategory(22) == "You are normal weight"

def test_normal_off_upper():
    assert BMICategory(24.9) == "You are normal weight"

def test_normal_on_upper():
    assert BMICategory(25) != "You are normal weight"


#testing overweight boundaries
def test_over_off_lower():
    assert BMICategory(24.9) != "You are overweight"

def test_over_on_lower():
    assert BMICategory(25) == "You are overweight"

def test_over_interior():
    assert BMICategory(27) == "You are overweight"

def test_over_off_upper():
    assert BMICategory(29.9) == "You are overweight"

def test_over_on_upper():
    assert BMICategory(30) != "You are overweight"


#testing obese boundary
def test_obese_off():
    assert BMICategory(29.9) != "You are obese"

def test_obese_on():
    assert BMICategory(30) == "You are obese"

def test_obese_interior():
    assert BMICategory(40) == "You are obese"
