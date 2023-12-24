:- dynamic playlist/2.

playlist(Name, []) :-
    asserta(playlist(Name, [])),
    write('Playlist added successfully\n').

add_song(Name, Title, Artist, UpdatedPlaylist) :-
    retract(playlist(Name, Songs)),
    append([[Title, Artist]], Songs, NewSongs),
    asserta(playlist(Name, NewSongs)),
    UpdatedPlaylist = playlist(Name, NewSongs),
    write('Song added successfully\n').

display_playlist(Name) :-
    playlist(Name, Songs),
    write('Playlist: '), write(Name), nl,
    write('Songs:'), nl,
    display_songs(Songs),
    !.

display_songs([]).
display_songs([[Title, Artist] | Rest]) :-
    write('  - '), write(Title), write(' by '), write(Artist), nl,
    display_songs(Rest),
    !.
display_songs(Songs) :-
    \+ is_list(Songs),
    write('Invalid song list\n'),
    fail.
