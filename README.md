## TD 12

Amaury GIMONNET  
David ELBAR  
Aram TOSBATH  
Esteban OUVRE  

## Tri à Bulle (Bubble sort)

C'est un algorithme de tri qui fait des itérations sur une liste. Il compare d'abord les 2 premiers éléments de la liste :
- si le 1er élément est plus grand que le 2ème, il les échange de place
- sinon, les 2 éléments restent à leur place

Il compare alors les 2 prochains éléments, et ainsi de suite jusqu'à ce que les nombres les plus grands finissent en fin liste et les nombres plus petits restent en début de liste.

## Tri par sélection (selection_sort)

Pour cet algorithme, on parcourt la liste à la recherche du plus petit élément et on le change de place avec le 1er élément de la liste.  
Maintenant que le 1er élément est trié, on parcourt le reste de la liste à la recherche du plus petit élément afin de le changer de place avec le 2ème élément de la liste, et ainsi de suite ...

## Tri par insertion (insertion_sort)

On suppose que le 1er élément est trié et on passe à l'élément suivant. Si celui-ci est plus grand que le 1er, on le laisse tel quel, mais s'il est plus petit, on copie la valeur du 1er élément dans la 2ème position et on défini le 1er élément par la valeur du 2ème etc...

## Tri fusion (merge_sort)

On divise la liste en 2 listes, puis on continue de diviser chaque liste en 2 jusqu'à ce que chaque liste soient composé d'un seul élément.  
On tri alors chaque liste en comparant les plus petites valeurs, avant de les fusionner ensemble et finalement obtenir la liste triée.

## Tri rapide (quick_sort)

Pour cette méthode, on choisit une valeur qui va être le "pivot". Ensuite, les valeurs plus petites que le pivot sont déplacées vers la gauche et les valeurs plus grandes sont déplacées vers la droite.

## Tri shell (shell_sort)



## Tri peigne (comb_sort)

