# Oil & Gas Industry Case Study
Model the value chain.

## Clarify Purpose
The purpose of this case study is to build a business knowledge blueprint for the given domain using automated web searches combined with focused reading. The general idea is to:
- build a catalogue of (noun) concepts representing key domain's elements
- identify triples representing an ontology with the main focus on a value chain (or business model)
   - the subject (a noun concept) is a concept (class), e.g. an actor
   - the predicate (a verb concept + a noun concept) represents a relation to some other concept, e.g. a product 
   - elements of a triple use underscore ('_') in place of space, spaces separate the three elements of the triple
- use automated and manual searches to populate the ontology
- report key findings

Key deliverables are:
- web searches in CSV format : `['inn', 'title', 'url']`
- `_concepts.csv` in CSV format : `['concept', 'title', 'url']`
- `_triples.csv` in CSV format : `['triple', 'url']`
- exploratory notebooks
- explanatory reports

Using HTML files as explanatory reports ensures the capability of automated curation of the body of knowledge.


## Observations
- Using `web_search()` from local returns some page asking for a user's action. To scrape the web it is important to run the code in Google Colab.
