import pandas as pd
import json

df = pd.read_csv('/Users/caleb/git/big_data_project2/ml-latest-small/movies.csv')
genre_df = df['genres'].apply(lambda x: x.split("|"))

############################ FUNCTIONS ########################################
def query_genre():
    wanted_genre = 'NULL'

    uniques = []
    for x in genre_df:
        if x:
            for y in x:
                if y.lower() not in uniques:
                    uniques.append(y.lower())

    print("________________________***GENRES***_______________________________")
    i = 0
    next = 2
    for x in range(len(uniques)):
        if next+2 <= len(uniques):
            if(not i):
                print("{:30s} {:2s}".format(str(uniques[i]) , str(uniques[i+1])))
            else:
                print("{:30s} {:2s}".format(str(uniques[next]) , str(uniques[next+1])))
                next+=2
        i+=1

    print("________________________***GENRES***_______________________________\n")

    while(wanted_genre.lower() not in uniques):
        wanted_genre = input('What genre do you feel like watching? ')
        if wanted_genre not in uniques:
            print("Please Try Again...\n")

    suggestions = []

    result = df[df['genres'].str.contains(wanted_genre, case=False, na=False)]

    if result.empty:
        print("No results for " + wanted_genre)
        return False
    else:
        print("_________________**RECOMMENDATIONS**___________________________")

        i = 0
        next = 2
        for x in range(len(result['title'].values)):
            if next+2 <= len(result['title'].values):
                if(not i):
                    text1 = (result['title'].values[i][:75] + '..') if len(result['title'].values[i]) > 75 else result['title'].values[i]
                    text2 = (result['title'].values[i+1][:75] + '..') if len(result['title'].values[i+1]) > 75 else result['title'].values[i+1]
                    print("{:80s} {:5s}".format(text1 , text2))
                else:
                    text1 = (result['title'].values[next][:75] + '..') if len(result['title'].values[next]) > 75 else result['title'].values[next]
                    text2 = (result['title'].values[next+1][:75] + '..') if len(result['title'].values[next+1]) > 75 else result['title'].values[next+1]
                    print("{:80s} {:5s}".format(text1 , text2))
                    next+=2
            i+=1

        print("_________________**RECOMMENDATIONS**___________________________\n")
        print()

    return True
###############################################################################
if __name__ == "__main__":
    flag = False

    print("\n\t\t\tWelcome to the Recommender System 6000!\n")
    print("What are you looking for today?\n")
    print("1: Genres, 2: Authors, 3: Popularity, 4: ")

    while(not flag):
        if(query_genre()):
            flag = True
