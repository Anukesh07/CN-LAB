size=int(input("Enter the size of the bucket : "))
out=int(input("Enter the output rate : "))
n=int(input("Enter the number of inputs :" ))
store=0
for i in range(n):
    inc=int(input("Enter the incoming packet size : "))
    print("Incoming packet size is : {}".format(inc))
    if(inc<=(size-store)):
        store+=inc
        print("Bucket buffer size {} out of {}".format(store,size))
    else:
        print("Dropped {} number of packets ".format(inc-(size-store)))
        print("Bucket buffer size is {} out of {}".format(store,size))
        store=size
    store=store-out
    print("After outgoing {} packets left out of {} in buffer ".format(store,size))
