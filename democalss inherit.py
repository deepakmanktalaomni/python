import democlass
def monkey_f(self):
    print ("monkey_f()")


democlass.myClass.f = monkey_f
obj = democlass.myClass()
obj.f()
