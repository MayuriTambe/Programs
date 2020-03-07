marks={66,34,76,55,98,57,63}
weights={45,63,76,89,65,39,48}

Intersection=marks.intersection(weights)
print("The intersection using intersection function is:",Intersection)

Intersection=(marks&weights)
print("The intersection using & operator is:",Intersection)