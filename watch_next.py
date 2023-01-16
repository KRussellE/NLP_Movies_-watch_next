import spacy    # import spacy from the Library

nlp = spacy.load('en_core_web_md')  # Return a Language object containing all components and data needed to process text.

def next_movie(description):    # open file
    movies = open("movies.txt", "r") 
    split_list = []
    for i in movies:    
        split_list.append(i.split(':')) # split movies into title and description and store in a list
    count = len(split_list) 
    similarity_list = []    # a list called similarity_list to store similarity values
    
    model_sentence = nlp(description)  
    for i in range(0, count):   # iterate as many times as the number of movies in the text file
        similarity_list.append(nlp(split_list[i][1]).similarity(model_sentence))    # check similarity between the movie description with the recently watched movie description
    print("\u001b[32mSimilarity with other movies: \u001b[37m")
    for item in similarity_list:
        print(item, end=" ")    # print out the similarities between the movies and the watched movie
    max_similarity = max(similarity_list)   # get the maximum similarity value
    max_similarity_index = similarity_list.index(max_similarity)    # get index of highest similarity value
    return split_list[max_similarity_index][0]  # return movie title similar to watched movie

# movie description to comapare with
doc=("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator")

print("\n\n\u001b[32mBased on the maximum similarity \n\tNext Movie Recommended to Watch: \u001b[33m" + next_movie(doc) + "\n")   # call function that gets the next movie description that is similar to the watched movie