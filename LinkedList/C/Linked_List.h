#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct node *Node;
typedef struct linked_list *Linked_List;


//Building
Node new_Node(const int value);
Linked_List new_Linked_List();

// Linked_List Methods
int length(Linked_List linked_list);
Node get_current_node(Linked_List linked_list, int index);
void append_element(Linked_List linked_list, int value);
void insert_element_at(Linked_List linked_list, int value, int index);
int remove_element_at(Linked_List linked_list, int index);
int get_element_at(Linked_List linked_list, int index);
void rotate_left(Linked_List linked_list);
char* to_string(Linked_List linked_list);

// Free Methods
// TODO

#endif