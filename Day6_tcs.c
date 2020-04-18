//Day6 Program 
//TCS Practice test
//18 apr 2020



#include<stdio.h>
char * fun(char *s)
{
	char ph[10][10]={""," ","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"};
	int i,j=0,z=0;
	static char s1[100];
	//printf("%s",s);
	for(i=0;s[i]!='\0';i++)
	{
		j++;
		if(s[i]==' ')
		{
			s1[z++]=ph[s[i-1]-48][j-2];
			j=0;
		}
	}
	s1[z++]=ph[s[i-1]-48][j-1];
	s1[z]='\0';
	//printf("%s",s1);
	
	return s1;
}
int main()
{
	char s[100],*res;
	scanf("%[^\n]s",s);
	res=fun(s);
	printf("%s",res);
	
}
