from autocompleter import Autocompleter

a = Autocompleter()

prev = input()
for i in range(10):
    w = a.get_next([prev])
    print(w)
    prev = w