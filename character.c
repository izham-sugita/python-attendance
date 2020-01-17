#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main()
{

  char *name0;
  char name1[10];
  char name2[]="Hello"; //pre-determine size

  printf("Enter a name:\n");
  scanf("%s", name1);

  printf("Your name is %s\n", name1);

  printf("%s\n", name2);

  printf("Enter a new name:");
  scanf("%s", &name0);

  printf("%s\n", &name0);

  name1[0] = 'J';
  printf("New name: %s\n", name1);

  /*The simplest way to take a name*/
  char name3;
  scanf("%s", &name3);
  printf("Name #3 is %s\n", &name3);
  printf("name value: %d\n", name3);

  char *filename = &name3;
  printf("filename = %s\n", filename);
  
}
