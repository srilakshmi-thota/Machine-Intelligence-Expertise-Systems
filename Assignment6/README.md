__Libraries used:__\
random : to generate the random probability and to randomly choose the gene from geneset

__Input:__\
Target String : Arise awake and stop not\
geneset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"\
population size=100

__Output:__\
Genetic algo fittest chromosome close to the target string after each iteration along with it's fitness value

__User-defined functions:__\
__Class :__ Individual(object) - class representing an individual chromosome in the population\
1.__init__(self , chromosome)\
Initialises the valuesand creates an chromosome object and also calculates the fitness value of it and assigns to it

__2.mutated_genes(self)__
Randomly chooses a gene from the geneset and return the gene

__3.create_chromosome(self)__\
Creates chromosome-string of genes

__4.mate(self,parent2)__\
Performs mating and returns the new offspring by below steps:\
-Selects a random probability P\
-If P<0.45 inserts the gene from self i.e parent1\
-else If P<0.90 inserts the gene from parent2\
-else insert random gene by mutate for maintaining diversity

__5.cal_fitness(self)__\
Calculates the fitness of the chromosome by counting the number of characters which matches the characters in target string at a particular index and return the fitness value



Initialises the population size=100 and the generation1 and creates the next generation according to given rules in each iteration till the target string is found in the form of fittest chromosome of the population
__Rules:__\
10% of fittest population goes to the next generation\
From 50% of population, Individuals will mate to produce offspring -calls the mate function










