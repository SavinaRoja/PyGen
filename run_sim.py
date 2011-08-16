#! /usr/bin/python

import argparse
import sys

from Flower import Flower #Code for a flower, in Flower.py
from random import randint #A method for creating random integers

def run_sim(pop_size, max_fit, selection, runs = 1, output = sys.stdout, style = 'verbose'):
    for run in range(runs):
        population = [] #Create a list to hold the elements of the population
        for i in range(pop_size): #Fill the list with flowers
            population.append(Flower())

        generation = 0
        maxreached = False
        while not maxreached:
            #Sort the population by individual fitness
            population.sort(reverse = True, key = lambda Flower: Flower.fitness)
            
            mostfit = population[:int(pop_size / selection)]
            if style == 'verbose':
                output.write('GENERATION {0} - Top Fitness: {1}\n'.format(generation, 
                                                                          mostfit[0].fitness))
            elif style == 'csv':
                pass
            
            if mostfit[0].fitness >= max_fit: #Check for threshold fitness
                maxreached = True #Escape the while loop conditions to end the program
                if style == 'verbose':
                    output.write('Maximum Fitness Achieved!\n')
                elif style == 'csv':
                    output.write(str(generation))
                    output.write(',')

            
            if not maxreached:
                population = [] #Empty the population list to start over
                for i in range(pop_size): #Re-populate from the most fit flowers
                    #Randomly pick two parents from the most fit population
                    firstparent = mostfit[randint(0,len(mostfit)-1)]
                    secondparent = mostfit[randint(0,len(mostfit)-1)]
                    
                    #Mate the two parents to create a child flower for the next generation
                    population.append(firstparent.mate(secondparent))
                
                generation += 1 #Increase the generation counter by one
                
        if not run % 1000:
            output.write('\n')

def main():
    '''do stuff'''
    parser = argparse.ArgumentParser(description = 'PyGen Parser')
    parser.add_argument('-b', '--batch', action ='store', type = int, default = 0,
                        help = 'Run a number of iterations of the simulation')
    parser.add_argument('-p', '--popsize', action ='store', type = int, default = 64,
                        help = 'Set the population size')
    parser.add_argument('-f', '--fitness', action ='store', type = int, default = 32,
                        help = 'Set the fitness goal')
    parser.add_argument('-s', '--selection', action = 'store', type = float, default = 2,
                        help = 'Set the population size divisor for selection')
    parser.add_argument('-o', '--output', action = 'store',
                        help = 'Choose filename for CSV output. Or enter "stdout".')
    args = parser.parse_args()
    
    RUNS = args.batch #Number of runs to use for batch mode
    POPSIZE = args.popsize #The size of the flower population
    MAXFIT = args.fitness #Set the fitness threshold
    SELECTION = args.selection #Selection stringency factor
    
    if not args.output:
        if RUNS:
            args.output = 'batch_output.csv'
        else:
            args.output = 'stdout'
    
    if args.output == 'stdout':
        run_sim(RUNS, POPSIZE, MAXFIT, SELECTION, sys.stdout)
    elif args.output[-4:] == '.csv':
        with open(args.output, 'w') as outfile:
            run_sim(RUNS, POPSIZE, MAXFIT, SELECTION, outfile)
    else:
        with open(args.output + '.csv', 'w') as outfile:
            run_sim(RUNS, POPSIZE, MAXFIT, SELECTION, outfile)

if __name__ == '__main__':
    main()