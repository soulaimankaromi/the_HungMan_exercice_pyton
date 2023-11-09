algorithme     candid
fonction   mot(y:chain de caractere):boleen
variable
i : entier
p,r:boleen
debut
        si      4 =< langueur(y) =< 25 alors 
                  p <-- vrai 
         sinon 
                  p <-- faux
         fin si
pour i <-- 0 a langueur (y)-1 pas 1 faire
       si    ascii(y[i]) =<65  ou ascii(y[i]) >= 90 alors 
                 r <-- faux
        fin si
fin pour       
       si p =faux ou r = faux alors 
              returne faux 
       sinon
              returne vrai
fin
fonction  test (c:caractere , y: chain de caractere):boleen
variable 
i : entier 
p : boleen
debut
a <-- 0
pour i <-- 0 a longueur(y)-1 pas 1 faire
          si c = y[i] alors 
              p <-- vria
               a <-- a+1
         sinon
                p <-- faux
         fin si
fin pour 
        si p = vria alors
            returne vria
         sinon
            returne faux
fin
variable
i,j,k : entier
A : caracter
M : chain de caractere
p:boleen
tableau T () :chain de caractere
debut
repeter 
ecrire("tapez le mot :")
lire (M)
jusqu a  mot (M) = vrai
pour i <-- 0 a longueur(M)-1 pas 1 faire
           T.ajoute(*)
fin pour
j <-- 0
k <-- 0
repeter
ecreri("tapez le caracter :")
lire(A)
pour i <-- 0 a longueur(M)-1 pas 1 faire
si A = m[i] alors 
t[i] <-- m[i]
j <-- j+1
finsi
p <-- test(A,M)
si p = faux alors
k <-- k+1
finsi
jusqu a  j = longueur(M) ou k = 5
si k =5 alors 
ecrire("Tu es un gagnant")
sinon
ecrire("tu es perdant")
fin
