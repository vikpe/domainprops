import re


def tld(domain: str) -> str:
    return domain.rsplit(".", maxsplit=1)[1]


def sld(domain: str) -> str:
    return domain.rsplit(".", maxsplit=1)[0]


def bld(domain: str) -> str:
    return domain.split(".", maxsplit=1)[0]


def length(domain: str) -> int:
    return len(sld(domain))


def idn(domain: str) -> str:
    return domain.encode("idna").decode("utf8")


def domains(domain: str) -> list:
    return domain.split(".")


def has_alpha(domain: str) -> bool:
    base = sld(domain)
    return bool(re.search(r"[a-z]", base, re.IGNORECASE))


def has_numbers(domain: str) -> bool:
    base = sld(domain)
    return bool(re.search(r"\d", base))


def has_alphanum(domain: str) -> bool:
    return has_alpha(domain) and has_numbers(domain)


def has_hyphens(domain: str) -> bool:
    return "-" in sld(domain)


def is_alpha(domain: str) -> bool:
    return not (has_numbers(domain) or has_hyphens(domain))


def is_numeric(domain: str) -> bool:
    return not (has_alpha(domain) or has_hyphens(domain))


def is_alphanumeric(domain: str) -> bool:
    return has_alphanum(domain) and not has_hyphens(domain)


def is_subdomain(domain: str) -> bool:
    return domain.count(".") > 1


def is_idn(domain: str) -> bool:
    return idn(domain) != domain
