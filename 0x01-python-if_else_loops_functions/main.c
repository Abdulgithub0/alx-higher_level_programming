#include <stdio.h>

/**
 *
 *
 */

void main()
{
	int arr[] = {2,3,6,9,5,10,4};
	int lenght = sizeof(arr) / sizeof(int);
	int i = 0;
	//sort the array
	while (i < lenght)
	{
		for (int j = 0; j < lenght - 1; j++)
		{
			if (arr[i] > arr[j + 1])
			{
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
		i++;
	}
	for (i = 0; i < lenght; i++)
		printf("%d", arr[i]);
	printf("\n");
}
