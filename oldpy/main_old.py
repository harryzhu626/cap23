from oldpy.tweettodb import tweettodb_main
from oldpy.opinionminer import retrieve_tweets, extract_content

if __name__ == '__main__':
    #tweettodb_main()
    cursor = retrieve_tweets()
    for item in cursor:
        extract_content(item)
    # sentence = ['this character design does not make any sense!','jean is the best character!']
    # print(analyze_opinion(sentence))