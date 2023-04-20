#pragma once
#ifndef LINKED_LIST_HPP
#define LINKED_LIST_HPP

#include <stdexcept>
#include <sstream>
#include <string>

template<typename T>
class Linked_List {
private:
    class Node {
    public:
        T value;
        Node* next;
        Node* prev;
        Node(T value);
        ~Node();
    };
    int size;
    Node* header;
    Node* trailer;

    Node* getCurrentNode(int index);

public:
    Linked_List();
    ~Linked_List();
    int length();
    void appendElement(T value);
    void insertElementAt(T value, int index);
    T removeElementAt(int index);
    T getElementAt(int index);
    void rotateLeft();
    std::string toString() const;

};

template <typename T>
Linked_List<T>::Node::Node(T value) {
    this->value = value;
    this->next = nullptr;
    this->prev = nullptr;
}

template <typename T>
Linked_List<T>::Node::~Node() {}

template <typename T>
typename Linked_List<T>::Node* Linked_List<T>::getCurrentNode(int index) {
    Node* current;
    if (this->size - index >= this->size / 2) {
        current = this->header;
        for (int i = 1; i <= index; i++) {
            current = current->next;
        }
    } else {
        current = this->trailer;
        for (int i = 0; i < this->size - index; i++) {
            current = current->prev;
        }
    }
    return current;
}

template <typename T>
Linked_List<T>::Linked_List() {
    this->header = new Node(T());
    this->trailer = new Node(T());
    this->size = 0;

    header->next = this->trailer;
    trailer->prev = this->header;
}

template <typename T>
Linked_List<T>::~Linked_List() {
    Node* current = this->header->next;
    while (current != this->trailer) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }

    delete this->header;
    delete this->trailer;
}

template <typename T>
int Linked_List<T>::length() {
    return this->size;
}

template <typename T>
void Linked_List<T>::appendElement(T value) {
    Node* new_node = new Node(T(value));
    if (this->size == 0) {
        this->header->next = new_node;
        this->trailer->prev = new_node;
        new_node->next = this->trailer;
        new_node->prev = this->header;
    } else {
        new_node->next = this->trailer;
        new_node->prev = this->trailer->prev;
        this->trailer->prev->next = new_node;
        this->trailer->prev = new_node;
    }
    this->size++;
}

template <typename T>
void Linked_List<T>::insertElementAt(T value, int index) {
    if(index >= this->size || index < 0) {
        throw std::out_of_range("Index out of range");
    }
    Node* new_node = new Node(T(value));
    Node* current = getCurrentNode(index);
    new_node->next = current;
    new_node->prev = current->prev;
    current->prev->next = new_node;
    current->prev = new_node;
    this->size++;
}

template <typename T>
T Linked_List<T>::removeElementAt(int index) {
    if(index >= this->size || index < 0) {
        throw std::out_of_range("Index out of range");
    }
    Node* current = getCurrentNode(index);
    T deletedValue;
    if(index == this->size - 1) {
        deletedValue = current->next->value;
        current->next = current->next;
        this->trailer->prev = current;
    } else {
        deletedValue = current->next->value;
        current->next = current->next->next;
        current->next->prev = current;
    }
    this->size--;
    return deletedValue;
}

template <typename T>
T Linked_List<T>::getElementAt(int index) {
    if(index + 1 > this->size || index < 0) {
        throw std::out_of_range("Index out of range");
    }

    Node* current = getCurrentNode(index+1);
    return current->value;
}

template <typename T>
void Linked_List<T>::rotateLeft() {
    if(this->size <= 0) {
        return;
    }
    T nodeToRotate = removeElementAt(0);
    appendElement(nodeToRotate);
}

template <typename T>
std::string Linked_List<T>::toString() const {
    if (this->size == 0) {
        return "[ ]";
    }

    std::ostringstream ss;
    ss << "[ ";
    Node* current = this->header->next;
    while (current != this->trailer) {
        ss << current->value << ", ";
        current = current->next;
    }
    std::string contents = ss.str();
    contents = contents.substr(0, contents.length()-2);
    contents += " ]";
    return contents;
}


#endif
