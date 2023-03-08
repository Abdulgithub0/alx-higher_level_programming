#include <stdio.h>
#include <string.h>
/**
 *
 */

int main()
{
	char *best = "Best";
	char *school = "Best School is Alx";
	char check;
	int len1 = strlen(best);
	printf("%s\n%s\n", best, school);
	for(int i = 0; i < len1; i++)
	{
		check = best[i];
		if (check >= 'a' && check <= 'z')
		       check -= 32;
		printf("%c", check);
	}
	printf("\n");
	for (int i = 0; i < strlen(school); i++)
	{
		check = school[i];
		if (check >= 'a' && school[i] <= 'z')
			check -= 32;
		printf("%c", check);
	}
	printf("\n");
}


