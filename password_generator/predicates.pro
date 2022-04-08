:- include( 'dictionary.pro' ).

remove_atom( [], [] ).
remove_atom( [ X|Xs ], [ X|Ys ] ) :- var( X ),
remove_atom( Xs, Ys ).
remove_atom( [ X|Xs ], Ys ) :- nonvar( X ),
remove_atom( Xs, Ys ).

generate( Xs, X, Y, Ys ) :-
remove_atom( Y, Zs ), call( X, Xs, Zs ),
atomic_list_concat( Y, Ys ).
