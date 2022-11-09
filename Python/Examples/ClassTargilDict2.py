
def write_movie_info(tr_fa, dicti):
    keys = list(dicti.keys())  # ["Chocolat","Skyfall"]
    values = list(dicti.values())
    if tr_fa:
        for index in range(len(keys)):
            print(keys[index]+":"+",".join(sorted(values[index])))
    else:
        for index in range(len(keys)):
            print(keys[index]+":"+",".join(values[index]))



def main():
    dicti ={"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],"Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
    write_movie_info(True, dicti)




if __name__ == "__main__" :
    main()
