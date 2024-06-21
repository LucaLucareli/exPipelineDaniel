from scipy.stats import binom, poisson

#Questão 1
n = 30000
p = 1/10000
k = 1

prob = binom.pmf(k, n, p)

print(prob)

λ = 3
k = 1

prob = poisson.pmf(k,λ)

print(prob)

#Questão 2
n = 100
p = 0.01/100
k = 0

prob_germina_app = binom.pmf(k, n, p)

print(prob_germina_app)

n = 100
p = 99.99/100
k = 100

prob_germina_app = binom.pmf(k, n, p)

print(prob_germina_app)

#Questão 3
λ = 2
k = 0

prob_com_mudanca = poisson.pmf(k,λ)

print(prob_com_mudanca)

λ = 4
k = 0

prob_sem_mudanca = poisson.pmf(k,λ)

print(prob_sem_mudanca)

mudanca = prob_com_mudanca - prob_sem_mudanca

print("Mudança de ",round(mudanca*100,2),'%')



