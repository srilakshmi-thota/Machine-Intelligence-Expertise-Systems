# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 02:34:44 2019

@author: tinku
"""
import random

class Individual(object): 
    
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 
        
  
    @classmethod
    def mutated_genes(self): 
        global geneset
        gene = random.choice(geneset) 
        return gene 
  
    @classmethod
    def create_chromosome(self): 
        global target
        return [self.mutated_genes() for _ in range(len(target))] 
  
    def mate(self, parent2): 
        offspring = [] 
        for gp1, gp2 in zip(self.chromosome, parent2.chromosome):     
            prob = random.random() 
            if prob < 0.45: 
                offspring.append(gp1) 
            elif prob < 0.90: 
                offspring.append(gp2) 
            else: 
                offspring.append(self.mutated_genes()) 
        return Individual(offspring) 
  
    def cal_fitness(self):  
        global target
        fitness = 0
        for g1, g2 in zip(self.chromosome, target): 
            if g1 == g2: fitness+= 1
        return fitness 
    
    
generation = 1  
found = False
population = []
geneset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"
target="Arise awake and stop not"
population_size=100
for i in range(population_size):
    chromosome = Individual.create_chromosome()
    population.append(Individual(chromosome))
while not found:
    population=sorted(population, key = lambda x:x.fitness,reverse=True)
    if population[0].fitness == len(target):
        found=True
        break;
    new_generation=[]
    s = int((10*population_size)/100) 
    new_generation.extend(population[:s]) 
    s = int((90*population_size)/100) 
    for i in range(s): 
        parent1 = random.choice(population[:50]) 
        parent2 = random.choice(population[:50]) 
        child = parent1.mate(parent2) 
        new_generation.append(child) 
        
        population = new_generation 
        print("Generation: ",generation,"\tString: ","".join(population[0].chromosome),"\tFitness: ",population[0].fitness) 
        generation += 1

print("Generation: ",generation,"\tString: ","".join(population[0].chromosome),"\tFitness: ",population[0].fitness) 
    
