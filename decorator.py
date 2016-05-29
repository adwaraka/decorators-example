from operator import itemgetter

def call_formatter(func):
    def inner(*args, **kwargs):
        #print args 
		#(['Mike', 'Thomson', '20', 'M'],)
        values_list = args[0]
        if values_list[-1] == "M":
            print "Mr. {} {}".format(values_list[0], values_list[1])
        else:
            print "Ms. {} {}".format(values_list[0], values_list[1])
        return func(*args, **kwargs)
    return inner

@call_formatter
def parse_name(record):
    pass

def main():
    count = int(raw_input())
    list_input = []
    for _ in xrange(count):
        to_list = []
        to_list = str(raw_input()).split(" ")
        list_input.append(to_list)

    list_input.sort(key=itemgetter(2))
    #print list_input
	#input 
	#1
	#Mike Thomson 20 M
    for val in list_input:
        parse_name(val)


main()