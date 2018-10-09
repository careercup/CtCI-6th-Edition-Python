#-----------------------------------------------------------------------
# Strip all spaces at the end of string and then replace spaces with %20
#-----------------------------------------------------------------------
def urlify(s):
    new_s = s.rstrip()
    url = new_s.replace(" ", "%20")
    return url

inp = "I am$ be is fine,9"
test = inp.split(',')[0]
make_url = urlify(test)
