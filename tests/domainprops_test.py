import unittest

from domainprops import domainprops


class DomainTest(unittest.TestCase):
    def test_sld(self):
        self.assertEqual("foo", domainprops.sld("foo.com"))
        self.assertEqual("foo.bar", domainprops.sld("foo.bar.com"))

    def test_bld(self):
        self.assertEqual("foo", domainprops.bld("foo.com"))
        self.assertEqual("foo", domainprops.bld("foo.bar.com"))

    def test_tld(self):
        self.assertEqual("com", domainprops.tld("foo.com"))
        self.assertEqual("com", domainprops.tld("foo.bar.com"))

    def test_idn(self):
        self.assertEqual("foo.com", domainprops.idn("foo.com"))
        self.assertEqual("xn--f-vioa.com", domainprops.idn("f⊕⊕.com"))

    def test_domains(self):
        self.assertEqual(["foo", "com"], domainprops.domains("foo.com"))
        self.assertEqual(["foo", "bar", "com"], domainprops.domains("foo.bar.com"))

    def test_length(self):
        self.assertEqual(3, domainprops.length("foo.com"))
        self.assertEqual(3, domainprops.length("f⊕⊕.com"))
        self.assertEqual(7, domainprops.length("foo.bar.com"))

    def test_has_alpha(self):
        self.assertTrue(domainprops.has_alpha("foo123.com"))
        self.assertTrue(domainprops.has_alpha("foo-123.com"))
        self.assertTrue(domainprops.has_alpha("foo.com"))
        self.assertTrue(domainprops.has_alpha("foo-bar.com"))
        self.assertTrue(domainprops.has_alpha("f⊕⊕.com"))
        self.assertFalse(domainprops.has_alpha("123.com"))

    def test_has_numbers(self):
        self.assertTrue(domainprops.has_numbers("foo123.com"))
        self.assertTrue(domainprops.has_numbers("foo-123.com"))
        self.assertFalse(domainprops.has_numbers("foo.com"))
        self.assertFalse(domainprops.has_numbers("foo-bar.com"))
        self.assertFalse(domainprops.has_numbers("f⊕⊕.com"))
        self.assertTrue(domainprops.has_numbers("123.com"))

    def test_has_alphanum(self):
        self.assertTrue(domainprops.has_alphanum("foo123.com"))
        self.assertTrue(domainprops.has_alphanum("foo-123.com"))
        self.assertFalse(domainprops.has_alphanum("foo.com"))
        self.assertFalse(domainprops.has_alphanum("foo-bar.com"))
        self.assertFalse(domainprops.has_alphanum("f⊕⊕.com"))
        self.assertFalse(domainprops.has_alphanum("123.com"))

    def test_has_hyphens(self):
        self.assertFalse(domainprops.has_hyphens("foo.com"))
        self.assertTrue(domainprops.has_hyphens("foo-bar.com"))

    def test_is_alpha(self):
        self.assertFalse(domainprops.is_alpha("foo123.com"))
        self.assertFalse(domainprops.is_alpha("foo-123.com"))
        self.assertTrue(domainprops.is_alpha("foo.com"))
        self.assertFalse(domainprops.is_alpha("foo-bar.com"))
        self.assertTrue(domainprops.is_alpha("f⊕⊕.com"))
        self.assertFalse(domainprops.is_alpha("123.com"))

    def test_is_numeric(self):
        self.assertFalse(domainprops.is_numeric("foo123.com"))
        self.assertFalse(domainprops.is_numeric("foo-123.com"))
        self.assertFalse(domainprops.is_numeric("foo.com"))
        self.assertFalse(domainprops.is_numeric("foo-bar.com"))
        self.assertFalse(domainprops.is_numeric("f⊕⊕.com"))
        self.assertTrue(domainprops.is_numeric("123.com"))

    def test_is_alphanum(self):
        self.assertTrue(domainprops.is_alphanumeric("foo123.com"))
        self.assertFalse(domainprops.is_alphanumeric("foo-123.com"))
        self.assertFalse(domainprops.is_alphanumeric("foo.com"))
        self.assertFalse(domainprops.is_alphanumeric("foo-bar.com"))
        self.assertFalse(domainprops.is_alphanumeric("f⊕⊕.com"))
        self.assertFalse(domainprops.is_alphanumeric("123.com"))

    def test_is_subdomain(self):
        self.assertFalse(domainprops.is_subdomain("foo.com"))
        self.assertFalse(domainprops.is_subdomain("f⊕⊕.com"))
        self.assertFalse(domainprops.is_subdomain("foo-bar.com"))
        self.assertTrue(domainprops.is_subdomain("foo.bar.com"))

    def test_is_idn(self):
        self.assertFalse(domainprops.is_idn("foo.com"))
        self.assertTrue(domainprops.is_idn("f⊕⊕.com"))


if __name__ == "main":
    unittest.main()
