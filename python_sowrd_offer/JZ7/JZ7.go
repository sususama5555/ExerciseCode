package main

/**
 *
 * @param n int整型
 * @return int整型
*/
func Fibonacci( n int ) int {
    // write code here
    if (n <= 2){
        return 1
    }
    return Fibonacci(n-1) + Fibonacci(n-2)
}
