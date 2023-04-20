#include <iostream>
#include "Linked_List.hpp"

int main (int argc, char *argv[])
{
    Linked_List<int> list;
    list.appendElement(1);
    list.appendElement(2);
    list.appendElement(3);
    list.appendElement(4);
    list.appendElement(5);

    std::cout << "List contents: " << list.toString() << std::endl;

    return EXIT_SUCCESS;
}
