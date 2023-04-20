#include <stdio.h>
#include "Linked_List.h"

int main(int argc, char const *argv[]) {
    Linked_List ll = new_Linked_List();
    append_element(ll, 1);
    append_element(ll, 2);
    rotate_left(ll);
    printf("%s\n", to_string(ll));
    return 0;
}
