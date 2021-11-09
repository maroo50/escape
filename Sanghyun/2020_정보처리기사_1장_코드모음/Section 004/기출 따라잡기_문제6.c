#include <stdio.h>
main()
{
	int a = 5, b = 10, c = 15, d = 30, result;
	result = a * 3 + b > d || c - b / a <= d && 1;
	printf("%d\n", result);
}

// 5* 3 + 10 = 25 > 30 == false = 0
// 15 - (10/5) = 13 <= 10  == false 0
// 