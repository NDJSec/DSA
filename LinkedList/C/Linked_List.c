#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "Linked_List.h"

struct node
{
    int value;
    Node next;
    Node prev;
};


struct linked_list
{
    int size;
    Node header;
    Node trailer;
};

Node new_Node(const int value) {
    Node node = (Node) malloc(sizeof(struct node));
    node->value = value;
    node->next = NULL;
    node->prev = NULL;
    return node;
}

Linked_List new_Linked_List() {
    Linked_List linked_list = (Linked_List) malloc(sizeof(struct linked_list));
    linked_list->header = new_Node(NULL);
    linked_list->trailer = new_Node(NULL);
    linked_list->size = 0;

    linked_list->header->next = linked_list->trailer;
    linked_list->trailer->prev = linked_list->header;
    return linked_list;
}

int length(Linked_List linked_list) {
    return linked_list->size;
}

Node get_current_node(Linked_List linked_list, int index) {
    Node current;
    if(linked_list->size - index >= linked_list->size / 2) {
        current = linked_list->header;
        for(int i = 1; i <= index; i++) {
            current = current->next;
        }
    } else {
        current = linked_list->trailer;
        for(int i = 0; i <= linked_list->size - index; i++) {
            current = current->prev;
        }
    }
    return current;
}

void append_element(Linked_List linked_list, int value) {
    Node new_node = new_Node(value);
    if(linked_list->size == 0) {
        linked_list->header->next = new_node;
        linked_list->trailer->prev = new_node;
        new_node->next = linked_list->trailer;
        new_node->prev = linked_list->header;
    } else {
        new_node->next = linked_list->trailer;
        new_node->prev = linked_list->trailer->prev;
        linked_list->trailer->prev->next = new_node;
        linked_list->trailer->prev = new_node;
    }
    linked_list->size++;
}

void insert_element_at(Linked_List linked_list, int value, int index) {
    if(index >= linked_list->size || index < 0) {
        perror("ERROR: Index out of bounds");
    }

    Node new_node = new_Node(value);
    if(linked_list->size - index >= linked_list->size / 2) {
        Node current = linked_list->header;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        new_node->next = current->next;
        new_node->prev = current;
        current->next->prev = new_node;
        current->next = new_node;
    } else {
        Node current = linked_list->trailer;
        for (int i = 0; i < index; i++) {
            current = current->prev;
        }
        new_node->next = current;
        new_node->prev = current->prev;
        current->prev->next = new_node;
        current->prev = new_node;
    }
    linked_list->size++;
}

int remove_element_at(Linked_List linked_list, int index) {
    if(index >= linked_list->size || index < 0) {
        perror("ERROR: Index out of bounds");
    }

    Node current = get_current_node(linked_list, index);
    int deletedValue;
    if(index == linked_list->size - 1) {
        deletedValue = current->next->value;
        current->next = current->next->next;
        linked_list->trailer->prev = current;
    } else {
        deletedValue = current->next->value;
        current->next = current->next->next;
        current->next->prev = current;
    }
    linked_list->size--;
    return deletedValue;
}

int get_element_at(Linked_List linked_list, int index) {
    if(index + 1 > linked_list->size || index < 0) {
        perror("ERROR: Index out of bounds");
    }

    Node current = get_current_node(linked_list, index+1);
    return current->value;
}

void rotate_left(Linked_List linked_list) {
    if(linked_list->size <= 0) {
        return;
    }
    int node_to_rotate = remove_element_at(linked_list, 0);
    append_element(linked_list, node_to_rotate);
}

char* to_string(Linked_List linked_list) {
    if(linked_list->size == 0) {
        return strdup("[ ]");
    }

    char temp_contents[100];
    char* contents = (char*) malloc(100 * sizeof(char));
    strcpy(contents, "[");
    
    Node current = linked_list->header->next;
    while(current != linked_list->trailer) {
        sprintf(temp_contents, "%d,", current->value);
        strcat(contents, temp_contents);
        current = current->next;
    }
    contents[strlen(contents)-1] = ']';
    
    return contents;
}





