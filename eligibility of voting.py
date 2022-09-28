#include<stdio.h>
int main()
{
int i;
printf("enter the age of person: ");
scanf("%d",&i);

if(i>=18)
 {
   printf("Eligible for voting ");
 }
  else
    {
      printf("Eligible for Not voting! ");
    }
    return 0;
}
