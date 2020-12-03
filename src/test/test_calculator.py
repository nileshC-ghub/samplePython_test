
#Performing actions to make sure other packages can be imported
import sys
sys.path.append("..")

from calculator import Calculator

def test_add():
    calcu = Calculator()

    result = calcu.add(3,12)

    assert result == 15
