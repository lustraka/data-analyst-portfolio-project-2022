# Train SL-Reviewer Model
> **Vision**: Channeling the flow of meaning between academies and businesses.

# Clarify Purpose
**Purpose**. A crutial step of drafting R&d proposals is providing information about the current state of the domain. Obviously, an appropriate input for this step is a systematic literature review (SLR). Therefore, the goal of this case study is to set up a model for conducting SLRs based on some methodological sources and 8 selected review studies. The next step will be the validation of the model using another 5 studies as a benchmark.

> “An **SLR** is a review of an existing body of literature that follows a transparent and reproducible methodology in searching, assessing its quality and synthesizing it, with a high level of objectivity.” (Kraus et al., 2020)

# Collect Elements
**Key Concepts** in this study are requirements/guidelines which can build up checklists for conducting SLRs in their contexts. These requirements can be [enforced on various levels](https://www.sciencedirect.com/topics/computer-science/enforcement-level) (from strictly enforced to guideline) invocating appropriate consequences. The model systemizing these requirements will allow to derive appropriate set of requirment for the review task at hand.

----

**Double S Approach**. Beside the systematic approach to searching papers and assessing their quality, there is an opportunity to apply the methodology of requirements specification to the subject matter of the review study. Identify requirements and evaluate thier fullfilment in relevant resources. Identify the gaps and specify requirements for the next developmental stage of the given system or domain.

**EARS CheatSheet**

![EARS CheatSheet](https://www.plantuml.com/plantuml/png/RP11ImCn48Nl-HLp3chkMv5UAXP4eLeyJtUdkmFPsJKpgVZlJMe55tfzyxxtahTMmsHvZAxPqMVcH2E9wShf7DbSipzmKMtAVn9WZookUJCqkkqIdqXMhlbusZvlu3u45a3GcLe-SWjQNI4yG5ZIcqBPVthpKc5BtFUKhW2li_4a6E58Q3dHBxGxLruaO0MMDkQEkYi9U_b2CUhWG0EUUCgfP6mVbxKty5wV4Xn91vS9lBU1lAz6_LQZ4GJ7ywUyrm5ZNDmIwJo9rljTSEkIKyRz0G00)

# Compose Interactions
**MVP**. What is the minimum viable review assembly line that allows me to produce a minimum viable standalone systematic literature review?

**3S Competitive Advantage**. The "systematic review consultancy" Google search retrieves for example [Systematic Review Consultants LTD](https://systematicreview.info/) and a couple of opportunities on job sites (Fiverr, Upwork, Kolabtree). You need to build and maintain your competitive advantage strategically, systematically, and systemically.

# Manage Content With OODA

Folder|Content|Note
-|-|-
[01_Admin](./01_Admin)|[Journal_master](./01_Admin/Journal_master.md) * [PLCM_master](./01_Admin/PLCM_master.md)|GODA(s), PLCM, Journal
[02_TopicMaps](./02_TopicMaps)|[20220825_KickOff](./02_TopicMaps/20220825_KickOff.md) * [20220828_google_SLR_SM](./02_TopicMaps/20220828_google_SLR_SM.md) * [BolandA-2017](./02_TopicMaps/BolandA-2017.md) * [GusenbauerHaddaway-2019](./02_TopicMaps/GusenbauerHaddaway-2019.md) * [OosterwykG+2019](./02_TopicMaps/OosterwykG+2019.md)|Search, Document
[03_FullTexts](./03_FullTexts)||.pdf
[04_DataBase](./04_DataBase)|[AI_SLR_examples](./04_DataBase/AI_SLR_examples.ris) * [AI_SLR_examples](./04_DataBase/AI_SLR_examples.xls) * [authors](./04_DataBase/authors.csv) * [concepts](./04_DataBase/concepts.csv) * [DataModel](./04_DataBase/DataModel.md) * [data_extraction_sheet](./04_DataBase/data_extraction_sheet.xlsx) * [discourse](./04_DataBase/discourse.csv) * [papers](./04_DataBase/papers.csv) * [searches](./04_DataBase/searches.csv) * [triples](./04_DataBase/triples.csv) * [WoS-GusenbauerMichael](./04_DataBase/WoS-GusenbauerMichael.ris)|DataModel, .csv, downloads
[05_CodeBase](./05_CodeBase)|[20220825-data_extraction_sheet](./05_CodeBase/20220825-data_extraction_sheet.ipynb) * [Admin](./05_CodeBase/Admin.ipynb) * [Collect_Data_Concepts](./05_CodeBase/Collect_Data_Concepts.ipynb) * [Collect_Data_Papers](./05_CodeBase/Collect_Data_Papers.ipynb) * [slr](./05_CodeBase/slr.py)|Jupyter Notebooks
[06_CRM](./06_CRM)|[Readme](./06_CRM/Readme.md)|Dissemination, Exploitation, Communication

- Manage the product's life cycle in [PLCM](./01_Admin/PLCM_master.md)
- Review progress and keep a journal in [Journal](./01_Admin/Journal_master.md)
- Review the point of departure in [20220825_KickOff](./02_TopicMaps/20220825_KickOff.md)
- Map documents in [02_TopicMaps](./02_TopicMaps)
- Store search results in [04_DataBase](./04_DataBase/)
- Manage data in [04_DataBase](./04_DataBase/) in line with [Data Model](./04_DataBase/DataModel.md)
- Process data in [05_CodeBase](./05_CodeBase/)
- Report findings in [06_CRM](./06_CRM/Readme.md)


----

- [ ] Take notes from the paper [Ref_GusenbauerHaddaway-20191015.md](./03_Info/Ref_GusenbauerHaddaway-20191015.md) (SLR suitable search systems)


## GODA Template
WP XYZ|OVI|SoV| Assumptions
-|-|-|-
**Goal**|(impact)|-|
**Objective**|(outcome)|-|-
**Deliverable** 1|(output)|-|-
Deliverable 2|(output)|-|-
**Activities**|**Effort**|**Budget**|-

OVI = Objectively Verifiable Indicators (Indicator = Concept + **Q**uantity (Target) + **Q**uality (Standard) + **T**ime > QQT) | SoV = Source of Verification

