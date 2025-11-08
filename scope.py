def check_scope():
    def do_local():
        test = "local test"
    def do_non_local():
        nonlocal test
        test = "non local test"    
    def do_globel():
        global test
        test = "globel test" 

    
    test = "default" 
    
    do_local()
    print("Text value after do_local : ",test) 
    
    do_non_local()
    print("Text value after do_non_local : ",test) 
    
    do_globel()
    print("Text value after globel_test :",test) 



check_scope()
print("Text value after globel_test :",test) 