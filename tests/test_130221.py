import pytest
from source.hw_130221.app import main
import re


class TestHomework130221:
    def test_content(self):
        r = re.compile(r'^CTF{.*}$')
        assert main() == list(filter(r.match, main())), "Не все флаги подходят под формат флага"

    def test_length(self):
        assert len(main()) == 2, "Неправильное количество флагов"


