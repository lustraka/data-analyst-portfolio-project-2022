# -*- coding: utf-8 -*-
"""Routines for Internal Information Management with Term - Association Ontology
"""

# Import dependencies
import requests
import pandas as pd
import numpy as np
import re
from datetime import date
import json
import os

def load_elem_rel():
  """Load elements and relatioships from storage or initialize empty dataframes."""

  if os.path.isfile('elem.txt'):
    # Read json object from file
    elem = []
    with open('elem.txt', 'r') as file:
      line = file.readline()
      while line:
        elem.append(json.loads(line))
        line = file.readline()
    elem_df = pd.DataFrame(elem)
  else:
    # Create an empty dataframe
    elem_df = pd.DataFrame(columns=['term', 'note'])
  
  if os.path.isfile('rels.csv'):
    # Load relations
    rels_df = pd.read_csv('rels.csv')
  else:
    # Create an empty dataframe
    rels_df = pd.DataFrame(columns=['elea', 'relt', 'eleb'])
  
  if os.path.isfile('relt.csv'):
    # Load relationship types
    relt_df = pd.read_csv('relt.csv')
  else:
    # Create an empty dataframe
    relt_df = pd.DataFrame(columns=['term', 'inverse'])

  print('Shapes of loaded files: ', [df.shape for df in [elem_df, rels_df, relt_df]])
  
  return elem_df, rels_df, relt_df

def add_batch(batch, elem_df, rels_df, relt_df):
  """Adds a triple batch to triple tables`
  
  Params:
    batch with a structure [elea, relt, [eleb]]
    elem_df, rels_df, relt_df
  
  Returns:
    updated elem_df, rels_df, relt_df"""

  def add_term(df, term):
    """Add an term to a dataframe"""

    rec = df.loc[df.term == term]

    if rec.shape[0] == 0:
      # Add the term to a dataframe
      return df.append(pd.DataFrame({'term':[term]}), ignore_index=True)
    elif rec.shape[0] == 1:
      return df
    else:
      print(f'Duplicated records for element \"{term}\" identified!')
      return df

  def add_triple(rels, elea, relt, eleb):
    """Add a triple to a rels dataframe"""

    triple = rels.query(f"elea == \'{elea}\' and relt == \'{relt}\' and eleb == \'{eleb}\'")

    if triple.shape[0] == 0:
      # Add a relatinship to a dataframe
      return rels.append(pd.DataFrame(
          {'elea':[elea], 'relt': [relt], 'eleb':[eleb]}), 
          ignore_index=True)
    elif triple.shape[0] == 1:
      return rels
    else:
      print(f'Duplicated relationship \"{elea}\" | \"{relt}\" | \"{eleb}\" identified!')
      return rels
  
  # Make copies of dataframes
  elem_df = elem_df.copy()
  rels_df = rels_df.copy()
  relt_df = relt_df.copy()

  # print('Starting with:', [df.shape for df in [elem_df, rels_df, relt_df]])

  # Add elements
  for e in [batch[0]]+batch[2]:
    elem_df = add_term(elem_df, e)
  
  # Add a relationship type
  relt_df = add_term(relt_df, batch[1])

  # Add relationships
  for b in batch[2]:
    rels_df = add_triple(rels_df, batch[0], batch[1], b)
  
  # print('Ending with:  ', [df.shape for df in [elem_df, rels_df, relt_df]])
  print(f"A batch for {batch[0]} processed.")

  return elem_df, rels_df, relt_df

def dump_elem_rel(elem_df, rels_df, relt_df):
  """Save dataframes as txt or csv on local storage"""

  # Store elem_df as a text file with row in json format
  with open('elem.txt', 'w') as file:
    for _, row in elem_df.sort_values(by='term').iterrows():
      file.write(json.dumps(row.to_dict(), ensure_ascii=False)+'\n')
  
  # Store other dataframes as CSV
  rels_df.to_csv('rels.csv', index=False)
  relt_df.to_csv('relt.csv', index=False)

  print('Don\'t forget to download results for further use!!')
  return

