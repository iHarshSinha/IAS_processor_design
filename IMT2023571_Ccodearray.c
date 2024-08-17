#include<stdio.h>
int maxil(int a[],int n){
  int maxi=a[0];
  for(int i=0;i<n;i++){
      if(a[i]>maxi){
        maxi=a[i];  
    }
  }
  return maxi;
  
    }
int minil(int a[],int n){
  int mini=a[0];
  for(int i=0;i<n;i++){
    if(a[i]<mini){
      mini=a[i];  
  }
  }
  return mini;
  
}

int range(int a[],int n){
  int maxi=maxil(a,n);
  int mini=minil(a,n);
  return maxi-mini;
}
int mean(int a[],int n){
  int sum=0;
  for(int i=0;i<n;i++){
    sum=sum+a[i];
  }
  return sum/n;
}
int dispersion(int a[],int n){
  int maxi=maxil(a,n);
  int mini=minil(a,n);
  int d=(maxi-mini)/(maxi+mini);
  return d;
}

int main(){
  int a[10]={2,7,1,6,5,19,123,80,0,2};
  printf("The max element is: %d\n",maxil(a,10));
  printf("The min element is: %d\n",minil(a,10));
  printf("The range is: %d\n",range(a,10));
  printf("The mean is: %d\n",mean(a,10));
  printf("The coeff. of dispersion is: %d\n",dispersion(a,10));
}