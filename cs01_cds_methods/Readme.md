# Case Study : Critical Data Studies' Methods
🚧 Status: Under construction! 🚧 
## Clarify Purpose
The purpose of this study is to analyse examples of critical data studies (CDS) featuring various methods (Kitchin 2021b) and design a concept of some CDS for further implementation.

The AREA Method (Einhorn 2017) helps me bring greater **CARE** to making smarter, better decisions:
- Craft critical concepts
- Address biases
- Reveal perspectives
- Extract learning

![Case study mind map](https://www.plantuml.com/plantuml/png/FP11JiCm44NtEOLNg2XBBj2IIgYBqAgmpCRKGseH_uayOq4a3i_WG7UM__FyDzwA-goVRzAqhlD2xaLBM5mV4LplvwPjtPv48xn6ne2duzxkZ6KeVUc0pQE_V8oP2yBzNv9IGTJ5icwA1FtkYYWdoly0BZJNSKPShNvDt9bziCu1hxjZ9NVmqoBHt5QDEA8U3scUA16qIlq-FMKUCuaCU3XLf6TJu1mntZgd8aORiZd0HbtLtRbdsy5MfdbLEzCxPJ8zQRQ4OD_o0m00)
(Source: WorkFlowy LS_2011)

## Collect Elements
- [Journal](cs01_journal.md) tracks the research journey of this case study including effort
- Knowledge Base holds the Term-Association ontology (TAO) inluding instances
  - `tao_iim.py`: a module for loading, adding and dumping data to the knowledge base
  - `elem.txt`, `rels.csv`, `relt.csv`: the knowledge base (editable)
  - `batches_RRRRMMDD.txt`: a set of triples added to the baseline
- Notebooks IPYNB document the workflow
  - 20211130_Build_knowledge_base: used for populating a knowledge base with references from Kitchin (2021b)
- Deliverables indicate the progress
  - [Critical Data Studies Methods Instantiated](CDS_methods_instantiated.md) (done 2021-11-30)

## Compose Relationships
The initial concept model of TAO-IIM for this case study includes four concepts:

![Initial Ontology](https://www.plantuml.com/plantuml/png/FP2nJWCn38RtF8ML2Kxg6o3KjGDGiNIv9JcRdgMhKpcEKDyUNmWCrdy-V_fivLWjgRNR5fQa2F4aHYfay5wGPc6H2Ac2Pv1Y1ChNrGBx7oGn_c92o0y8IU1qXeIeL6iWGTZn8RrGXa-gfUdYpgPRTtgE-RdbZPTaN6IMU_uTUuxn6zbQS9Qd3xrUajBpB4M_E-GP0ej0VCclQwbMu-4GkSB-tK-BVOzNH-YM2pBzKQD5O8bzeHV4QLhOg4xJeBmRge4CrNqhZtzJxuPfl-f8WlwiFm00)

## Conduct Pre-Mortem
**2021-11-30**: I need a clear structure for this study, otherwise I get lost. After a couple of first fsp spent on the study I can set a time limit. This is a part of my one-sided contract for this artwork.

----

IPYNB Template
```
{
 "nbformat": 4,
 "nbformat_minor": 5,
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "cells": [
 ]
}
```
