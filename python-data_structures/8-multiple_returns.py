#!usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        length="None"
        print("Length: {:d} ".format(length))
    else :
        length= len(sentence)
        first= sentence[:1]
        print("Length: {:d} - First character: {}".format(length, first))
