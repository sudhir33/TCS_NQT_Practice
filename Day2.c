//String valid or not
//14/apr/2020
//TCS NQT DAY2
#include<stdio.h>
#include<stdlib.h>
char *remove_dupliactes(char *str)
{
	static char str1[100];
	int i,j,l1=1,flag=0;
	str1[0]=str[0];
	for(i=0;str[i]!='\0';i++)
	{
		flag=0;
		for(j=0;j<l1;j++)
		{
			if(str[i]==str1[j])
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			str1[l1++]=str[i];
		}	
	}
	str1[l1]='\0';
	//printf("%s\n",str1);
	return str1;
}
int find_freq(char s,char * str)
{
	int i=0,c=0;
	for(i=0;str[i]!='\0';i++)
	{
		if(s==str[i])
		{
			c++;	
		}
	}
	//printf("%d\n",c);
	return c;
}
char *valid_not(char *str)
{
	char *str1;
	int c1=0,i,c2,d=0;
	str1=remove_dupliactes(str);
	//printf("%s",res);
	c1=find_freq(str1[0],str);
	for(i=1;str1[i]!='\0';i++)
	{
		c2=find_freq(str1[i],str);
		//printf("%d %d %d\n",c1,c2,c2-c1);
		if(abs(c1-c2)==1)
		{
			d=d+1;
		}
		if(abs(c1-c2)>1 || d==2)
		{
			return "not valid";
		}
	}
	if(d==1)
	{
		return "make valid";
	}
	return "valid";
}
void main()
{
	char str[100],*res;
	scanf("%s",&str);
	res=valid_not(str);
	printf("%s",res);
}
