from transformers import pipeline 

pipe = pipeline('text-classification')

def opinion_mine_single(submission_clean):
    opinion = pipe(submission_clean)
    return opinion


def opinion_mine_multi(submissions_clean):
    for submission in submissions_clean:
        yield opinion_mine_single(submission)