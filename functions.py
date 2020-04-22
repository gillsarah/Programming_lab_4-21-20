'''
First, some imprecise definitions (look up for the real defs, but these work for our purposes)
Function: A focused grouping of code that is easily reusable
Functional programming: The result of a function is limited to its output,
and is exactly determined by the arguments given as inputs
Global variable: A variable that is defined at the top level of the program, and is accessible everywhere
Local variable: A variable that is defined inside of a function, and is only available in that function.
'''

#Optional Task:
#Re-factor your code from HW1
#bundle everything into function! Name the functions descriptively. Call the functions
#try calling the function in a for loop
#if you don't have any questions, we can talk about this durring the Q&A breakout sessions

#####
#Functions:
#####

#here's one
def multiply_odds_by_2_evens_by_3(list_of_num):
    '''
    Descriptive title says it all: multiplies the odds by 2 and the evens by 3
    Inputs: a list of integers 
    Outputs: a list of integers 
    There are computer science rules about this comment chunk, that I am not following.
    However, I do like to have a little description in more complicated code that helps
    me know what it does (if it is not supper obvious (like this one is))
    '''
    rv = []
    for number in list_of_num:
        if number % 2 == 0: #even
            rv.append(number * 3)
        else:
            rv.append(number * 2)
    return rv

list1 = [1, 2, 3]
multiply_odds_by_2_evens_by_3(list1)

#why have a return statement? 
#Because now I can use the returned list and do more stuff to it
new_list = multiply_odds_by_2_evens_by_3(list1)

multiply_odds_by_2_evens_by_3(new_list)


def my_new_func():
    '''
    reads variables from the global namespace, not a best practice
    input is a list of ints
    output is a list of ints (each haveing been mult by 2)
    '''
    return[x*2 for x in new_list]
my_new_func()

#better:
def my_new_new_func(my_list):
    '''
    now it uses local variables
    input is a list of numbers
    output is a list of numbers (each having been mult by 2)
    '''
    return[x*2 for x in my_list]
#this will throw an error:
my_new_new_func()
#I didn't tell it what to take in, and now my function has args (well, one arg)

#this will also thow an error:
my_new_new_func(my_list)
#my_list doesn't exist outside of the function

#the real fucntion call:
my_new_new_func(new_list)



#Argument and Keyward Arguments:

def say_hello(name, grade = 'I am a first year MPP'):
    '''
    takes in a string for name 
    optional to change grade
    '''
    statement = 'Hello, my name is '+ name + ' and ' + grade
    print(statement)

say_hello('Jose') 

say_hello('Will', grade = 'I am a second year MAIDP')


say_hello('Bill', 'I am a second year MPP') #risky, better to be explicit like above, but it works

#I'm repeating myself, let's make this a little bit more automated
def say_hello(name, grade = 'first', program = 'MPP'):
    '''
    takes in a string for name 
    optional to change grade and program 
    '''
    statement = 'Hello, my name is '+ name + ' and I am a ' + grade + ' year '+ program
    print(statement)

#this is the same, but I have to do a little bit less typing in the fn call, so that's nice
say_hello('Will', grade = 'second', program= 'MAIDP')
#and I can still call it the simple way:
say_hello('Jose')

#call
some_people = [('Jose', 'first', 'MPP'), ('Will', 'second', 'MAIDP')]
for n, y, p in some_people:
    say_hello(name=n, grade=y, program=p)



#####
#generators -good for saveing memory
#####
def my_gen(stop):
    v = -1
    while  v <= stop: #to get only a fixed number (in general, make sure your while loops don't go forever)
        v += 1
        yield v  #yield is a the "return" for generators

generator = my_gen(100) #create an instance of the generator, get at most 100
next(generator) #next is a built in fn. calls generator one more time each time I call next 

def my_count(stop):
    v = -1
    while  v <= stop: #to get only a fixed number (in general, make sure your while loops don't go forever)
        v += 1
        return v 

my_count(10)


#####
#lambdas -anonymous functions
#####
#useful for woring with dataframes

#import pandas, you'll learn about pandas soon!
import pandas as pd #you should put import statements at the top of your code (not like this)

#makeing a toy df to play with
my_df =pd.DataFrame()
my_df['col1'] = [1,0,2,3]
my_df['col2'] = [5,5,6,7]
my_df['col3'] = [4,5,3,6]

#make everything in it into a string (yes I could have done this when I made the df)
my_df = my_df.applymap(str) 

#apply the string comprehension str.zfill to each element in colum 3
my_df['col3'] = my_df['col3'].apply(lambda x: x.zfill(3)) 

my_df

#not a great fn, but this does show you how you can bundle things easily
def parse_df(df):
    '''
    takes a df of numbers with colum names col1 and col3
    output is a df that I can use in x_func later
    '''
    str_df = df.applymap(str) 
    str_df['col3'] = str_df['col3'].apply(lambda x: x.zfill(3)) 
    str_df['col1'] = str_df['col1'].apply(lambda x: x.zfill(2)) 
    str_df['col4'] = str_df['col1'] + str_df['col3']
    return str_df


new_df = parse_df(my_df)
new_df

def x_func(a_serise):
    for i in a_serise:
        print(i)

x_func(new_df['col4'])

#or call the function in the other function:

def y_func(df):
    temp_df = parse_df(df)
    for i in temp_df['col4']:
        print(i)

y_func(my_df)

