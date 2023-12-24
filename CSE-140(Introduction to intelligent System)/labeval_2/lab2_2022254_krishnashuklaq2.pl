breed(dachshund, small).
breed(chihuahua, small).
breed(beagle, medium).
breed(boxer, large).
color(dachshund, brown).
color(chihuahua, tan).
color(beagle, white_and_brown).
color(boxer, fawn).
person(john, chihuahua).
person(sara, beagle).
person(mike, boxer).
person(amy, dachshund).
small_dog(X) :- breed(X, small).
medium_dog(X) :- breed(X, medium).
large_dog(X) :- breed(X, large).
brown_dog(X) :- color(X, brown).
tan_dog(X) :- color(X, tan).
white_and_brown_dog(X) :- color(X, white_and_brown).
fawn_dog(X) :- color(X, fawn).
dog_owner(X, Y) :- person(X, Z), breed(Z, Y).
owner(Z,X):-breed(Z,small),person(X,Z).
color(beagle,X).
person(amy,X),breed(X,small).

