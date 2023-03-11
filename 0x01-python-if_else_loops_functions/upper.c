#include <stdio.h>
#include <string.h>
/**
 *
 */

int main(int argc, char **argv)
{
	char *best = argv[1];
	char check;

	if (argv[1] == NULL || argv[2] != NULL){
			printf("Enter a single string argument\n"); return 1;}
	int len1 = strlen(best);
	for(int i = 0; i < len1; i++)
	{
		check = best[i];
		if (check >= 'a' && check <= 'z')
		       check -= 32;
		printf("%c", check);
	}
	printf("\n");
	return 0;
}


