
#include <stdio.h>
#include <stdlib.h>

int  main(){
int idade, soma =0 , contador =0; // deaclaração de variaveis
float media;

while ( idade >= 0 || contador <= 30){
  printf("Digite a idade: ");
  scanf("%d", &idade);
  if (idade < 0){ //tratamento de erro pra idade negativa nao contabilizar
    break;
  }
  soma = soma + idade;
  contador++;
}
media = soma / contador;
printf("A media das idades é: %f", media);
  return 0;
}
