Select *
FROM Track
LEFT OUTER JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
LEFT OUTER JOIN Genre ON Genre.GenreId =Track.GenreId
LEFT OUTER JOIN Album ON Album.AlbumId = Track.AlbumId
LEFT OUTER JOIN Artist ON Artist.ArtistId = Album.ArtistId
