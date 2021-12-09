# Case Study 01 Journal

This journal provides the overview of case study's activities (transactions) for future reference. Records of steps taken are accompanied with effort entries (in square brackets) measured in fibonacci story points (fsp). The reflection process encompasses also moving recent journal entries into the archive section.

## Design Document Transformations

**Master Process**. In order to *map CDS methods*:
- map references to the CDS methods in Kitchin (2021b) > DONE: see Journal 2021-11-30/2
- search web resources to identify critical data studies,
- analyse search results and plan next steps.

**Next Steps**. See [20211202_Search_Web_Resources.ipynb](https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/cs01_cds_methods/20211202_Search_Web_Resources.ipynb)

Candidates for other next steps:
- [ ] ...

## Journal Recent Activities
**2021-12-09 Thu** (1) **KnoxNafus-2018**. This focus on expertise allows us to do something that is relatively unusual in an edited collection: both to provide a comparative description of a number of empirical fieldsites where communities of experts are self-consciously forming around the new possibilities put on the table by digital data; and to consider how our understanding of the ways experts make and remake digital data might reframe our own expertise as ethnographers. (2) **Grommé et al. (2017)**. Our concern in this chapter is how data scientists are being defined in relation to national statisticians and how both professions are objects of struggle with ambiguous outcomes.

**2021-12-06 Mon**
- (1) **Last Sprint Reflection**. The study is rooted in an idea of freelancing as an external expert / evaluator for grant agencies. While registering in the EU grant portal and the TACR system I became aware of publications being a part of references. Inspired by Kitchin (2021b), I started this case study with a goal to produce a kind of academic text. In the first sprint over last two weeks I built an internal information management system with HTML files used as an interface.
- (2) **Next Sprint Inception**. The next sprint should be devoted to analysis and modeling of critical data studies. What is their general architecture of roles, goals, processes, events, assets, locations and their relatinships? Now, I can keep my observations in HTML files in structured expresions for further consolidation, comparison, and evaluation. I should keep the architecture as simple as possible. The key concepts can be retrived directly from Kitchin (2021b). [1 fsp]
- (3) **Knox and Nafus 2018**. An introduction to the book is a part of a Kindle edition ebook's sample. It is not an easy read. The next chapter is the Grommé et al. (2018) study which is free accessible on Internet. See [package_20211206.html](https://htmlpreview.github.io/?https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/data/cd_studies/package_20211206.html). [5 fsp]

## Curate Backlog and ToDos
- [ ] Document the knowledge base with Term-Association Ontology Internal Information Management (TAO-IIM)
- [ ] Clarify the nature of CDS methods and check their employment in selected documents

## Archive Journal Entries
### A Data Expert Critically Studies Data (Ne 21.11. - So 4.12.2021)

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


**2021-12-01 Wed**:
- (1) **Re-Design the Ontology**. I am tempted to extract authors, publishers and other concepts while searching web resources for collected publications. But! I have to proceed rigorously and lazily. Otherwise the amount of work needed to finish the case study becomes unmanageable. I plan to employ algorithmic web search with automatic extraction of a website address (aka internet node with an IP address). [4 fsp]
- (2) **Refactor the KB** The *Refactor concept names* process includes steps:
  - prepare a change dict in line with the new oncept model (ontology)
  - apply the change dict to tables
  - adjust and test algorithms with this new ontology
  - reflect :: The new ontology requires more care when using terms in outputs but is much clearer when selecting concepts (classes). [4 fsp]
- (3) **Plan Web Searching Engine**. I don't need to be a CSD expert, I just need to be able to monitor published CDSs and evaluate methods they utilize. Automated web searching engine ensures simple updating (to produce focused annual reports). [2 fsp]


**2021-12-02 Thu**
- (1) **Search Web Prototype I**. Understand the need, specify the quest, code and test the `search_web(master, search, count)` function in [20211202_Search_Web_Resources.ipynb](https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/cs01_cds_methods/20211202_Search_Web_Resources.ipynb), outline the next step, reflect that all in the journal. [7 fsp]
- (2) **Search Web Prototype II** The [20211202_Search_Web_Resources.ipynb](https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/cs01_cds_methods/20211202_Search_Web_Resources.ipynb) notebook contains all the step to populate the `url_master.csv` dataset with responses to the carefully crafted google searches. Populating the **URL master dataset** assumes manual addition of terms for further identification and analysis of the retrieved web resources. This semi-automated process is now prepared for populating the URL master dataset with the web resources from the CDS domain inspired by [CDS_methods_instantiated.md](https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/cs01_cds_methods/CDS_methods_instantiated.md). I just ply my trade with rigor, reflection, and care. [7 fsp]

**2021-12-03 Fri**
- (1) **CSV <> HTML**. A semi-automated analytical system needs a semi-automated interface. Editing TXT a CSV files is the simplest method. A little bit more sophisticated method is to export, edit, and import an HTML file. Especially if this pipeline enables authomatic adding new fields. How flexible analytic tool! See [20211203_Transform_CSV_HTML.ipynb](20211203_Transform_CSV_HTML.ipynb) and [test.html](https://htmlpreview.github.io/?https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/data/web_searches/test.html). [6 fsp]
- (2) **CDS Hunt Start**. Idenitify the most common words in CDS's titles ([20211204_Search_CDS.ipynb](20211204_Search_CDS.ipynb)) and try the first search: [url_review_20211203.html](https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/data/web_searches/url_review_20211203.html) (plain) | [url_review_20211203.html](https://htmlpreview.github.io/?https://github.com/lustraka/data-analyst-portfolio-project-2022/blob/main/data/web_searches/url_review_20211203.html) (rendered) or work with a local copy which apllies an in-file stylesheet. [3 fsp]

**2021-12-04 Sat**. (1) **`infon`**. A field `infon` (= information + JSON) contains structed data in the JSON format. It is a kind of a bottom-up data structure design or of the semi-structured note-taking. (2) **Gathering**. While processing the results of `data+university+society+digital+information+2021` query, I found one new CSD and was alluded by EC digital strategy to European Digital Innovation Hubs. [7 fsp]

# The End of a Story
