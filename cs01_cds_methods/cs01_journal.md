# Case Study 01 Journal

This journal provides the overview of case study's activities (transactions) for future reference. Records of steps taken are accompanied with effort entries (in square brackets) measured in fibonacci story points (fsp). The reflection process encompasses also moving recent journal entries into the archive section.

## Design Document Transformations
The *Refactor concept names* process includes steps:
- prepare a change dict in line with a concept model
- apply the change dict to tables
- adjust and test algorithms with this new convention

The *Map CDS methods based on Kitchen (2021b)* process includes steps:
- *Map references to the CDS methods based on Kitchin (2021b)* process (See Journal 2021-11-30/2)
- find out web resources and choose appropriate examples of each CDS method,
- add the **"embodies"** type triples and elements with the `title` and `url` attributes by hand,
- check the integrity of the knowledge base.

Candidates for next steps are:
- [ ] Change "a CDS *uses* a method" relation type to "a CSD *employs* a method" type Consider same change for *instantiates*.

## Journal Recent Activities
**2021-12-01 Wed**:
- (1) **Design an Ontology**. I am tempted to extract authors, publishers and other concepts while searching web resources for collected publications. But! I have to proceed rigorously and lazily. Otherwise the amount of work needed to finish the case study becomes unmanageable. I plan to employ algorithmic web search with automatic extraction of a website address (aka internet node with an IP address). [4 fsp]

**2021-11-30 Tue**:
- (1) **Boot-Root**. The *Set-up a node for case study* process includes steps:
  - create a `cs01_scd_methods` subfolder in the `data-analyst-portfolio-2022` repository,
  - create a `Readme.md` root document structured properly to focus attention,
  - create a `data` subfolder in the `data-analyst-portfolio-2022` repository and upload the baseline files of the knowledge base,
  - create the first IPYNB notebook to populate the knowledge base and test loading, updating, and dumping the knowledge base,
  - create a jounal, document the effort so far, and plan the next step [6 fsp].
- (2) **CDS References**. The *Map references to the CDS methods based on Kitchen (2021b)* process includes steps:
  - process the **"cites"** type  triples and the **"instantiates"** type triples for CDS methods in Kitchen (2021b)
  - dump the knowledge base for manual embelishment
  - add titles of references [8 fsp]
- (3) **Modus Operandi**. While embelishing data by hand I can use a local clone of the GitHub repository, then pull changes to origin and download files again in Colab.
- (4) [Critical Data Studies Methods Instantiated (Temporarily)](CDS_methods_instantiated.md) generated for further planning and processing [2 fsp]


## Curate Backlog and ToDos
- [ ] Document the knowledge base with Term-Association Ontology Internal Information Management (TAO-IIM)
- [ ] Clarify the nature of CDS methods and check their employment in selected documents

## Archive Journal Entries
