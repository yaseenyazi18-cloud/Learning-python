

def check_scope():
    def do_local():
        text = "local list"
    def do_no_local():
        nonlocal text
        text = "non local list"   
    def do_global():
        global text
        text = "global list"
                                                         
    text = "default"
    do_local()
    print(text)
    do_no_local()
    print(text)
    do_global()
    print(text)


check_scope()
print(text)