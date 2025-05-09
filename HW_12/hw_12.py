

def new_format(current_str):
    current_str = "{:,}".format(int(current_str)).replace(",",".")
    return current_str

print(new_format("1000000"))
print(type(new_format("1000")))
assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
