import regex

from functools import partial as p
from functools import reduce
import regex as re

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

# #### Special character normalization

decode_caret_return = p(re.sub, "_x000D_", "\r")
assert decode_caret_return("_x000D_") == "\r"

remove_caret_return = p(re.sub, "\r", "")

# #### Cosmetics
deduplicate_commas = p(re.sub, ",{2,}", ",")
assert deduplicate_commas(r",,,\\,,,\\,\,,") == r",\\,\\,\,"

deduplicate_multiple_linefeeds = p(re.sub, "\n{1,}", "\n", flags=re.M)
assert deduplicate_multiple_linefeeds("\n\n\n\n\n\n\n") == "\n"

ensure_space_after_semicolon = p(re.sub, r";(?=\w)", "; ")

deduplicate_spaces = p(re.sub, " {2,}", " ")

strip = lambda x: x.strip()


cleaning_function = compose(
    *reversed([
    # return caret normalization
    decode_caret_return,
    remove_caret_return,
    # misc
    deduplicate_commas,
    # cosmetics
    deduplicate_multiple_linefeeds,
    ensure_space_after_semicolon,
    deduplicate_spaces,
    strip,
    ])
)
