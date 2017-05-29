

#two solutions here, one the easy way (not in the spirit of the question,
# but practical) and the 2 stack sort method the book it looking for


#K.I.S.S. 
#within stack class, I added the following:  
    def sort_stack(self):
        self.stack.sort(reverse=True)


#alternative, using a buffer stack and a temporary value holder
def sort_stack(input_stack):
    buffer_stack = stack(input_stack.pop())
    while input_stack.isEmpty == False:
        temp = input_stack.pop()
        while buffer_stack.peek() > temp:
            input_stack.add(buffer_stack.pop())
        buffer_stack.add(temp)
    return buffer_stack

