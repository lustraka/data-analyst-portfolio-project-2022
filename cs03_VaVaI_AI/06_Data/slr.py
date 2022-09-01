"""Code for systematic literature reviews"""

# Import Dependencies
import pandas as pd
import textwrap # ensures more readable text rendering in ipynb, html, as well as pdf


def print_paper_info(df, paper):
    """Print authors, year, title, abstract, and keywords of a paper."""
    
    rec = df.loc[df.id == paper].copy()
    if len(rec) < 1:
        print('No paper with id = ', paper)
        return 
    elif len(rec) > 1:
        print('Duplicated records for id = ',paper)
        return 
    else:
        print(rec.id.values[0])
        print(f"Authors: {rec.authors.values[0]}")
        for line in textwrap.wrap("Title: "+rec.title.values[0], width=80):
            print(line)
        print('Abstract:')
        for line in textwrap.wrap(rec.abstract.values[0], width=80):
            print(line)
        print('Keywords:')
        if rec.kws.values[0] == 'kws':
            print('no data')
        else:
            for line in textwrap.wrap(rec.kws.values[0], width=80):
                print(line)
    print('='*80, '\n')

    return

# Use this function in another module
# for paper in dw['papers'].id.values:
#     slr.print_paper_info(dw['papers'], paper)

def id_to_filename(id):
    """Converts paper's id into a string for filename."""
    
    file_name = id
    for char in [',', '.', '&', '(', ')']:
        file_name = file_name.replace(char,'')
    return file_name.replace(' ','_').replace('__','_')

def export_papers_to_md_table(df):
    """Prints records of papers as markdown tables."""

    for idx, row in df.iterrows():
        print(f"\n \n")
        print(f"({str(idx+1)}) aspect|value\n-|-")
        print(f"id|**{row['id']}** [{id_to_filename(row['id'])}]")
        print(f"authors|{row['authors'].replace('|',';')}")
        print(f"title|[{row['title']}]({row['url']})")
        print(f"abstract|{row['abstract']}")
        print(f"kws|{row['kws'].replace('|', '; ')}")
        print(f"doi|{row['doi']}")
        print(f"pub_details|{row['pub_details']}")
        print(f"note|{row['note'].replace('|','; ')}")
        

    return
