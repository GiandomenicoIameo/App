member( X, [ X|_ ] ).
member( X, [ _|Xs ] ) :- member( X, Xs ).

element( Xs, Ns ) :- length( Xs, Ns ).
element( [ _|Xs ], Ns ) :-
element( Xs, Ns ).

delete( Y, [ Y|Ys ], Ys ).
delete( X, [ Y|Ys ], [ Y|Zs ] ) :- delete( X, Ys, Zs ).

binomial( [], [] ).
binomial( [ X|Xs ], [ X|Ys ] ) :- binomial( Xs, Ys ).
binomial( [ _|Xs ], Ys ) :- binomial( Xs, Ys ).

combination( _, [], 0 ).
combination( Ys, [ X|Xs ], Ns ) :- Ns > 0, Ms is Ns - 1,
combination( Ys, Xs, Ms ), member( X, Ys ).

permutation( [], _, [] ).
permutation( [ X|_ ], Acc, [ X|Ys ] ) :- delete( X, Acc, Zs ),
permutation( Zs, Zs, Ys ).
permutation( [ _|Xs ], Acc, Ys ) :- permutation( Xs, Acc, Ys ).

combination_generate( Xs, X ) :- element( Xs, Ns ),
combination( Xs, X, Ns ).

binomial_generate( Xs, Zs ) :- sort( Xs, Ys ),
binomial( Ys, Zs ).

disposition_generate( Xs, Ys ) :- permutation( Xs, Xs, Ys ).

remove_nonvar( [], [] ).
remove_nonvar( [ X|Xs ], [ X|Ys ] ) :- var( X ),
remove_nonvar( Xs, Ys ).
remove_nonvar( [ X|Xs ], Ys ) :- nonvar( X ),
remove_nonvar( Xs, Ys ).

generate( Xs, X, Y, Ys ) :-
remove_nonvar( Y, Zs ), call( X, Xs, Zs ),
atomic_list_concat( Y, Ys ).
