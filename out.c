#include<stdio.h>
int main(){
float num;
int i;
if(0 == scanf("%f", &num)) {
num = 0;
scanf("%*s");
}
void checkNumber(float x) {
if(x<0){
printf("This is a negative number\n");
} else {
printf("This is zero or a positive number\n");
}
}
i = -3;
while(i<=num){
checkNumber(i);
i = i+1;
}
return 0;
}
