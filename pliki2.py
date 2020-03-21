import csv
import statistics

data= []

with open("przykladowy.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        data.append (
            {
                "year": int(row["Year"]),
            "score":int(row["Score"]),
            "title": row["Title"]
            }
        )
        # print(row['Year'], row['Score'],row['Title'])
        # print(data [0] ["score"])
        # print(data [0] ["title"])


        

        



# tytuł najgorszego filmu
# tytuły kilku najgorszych filmów
# tytuł najl filmu
# tytuły kilku najl filmów
# srednia ocen filmow
# mediana ocen filmo
# znajdz rok w ktorych wydal najwiecej filmow
        # najgorszy film
        # najlepszy film
        # średnia ocen filmów
        # mediana

    #    worst_score=100


    # tworzymy zmienne przechowujące chwilowo wynik
        worst_score= data [0] ["score"]
        worst_film = data [0] ["title"]
        mediana_list=[]
        movie_list=[]
      
        
        for entry in data:
            if entry ["score"] < worst_score:
                worst_score = entry["score"]
                worst_film = entry["title"]
               

                

                
    print (f'The worst movie score is {worst_score} and title is {worst_film}')

#    szukamy najlepszego filmu
    best_film = data [0] ["title"]

    for entry in data:
        if entry ["score"] > worst_score:
            worst_score = entry["score"]
            best_film = entry["title"]

                
    print (f'Best film is {best_film}')

# szukamy mediany dla listy filmow

    for entry in data:
        worst_score = entry["score"]
        mediana_list.append(worst_score)
        

    # print(sorted(mediana_list))

    list_lng=len(mediana_list)
    sort_list=sorted(mediana_list)

    print(list_lng )

    if list_lng%2==0: 

        mediana_tot = ( sort_list [int((list_lng-1)/2)] + sort_list[int( (list_lng+1)/2 )] )/2

    else:
        mediana_tot = sort_list[int((list_lng-1)/2)] 


print (f'Score mediana is {mediana_tot}')
       
# print (statistics.median(mediana_list))



sum_score=0
leng_list=0

for entry in data:
    worst_score = entry["score"]
    sum_score+=worst_score
    leng_list+=1


print (f'Avarage is {sum_score/leng_list}')



# for entry in data:
#     worst_score = entry["score"]
#     worst_film = entry["title"]
#     print (f'The movie is {sorted(worst_score)} and title is {worst_film}')



movie_score=[]
movie_list=[]
for entry in data:
        table_score = entry["score"]
        movie_score.append(table_score)
        table_movie= entry["title"]
        movie_list.append(table_movie)


movie_dict = {} 
for key in movie_score: 
    for value in movie_list: 
        movie_dict[key] = value 
        movie_list.remove(value) 
        break 

# print("Resultant dictionary is : " +  str(movie_dict))

  
# for i in sorted (movie_dict.keys()) :  
#      print(i, movie_dict[i], end = " \n" ) 


# print(len(sorted (movie_dict.keys())))     

movie_count = len(sorted (movie_dict.keys()))
n=movie_count-5


print('''
=========================
The five worst movies:''')

for x in list(sorted (movie_dict.keys()))[0:5]:
    print (x, movie_dict[x])
    

print('''
=========================
The five best movies:''')

for x in list(reversed (sorted (movie_dict.keys())))[0:5]:
    print (x, movie_dict[x])    

    
    



