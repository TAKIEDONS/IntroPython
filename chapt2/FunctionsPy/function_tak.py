# functions are defined using the def keyword, then
# the : character and whitespace define the function body

def candidates_args(strname,phone, *address_args):
    print(strname, phone)
    for arg in address_args:
        print(arg)

candidates_args("Takalani", "Nemadondoni", "president park","Moddrefointein Park", 35)
