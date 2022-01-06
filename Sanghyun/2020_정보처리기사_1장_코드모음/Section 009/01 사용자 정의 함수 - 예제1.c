#include <stdio.h>
void func(int i, int j);
main()
{
    int a = 3, b = 12;
    func(a, b);
    printf("%d, %d\n", a, b);
}
void func(i, j) int i, j;
{
    i *= 3;
    j /= 3;
    printf("%d, %d\n", i, j);
}

// 1. main 실행 a에 3, b에 12가 변수로 저장
// 2. func 함수에 3, 12 입력 - void 선언된 함수에 a, b 값이 i,j로 치환 따라서, i는 3 j는 12로 변수가 저장 됨 - 3*3 = 9, 3/12= 4 - print 함수로 i, j  값을 출력
// void 타입은 C에서 파생된 여러 언어에서 정상적으로 반환하지만 호출자에게 결과 값을 제공하지 않는 함수의 결과를 위한 타입
// 3. a값 3과 b값 12가 출력 됨
// ---- 정답 ----
// 9, 4
// 3, 12