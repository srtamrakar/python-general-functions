from FreqObjectOps.StrOps import StrOps


def test_is_camel_case_where_small_camel_case():
    assert StrOps.is_camel_case("smallcamelCase") is True


def test_is_camel_case_where_capital_camel_case():
    assert StrOps.is_camel_case("CapitalcamelCase") is True


def test_is_camel_case_where_snake_case():
    assert StrOps.is_camel_case("snake_CASE") is False


def test_is_camel_case_where_linebreak():
    assert StrOps.is_camel_case("""line\nbreak""") is False


def test_is_camel_case_where_spaces():
    assert StrOps.is_camel_case("""spaces in text""") is False


def test_is_camel_case_where_symbol():
    symbols = """`~!@#$%^&*()-_=+[]{};':"\\|,./<>?"""
    for s in symbols:
        assert StrOps.is_camel_case("""symbol{0}Found""".format(s)) is False


def test_remove_accent_where_accented():
    accented_text = "àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÄËÏÖÜŸçÇßØøÅåÆæœ"
    normal_text = "aeiouAEIOUaeiouyAEIOUYaeiouAEIOUanoANOaeiouAEIOUYcCssOoAaAEaeoe"
    assert StrOps.remove_accent(accented_text) == normal_text


def test_clean_snake_case():
    assert StrOps.clean_snake_case("àbc__DÊF_") == "abc_DEF_"


def test_to_alpha_numeric():
    assert (
        StrOps.text_to_alpha_numeric("abc yyyy/mm/dd", replace_string="_")
        == "abc_yyyy_mm_dd"
    )


def test_text_to_camel_case_upper():
    assert StrOps.text_to_camel_case("Àbc dêf", case="upper") == "AbcDef"


def test_text_to_camel_case_lower():
    assert StrOps.text_to_camel_case("Àbc dêf", case="lower") == "abcDef"


def test_camel_case_to_snake_case_upper():
    assert StrOps.camel_case_to_snake_case("abcDef", case="upper") == "ABC_DEF"


def test_camel_case_to_snake_case_lower():
    assert StrOps.camel_case_to_snake_case("AbcDef", case="lower") == "abc_def"


def test_text_to_snake_case_from_camel():
    assert StrOps.text_to_snake_case("abcDef", case="lower") == "abc_def"


def test_text_to_snake_case_from_normal():
    assert (
        StrOps.text_to_snake_case("abc def yyyy/mm-dd 123", case="lower")
        == "abc_def_yyyy_mm_dd_123"
    )
