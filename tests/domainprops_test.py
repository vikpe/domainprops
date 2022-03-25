from domainprops import domainprops


def test_sld():
    assert "foo" == domainprops.sld("foo.com")
    assert "foo.bar" == domainprops.sld("foo.bar.com")


def test_bld():
    assert "foo" == domainprops.bld("foo.com")
    assert "foo" == domainprops.bld("foo.bar.com")


def test_tld():
    assert "com" == domainprops.tld("foo.com")
    assert "com" == domainprops.tld("foo.bar.com")


def test_idn():
    assert "foo.com" == domainprops.idn("foo.com")
    assert "xn--f-vioa.com" == domainprops.idn("f⊕⊕.com")
    assert "xn--espaol-zwa.es" == domainprops.idn("español.es")
    assert "xn--ei-2va.com" == domainprops.idn("eži.com")


def test_domains():
    assert ["foo", "com"] == domainprops.domains("foo.com")
    assert ["foo", "bar", "com"] == domainprops.domains("foo.bar.com")


def test_pattern():
    assert "lll" == domainprops.pattern("foo.com")
    assert "nnn" == domainprops.pattern("123.com")
    assert "lllnnn" == domainprops.pattern("foo123.com")
    assert "lll.lll" == domainprops.pattern("foo.bar.com")
    assert "lll-lll" == domainprops.pattern("foo-bar.com")


def test_length():
    assert 3 == domainprops.length("foo.com")
    assert 3 == domainprops.length("f⊕⊕.com")
    assert 7 == domainprops.length("foo.bar.com")


def test_has_alpha():
    assert domainprops.has_alpha("foo123.com")
    assert domainprops.has_alpha("foo-123.com")
    assert domainprops.has_alpha("foo.com")
    assert domainprops.has_alpha("foo-bar.com")
    assert domainprops.has_alpha("foo.bar.com")
    assert domainprops.has_alpha("f⊕⊕.com")
    assert not domainprops.has_alpha("123.com")


def test_has_numbers():
    assert domainprops.has_numbers("foo123.com")
    assert domainprops.has_numbers("foo-123.com")
    assert not domainprops.has_numbers("foo.com")
    assert not domainprops.has_numbers("foo-bar.com")
    assert not domainprops.has_numbers("foo.bar.com")
    assert not domainprops.has_numbers("f⊕⊕.com")
    assert domainprops.has_numbers("123.com")


def test_has_hyphens():
    assert not domainprops.has_hyphens("foo.com")
    assert domainprops.has_hyphens("foo-bar.com")


def test_is_alpha():
    assert not domainprops.is_alpha("foo123.com")
    assert not domainprops.is_alpha("foo-123.com")
    assert domainprops.is_alpha("foo.com")
    assert not domainprops.is_alpha("foo-bar.com")
    assert not domainprops.is_alpha("foo.bar.com")
    assert not domainprops.is_alpha("f⊕⊕.com")
    assert not domainprops.is_alpha("123.com")


def test_is_numeric():
    assert not domainprops.is_numeric("foo123.com")
    assert not domainprops.is_numeric("foo-123.com")
    assert not domainprops.is_numeric("foo.com")
    assert not domainprops.is_numeric("foo-bar.com")
    assert not domainprops.is_numeric("foo.bar.com")
    assert not domainprops.is_numeric("f⊕⊕.com")
    assert domainprops.is_numeric("123.com")


def test_is_alphanum():
    assert domainprops.is_alphanumeric("foo123.com")
    assert not domainprops.is_alphanumeric("foo-123.com")
    assert domainprops.is_alphanumeric("foo.com")
    assert not domainprops.is_alphanumeric("foo-bar.com")
    assert not domainprops.is_alphanumeric("foo.bar.com")
    assert not domainprops.is_alphanumeric("f⊕⊕.com")
    assert domainprops.is_alphanumeric("123.com")


def test_is_subdomain():
    assert not domainprops.is_subdomain("foo.com")
    assert not domainprops.is_subdomain("f⊕⊕.com")
    assert not domainprops.is_subdomain("foo-bar.com")
    assert domainprops.is_subdomain("foo.bar.com")


def test_is_idn():
    assert not domainprops.is_idn("foo.com")
    assert domainprops.is_idn("f⊕⊕.com")
