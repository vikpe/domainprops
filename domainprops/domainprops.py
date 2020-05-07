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


def pattern(domain: str) -> str:
    result = ""

    for char in sld(domain):
        if char.isalpha():
            result += "l"
        elif char.isdigit():
            result += "n"
        else:
            result += char

    return result


def has_alpha(domain: str) -> bool:
    return bool(re.search(r"[a-z]", sld(domain), re.IGNORECASE))


def has_numbers(domain: str) -> bool:
    return bool(re.search(r"\d", sld(domain)))


def has_alphanum(domain: str) -> bool:
    return has_alpha(domain) and has_numbers(domain)


def has_hyphens(domain: str) -> bool:
    return "-" in sld(domain)


def is_alpha(domain: str) -> bool:
    return sld(domain).isalpha()


def is_numeric(domain: str) -> bool:
    return sld(domain).isdigit()


def is_alphanumeric(domain: str) -> bool:
    return has_alphanum(domain) and not has_hyphens(domain) and not is_subdomain(domain)


def is_subdomain(domain: str) -> bool:
    return domain.count(".") > 1


def is_idn(domain: str) -> bool:
    return idn(domain) != domain
