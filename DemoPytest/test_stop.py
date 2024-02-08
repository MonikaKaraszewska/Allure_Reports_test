import pytest

# @pytest.mark.skip(reason="skip teh whole class")
#@pytest.mark.xfail(reason="XFAIL the whole class")

''' zeby zatrzymac testy popwierszym fail w terminalu piszemy:
            pytest test_stop.py --maxfail=1 '''


class Test_Math:
    #pass
    def test_number_square(self):
        num = 10
        result = num * num
        assert result == num ** 2

    #Fail
    def test_divide_num(self):

        num = 10
        result = num + num
        assert result == num / num


    #fail
    def test_square_num(self):
        num = 10
        result = num + num
        assert result == num ** 2

        # pass
    def test_cube_num(self):
        num = 10
        result = num * num * num
        assert result == num ** 3
