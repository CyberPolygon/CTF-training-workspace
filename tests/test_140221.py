import pytest
from source.hw_140221.app import main
import re


class TestHomework140221:
    def test_content(self):
        r = re.compile(r'^CTF{.*}$')
        assert main() == list(filter(r.match, main()))

    def test_length(self):
        assert len(main()) == 2


