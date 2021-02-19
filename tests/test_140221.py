import pytest
from source.hw_130221.app import main
import re


class TestHomework130221:
    def test_content(self):
        r = re.compile(r'^CTF{.*}$')
        assert main() == list(filter(r.match, main()))

    def test_length(self):
        assert len(main()) == 2


