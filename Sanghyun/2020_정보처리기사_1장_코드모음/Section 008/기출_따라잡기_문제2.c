#include <stdio.h>
main()
{
	char a[] = { 'A', 'B', 'C', 'D', 'E', 'F' };
	char* p;
	p = &a[2];
	printf("%c, %c\n", *p, *(p - 2));
}


/*p + 2 주소는 오른쪽으로 2칸 이동한 p이다.*/
// #include <stdio.h>
// main()
// {
// 	char b[] = { 'A','B','C','D','E','F' };
// 	char * p;
// 	p = &b[2];
// 	printf("%c, %c\n", *p, *(p + 2));
// }