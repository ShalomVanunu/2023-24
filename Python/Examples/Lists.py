def movie_info(bool, lst):
   new = ""
   if bool:
     for key in lst:
         new += key +": " + ", ".join(sorted(lst[key])) + "\n"
     return new

   else:
       for key in lst:
           new += key + ": " + ", ".join(lst[key]) + "\n"
       return new

def main():
    lst = {"choclate" : ["aa", "cc","ee",'zz', 'bb'], "milk" : ['rr','tt','bb','uu']}
    print(movie_info(False, lst))


if __name__ == "__main__":
    main()



