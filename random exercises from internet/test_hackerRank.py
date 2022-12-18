import pytest
from SDA_studies.Autoestudio import solved_hackerRank as SHR
@pytest.mark.parametrize('year','result'[(1980,True), (1984, True), (1988, True)])
def test_leap_year(year, result):
    assert SHR.leap_year(year) is result