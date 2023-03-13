from pathlib import Path
import argparse
from flask import Flask, render_template, request
from utils import load_wapo
from inverted_index import build_inverted_index, query_inverted_index
from mongo_db import db, insert_docs, query_doc

app = Flask(__name__)

data_dir = Path(__file__).parent.joinpath("pa3_data")
wapo_path = data_dir.joinpath("test_corpus.jl")
#wapo_path = data_dir.joinpath("wapo_100.jl")

global_matched = [] # stores the matched doc output of query_doc()
query_text = '' # stores the query text 
doc_num = 0 # stores the number of matched doc

if not 'wapo_docs' in db.list_collection_names():
    # if wapo_docs collection is not existed, create a new one and insert docs into it
    insert_docs(load_wapo(wapo_path))


# home page
@app.route("/")
def home():
    return render_template("home.html")


# result page
@app.route("/results", methods=["POST"])
def results():
    # TODO:
    global global_matched, query_text, doc_num

    query_text = request.form["query"]  # Get the raw user query from home page
    matched_id_list, stopword_list, unknown_list = query_inverted_index(query_text)

    # retrieve doc content_str given matched_id_list
    global_matched = [query_doc(id) for id in matched_id_list]
    doc_num = len(matched_id_list)

    # prepping the first 8 doc to display on page 0
    page_count = 0
    first_matches = global_matched[page_count: page_count+8]
    global_matched = global_matched[8:]

    # only set page_flag to True if there are more than 8 matched documents
    page_flag = False
    if doc_num-8 > 1:
        page_flag = True

    return render_template("results.html", 
                           docs=first_matches,
                           doc_num=doc_num, 
                           query_text=query_text, 
                           page_count=page_count, 
                           page_flag=page_flag,
                           stopwords=stopword_list,
                           unknowns=unknown_list)


# "next page" to show more results
@app.route("/results/<int:page_id>", methods=["POST"])
def next_page(page_id):
    # TODO:
    global global_matched, query_text, doc_num

    # increment page_id to display in route /results/<int:page_id>
    page_id += 1 
    # prepare first 8 entries of the remaining documents for rendering
    first_matches = global_matched[:8]

    # only set page_flag to True if more than 8 matched documents are left
    page_flag = False 
    if len(global_matched)>8:
        page_flag = True

    # remove first 8 documents from global_matched
    global_matched = global_matched[8:]

    print('query text pages', query_text)

    # pass arguments to render_template()
    return render_template("results.html",
                           query_text=query_text,
                           doc_num=doc_num, 
                           docs=first_matches,
                           page_count=page_id,
                           page_flag=page_flag)  # add variables as you wish


# document page
@app.route("/doc_data/<int:doc_id>")
def doc_data(doc_id):
    # TODO:
    # use doc_id key to get document value from wapo_docs
    item = query_doc(doc_id)
    return render_template("doc.html", item=item)  # add variables as you wish


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Boolean IR system")
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--run", action="store_true")
    args = parser.parse_args()

    
    if args.build:
        build_inverted_index(load_wapo(wapo_path))
    if args.run:
        print('flag --run')
        app.run(debug=True, port=5000)