# Domainprops
> Python package for parsing domain name properties

[![test](https://github.com/vikpe/domainprops/workflows/test/badge.svg?branch=master)](https://github.com/vikpe/domainprops/actions) [![codecov](https://codecov.io/gh/vikpe/domainprops/branch/master/graph/badge.svg)](https://codecov.io/gh/vikpe/domainprops) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Install
```shell script
python -m pip install domainprops
```

## Usage
```python
from domainprops import domainprops

domainprops.tld("foo.com")          # "com"
domainprops.sld("foo.com")          # "foo"
domainprops.is_alpha("foo.com")     # True
domainprops.is_numeric("foo.com")   # False
```


## API
Function | Returns | Description | Example | Result
--- | --- | --- | --- | ---
`tld` | `string` | Top level domain | `tld("foo.com")` | `"com"`
`sld` | `string` | Sub level domain | `sld("foo.bar.com")` | `"foo.bar"`
`bld` | `string` | Bottom level domain | `bld("foo.bar.com")` | `"foo"`
`length` | `int` | Lenght of domain | `length("foo.com")` | `3`
`idn` | `string` | IDN version of domain | `idn("f⊕⊕.com")` | `"xn--f-vioa.com"`
`pattern` | `string` | Char pattern | `pattern("foo-123.com")` | `"lll-nnn"`
`domains` | `list` | Domain parts of domain | `domains("foo.bar.com")` | `["foo", "bar", "com"]`
`has_alpha` | `bool` | Has alpha characters | `has_alpha("foo.com")` | `True`
`has_numbers` | `bool` | Has numbers | `has_numbers("foo.com")` | `False`
`has_hyphens` | `bool` | Has hyphens | `has_hyphens("foo.com")` | `False`
`is_alpha` | `bool` | Is strictly alpha characters | `is_alpha("foo.com")` | `True`
`is_numeric` | `bool` | Is strictly numbers | `is_numeric("foo.com")` | `False`
`is_alphanumeric` | `bool` | Is strictly alpha characters and/or numbers | `is_alphanumeric("foo.com")` | `True`
`is_subdomain` | `bool` | Is sub domain | `is_subdomain("foo.com")` | `False`
