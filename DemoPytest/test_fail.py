''' xfail (expected failure):
xfail oznacza, że test został zaplanowany jako test, który jest spodziewany nie powieść się (zakończyć się błędem).
Testy oznaczone jako xfail są uruchamiane, ale oczekuje się od nich, że zakończą się niepowodzeniem.
Jeśli test xfail zakończy się powodzeniem (czyli nie pojawi się błąd, który był oczekiwany), to wynik testu
zostanie oznaczony jako "unexpected pass" (nieoczekiwane powodzenie), co oznacza, że sygnalizuje to potencjalny błąd
w teście. '''

'''skip:
skip oznacza, że test zostaje całkowicie pominięty podczas wykonywania.
Testy oznaczone jako skip nie są uruchamiane, pomijane są podczas wykonania testów.
Może to być użyte, na przykład, gdy dany test nie jest jeszcze gotowy do uruchomienia, lub 
gdy test wymaga specyficznych warunków, które obecnie nie są spełnione.'''


import pytest

class Test_Math:
    def test_divide_num(self):
        pytest.xfail("Need to investigate")
        num =10
        result = num + num
        assert result == num / num


    @pytest.mark.xfail(reason="Result ADD numbers &not m cocs ktam cos ")
    def test_square_num(self):
        num = 10
        result = num + num
        assert result == num ** 2

    @pytest.mark.xfail(reason="Result are correct")
    def test_cube_num(self):
        num =10
        result = num * num * num
        assert result == num **3

    @pytest.mark.xfail(run=False)
    def test_number_square(self):
        num = 10
        result = num * num
        assert result == num ** 2
