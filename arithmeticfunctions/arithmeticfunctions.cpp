#include "arithmeticfunctions.h"

int cube(int x){
    return x * x * x;
}

int max(int x, int y){
    if (x > y) {
        return x;
    } else {
        return y;
    }
}

int difference(int x, int y){
    return x - y;
}
