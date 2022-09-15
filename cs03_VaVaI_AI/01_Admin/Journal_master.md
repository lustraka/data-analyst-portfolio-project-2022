# Journal
## Systematic Literature Review(er and Sensemaker)
**2022-08-28 Sun**. What is the state-of-the-art of systematic literature reviews? Do they relate to sensemaking (both organization and information science)? To learn about sensemaking, read [CulmseeP-2013](https://workflowy.com/#/81653a4589d6) or check [Wikipedia](https://en.wikipedia.org/wiki/Sensemaking), [a conversation with Paul Culmsee](https://eight2late.wordpress.com/2014/06/18/making-sense-of-sensemaking-a-conversation-with-paul-culmsee/), or [CogNexus Institue](http://cognexus.org/id41.htm).

**2022-08-28 Sun** (1) I tested the SLR dataware architecture (CSV files). (2) I collected other useful papers on SLRs, including "review of reviews". These papers can be used to develop an "assebly line" or "assembly model" for systematic literature reviews. I have plenty of resources and I need to simplify and focus on a minimum viable product. The key output of this campaing should be (a) a description of a protocol and (b) an example to be used in collaboration offers (bids, pitches).


## Sprint Wrangle SLR Requirements
**2022-08-31 Wed** (1) **Extract requirements**. The first step of extracting requirments is focused on `Oosterwyk, Grant et al (2019)`. (a) Input data into `concepts.csv` or `discourse.csv`. (2) Check and output data for further use in appropriate Jupyter notebook. There are a couple of formats - plain text, html or md. Last two (html, md) need to copy-paste output to a markdown cell. The markdown formating provides most flexible rendering - notes and maybe also sources can be listed below the main table. (2) **Next steps**. (a) I need to saturate the list of requirements to the state where there is nothing to remove without losing significant value (rather than to add more details). (b) Then I can map the content of selected AI SLRs. (c) While doing (a) and (b) I can build the execution engine of the SL-Reviewer model.

**Oosterwyk, Grant et al (2019)**

The table x compares the SL-Reviewer's states with five major stages identified by Oosterwyk (2019) and the CADIMA protocol.
SL-Reviewer's states|Key stages by Oosterwyk (2019) | CADIMA Protocol
-|-|-
Ask questions (SAQ)|Define the protocol|
Collect data (SCD)|Search the literature<br />Select the papers|Literature search
Explore data (SED)|<b>Analyse</b>, synthesise and interpret|Data extraction<br />Critical appraisal
Synthesise knowledge (SSK)|Analyse, <b>synthesise and interpret</b>|Data synthesis
Write the review (SWR)|Write the review|Presenting data/results

**2022-09-02 Fri**. (1) **Root Questions**. The markdown passports for papers in [20220828_google_SLR_SM.md](../03_Info/20220828_google_SLR_SM.md) originated from the first search managed in CSV and IPYNB. The table with root questions derived from abstracts enable focusing on the next steps. On the other hand, to markdown passports for papers in [Oosterwyk_Grant_et_al_2019.md](../03_Info/Oosterwyk_Grant_et_al_2019.md) has been filled manually based on the refrences in Oosterwyk. There is another interesting paper on onthological meta-analysis and synthesis by Ramaprasad & Syn (2015) published along with a couple of other articles from this batch. Again, root questins enable OODA cycle. (2) **Bright, Light, Blind/Blank Spots**. The ontological approach from Ramaprasad & Syn (2015) is well suited for innovation-friendly SLRs. It is possible to combine it with requirment-based approach? Aren't requirments just logical components? An ontological approach enables more flexible derivation of features and requirments, I think.

**2022-09-07 Tue through 11 Sun**. Contemplate a systematic reviewer career at cottage in Polom. Read selected papers, clarify vision and mission. Should I extract requirments or checklist statements?

## Sprint Restart
**2022-09-14 Wed**. (1) Update a protocol with a hermeneutics cycle ACADAS. (2) Update a root page with systemic view (clarify purpose, collect elements, compose interactions). (3) Focus on MPVs and building 3S competitive advantage (strategic, systematic, systemic).

**2022-09-15 Tue** (1) **VaVaI FileConfig**. Adoption of BolandA-2017 file structure leads to confusion, partly because it presuppose a sequential protocol. A new FileConfig is more hermeneutic-friendly.

![FileConfig](https://www.plantuml.com/plantuml/png/JL9DRnen4BtpA-O8GaG9-KXx2rcQAcqfg44v8LN6di2qtXdBdat3lo-nZR9xclUnJ-DdtoKrKLjYrvemK5AFy1qnm0DvJ40Co-Wmml0TDy8lj1iDnl1iditZXYV7RyFtuWsxsMHwVd4x68_X_09cxXXvdCU_uUjoFXkcKG6h7yq2XiJMdsquH56nuglsHxh8nkU4AQmba5sOa8huX2RQVPddOhiMMRFp4XuwxzVufjKvN3BE8xtYAEjNC3Tgxat2Tpc3XJZqnPnoBAOpcruB4qp0sCEcqxtq2IjiCMYFqKZ1zpCS9IjTJ7YYmCa_zc9SoZjTGoCEwqv7_xSk71JZXd-AubRaRx7TGFDhKOzCAM5BR9IazlhbBNWXxJ6Dj6t7P0ircPmkeinJMDM-Cxo4HtwHs7wOhsh9435rNbCch-79HaHauXqOTe2UThGbJth8XfjSQHvlOSR67nALNp_1Ueydy1bMtTRNtTBW3jdLH_SV)

(2) **Restart**. Set up a method and aplly it to foster system nature (purpose), architecture, and dynamics.

**To be done**
- [ ] Add attribute 'concept' to Discourse class
- [ ] Simplify document IDs and consolidate content
- [ ] Analyze and interpret BoellCezez-2015
- [ ] Include also: Okoli, C. (2015). A Guide to Conducting a Standalone Systematic Literature Review. Communications of the Association for Information Systems, 37, pp-pp. https://doi.org/10.17705/1CAIS.03743 (`Okoli_Chitu_2015.pdf`)
