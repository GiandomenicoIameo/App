member( X, [ X|_ ] ).
member( X, [ _|Xs ] ) :- member( X, Xs ).

delete( Y, [ Y|Ys ], Ys ).
delete( X, [ Y|Ys ], [ Y|Zs ] ) :-
delete( X, Ys, Zs ).

generate_binomial( [], [] ).
generate_binomial( [ X|Xs ], [ X|Ys ] ) :-
generate_binomial( Xs, Ys ).
generate_binomial( [ _|Xs ], Ys ) :-
generate_binomial( Xs, Ys ).

combination( _, [] ).
combination( Ys, [ X|Xs ] ) :- member( X, Ys ),
combination( Ys, Xs ).

permutation( [], _, [] ).
permutation( [ X|_ ], Acc, [ X|Ys ] ) :- delete( X, Acc, Zs ),
permutation( Zs, Zs, Ys ).
permutation( [ _|Xs ], Acc, Ys ) :-
permutation( Xs, Acc, Ys ).

binomial( Xs, Zs ) :- sort( Xs, Ys ),
generate_binomial( Ys, Zs ).

disposition( Xs, Ys ) :-
permutation( Xs, Xs, Ys ).

remove_atom( [], [] ).
remove_atom( [ X|Xs ], [ X|Ys ] ) :- var( X ),
remove_atom( Xs, Ys ).
remove_atom( [ X|Xs ], Ys ) :- nonvar( X ),
remove_atom( Xs, Ys ).

init( Xs, X, Y, Ys ) :- remove_atom( Y, Zs ),
call( X, Xs, Zs ), atomic_list_concat( Y, Ys ).
