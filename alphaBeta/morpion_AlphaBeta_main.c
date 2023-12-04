#include <stdlib.h>
#include <stdio.h>

//ne pas oublier a faire a la fin du programme
void liberation(int **tab){
    for (int i = 0; i < 3; i++)
    {
        free(tab[i]);
    }
    free(tab);
}

void viderBuffer(){
  char char_saisie; //le caracère courant dans le buffer
  scanf("%c", &char_saisie);
  while (char_saisie!='\n') {
    scanf("%c", &char_saisie);
  }
}


void affichage(int ** tab, int taille){
    //deux boucle "pour" pour parcourire la matrice
    for (int i = 0; i < taille; i++)
    {
        for (int k = 0; k < taille; k++)
        {
            printf("--");//purement décoratif
        }
        printf("\n");
        for (int j = 0; j < taille; j++)
        {
            printf("%c|",tab[i][j]);
        }
        printf("\n");
    }
    
}

int ** createtab(int taille){
    int **tab; // tableau qui sera renvoyer
    tab = malloc(taille*sizeof(int*));//allocation de la ligne
    for (int i = 0; i < taille; i++)
    {
        tab[i] = malloc(taille*sizeof(int));//allocation des colonnes
        
        for (int j = 0; j < taille; j++)
        {
            tab[i][j]=' ';//on enregistre un vide pour chaque case
        }
    }
    return tab;
}

//fonction qui renvoi, un int, la saisie du joueur
int saisie(){
  int int_nbrSaisi; //le nombre qui sera saisie
  //verification s'il y a une erreur
  while (!scanf("%d", &int_nbrSaisi)) {
    viderBuffer(); // on oublie pas de vider le buffer pour ne pas avoir de boucle infini
    printf("Erreur lors de la saisie ! Veuillez entrer un entier :");
  }
  return(int_nbrSaisi);
}

void jouer(int ** tab,int taille){
    int victoire;
    int compteur;
    victoire=0;
    compteur=0;
    
}

void Joueur(int** tab, int taille){
    int ligne;
    int colonne;
    printf("Où voulez vous jouer?\nChoissiez la ligne puis la colonne");
    ligne=saisie();
    colonne=saisie();
    //vérif de l'existance de la case et vérif si la case est bien vide
    while ((tab[ligne][colonne]!=' ' )|| (ligne<0 && ligne >=taille) || (colonne<0 && colonne>=taille))
    {
        printf("La case sélectionner n'est pas vide ou n'existe pas.\nVeuillez ressaisire une case valide\n");
        printf("Selectionner la ligne : ");
        ligne=saisie();
        printf("Selectionner la colonne");
        colonne=saisie();
    }
    tab[ligne][colonne]='X';
}

void ordi(int** tab, int taille){
    srand(time(NULL));
    int ligne;
    int colonne;
    ligne=rand()%taille;
    colonne=rand()%taille;
    //vérif de l'existance de la case et vérif si la case est bien vide
    while ((tab[ligne][colonne]!=' ' ))
    {
        ligne=rand()%taille;
        colonne=rand()%taille;
    }
    tab[ligne][colonne]='X';

}


int main (int argc, char ** argv){
    int **tab;//pointeur qui contiendra le jeu
    tab=createtab(3);
    affichage(tab,3);
    liberation(tab);
}