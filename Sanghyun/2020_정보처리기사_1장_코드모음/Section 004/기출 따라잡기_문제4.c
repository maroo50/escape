#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
main()
{
	int i = 10, j = 10, k = 30;
	i /= j;   // 10/10 = 1
	j -= i;   // 10 - 1 = 9  
	k %= j;  // 30/9 9*3 = 27 나머지는 3, 왼쪽의 변수에 오른쪽으로 나눈값으로 나눈 나머지를 대입한다.
	printf("%d, %d, %d\n", i, j, k);
}