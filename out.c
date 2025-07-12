#include<stdio.h>
int main(){
float x;
int i;
printf("ഒരു സംഖ്യ നൽകുക:\n");
if(0 == scanf("%f", &x)) {
x = 0;
scanf("%*s");
}
if(x>0){
printf("സൂചിക ചെറുതാണ്\n");
} else {
printf("സൂചിക വലിയതാണ് അല്ലെങ്കിൽ പൂജ്യം\n");
}
i = 1;
while(i<=x){
printf("%.2f\n", (float)(i));
i = i+1;
}
return 0;
}
