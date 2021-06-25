========================Timestamp DATA TYPE===========================
SELECT author_name, book_name, 
 writetime(book_name) FROM books_by_author;

# timestamp nije dozvoljen nad kolonom koja je deo primarnog kljuca
SELECT author_name, book_name, 
 writetime(author_name) FROM books_by_author;

======================== UUID DATA TYPE===============================
INSERT INTO books_by_author (author_name, publish_year, book_id, book_name, rating)
VALUES('James Patterson',2017, uuid(),'Manning',4.0);

SELECT * FROM books_by_author 
WHERE author_name= 'James Patterson'

#UUID - je 128-bit heksadecimalna vrednost.

======================== SET DATA TYPE===============================
# Set tip podataka se skladisti kao kolekcija elemenata. Elemnti nisu uredjeni ali u CMD (CQLSH) 
# se vracaju elementi kao da su sortirani. 

ALTER TABLE books_by_author 
		ADD emails set<text>;

DESCRIBE TABLE books_by_author;

UPDATE books_by_author SET emails = {'james_patter@gmail.com'} 
	WHERE author_name= 'James Patterson';

UPDATE books_by_author SET emails = emails + {'james_patterson123@gmail.com'} 
	WHERE author_name= 'James Patterson';

UPDATE books_by_author SET emails = emails - {'james_patter@gmail.com'} 
	WHERE author_name= 'James Patterson';

UPDATE books_by_author SET emails = {} 
	WHERE author_name= 'James Patterson';

======================== LIST DATA TYPE===============================
# List tip podataka sadrzi sortira elemente u odredjenom redosledu. Defoltno,
# vrednosti u listi se smestaju po redosledu ubacivanja

ALTER TABLE books_by_author 
	ADD phone_numbers list<text>;

UPDATE books_by_author SET phone_numbers = [ '1-800-000-9999' ] 
	WHERE author_name= 'James Patterson';

UPDATE books_by_author SET phone_numbers = phone_numbers + [ '080-111-111-111' ] 
	WHERE author_name= 'James Patterson';

UPDATE books_by_author SET phone_numbers[1] = '480-111-1111' 
	WHERE author_name= 'James Patterson';

DELETE phone_numbers[0] from books_by_author 
	WHERE author_name= 'James Patterson';

======================= MAP DATA TYPE ================================
# Mapa sadrzi kolekciju parova key/value 

ALTER TABLE books_by_author 
	ADD login_sessions map<timeuuid, int>; 
