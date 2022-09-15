# Data Model

# Organize Data
![Class Model](https://www.plantuml.com/plantuml/png/TL7DJiCm3BxdAQnUOHjS9muRJ9oOX80xSbF38j8aSXp1DEtTITQ68WrwYDtlnuwTLHHaIRrLEzCHK1za3ptrBN5KscACy4p8UWS7TG6cWoKyvM-xtMncpcM8lWBdqA5WYv5ooXIJbPWpvuNKKOrr7Z4GJsMQ1uSzNS9z2R3O4_AYoIGcsNakzWBb84Oi5QADmgWbfn-VXKziIsTlyXbI-zgHeB7dZTUbuj2vz9eglxDFuKn-vvsc8B_r7RqPPyJuCd7qYJMTsLxO14id5rbQdnPXXv_R_rqR4tLc8esB8VnBEpx1x03DrNpkcc6NwdGM59hh0e-JLdnMxxI4o1fkL9tic2q3DKb_BbBL4rLjbL0hSbtgxJS0)

**searches.csv**
```
id,"expr",database,results,"note"
```
**papers.csv**
```
"id","authors",year,"title","abstract","kws",url,doi,"pub_details","note"
```
```
aspect|value
-|-
id|**** []
authors|
title|[]()
abstract|
kws|
doi|
pub_details|
note|
```
**authors.csv**
```
"name",year,"group","note"
```
**concepts.csv**
```
"name","definition","source","note"
```
**triples.csv**
```
"eleA",rel,"eleB","source","note"
```
> Specializations
```
search,retrieves,"paper",searches,"note"
```
**discourse.csv**
```
"idea","source","note"
```


