# Data Model

# Organize Data
![Class Model](https://www.plantuml.com/plantuml/png/TL1BJWCn3Dtd556tg1Li4OiME00Ix94dCJGYdyXs15NLkvFCP1YaWOq_VdxFdpqBa9JWrT5Pr1Yod7J0C22nCXwOzJC2cQC-goljR3NubQaw2m83CDQGa8iNhb5CWkgYElC9Cj92X2B7HAtjXD0an8d71Wmi14Pg-F7Py4A-JKYksbo6Lui2pgy779hYD252m4NvdLB9g_Q750rc-TrlySr59ox5cd0gP715Uo6NFOuiz7WO3_PJSly_wz6ngGXZVm12TMRQu2zMV_Fsh3VNkrtSJDzJesrLlRbfvNxpND_Eszrg9gFlL4ylbT7FLTrNaMMfXJ-N5eaVQ2REm1wZBS5_0m00)

# MarkDown Structures
## Concepts, Triples, Discourse
### Concepts
name|definition|source|note
-|-|-|-
"name"|"definition"|"source"|"note"

### Triples
eleA|rel|eleB|source|note
-|-|-|-|-
"eleA"|rel|"eleB"|"source"|"note"

### Discourse
idea|concept|source|note
-|-|-|-
"idea"|"concept"|"source"|"note"

# CSV Structures
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
"idea","concept","source","note"
```


