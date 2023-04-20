package linkedlist

import (
	"fmt"
	"log"
)

type node struct {
	value *int
	next  *node
	prev  *node
}

type linked_list struct {
	size    int
	header  *node
	trailer *node
}

func new_Node(value *int) *node {
	var node *node = &node{
		value: value,
		next:  nil,
		prev:  nil,
	}
	return node
}

func New_Linked_List() *linked_list {
	var linked_list *linked_list = &linked_list{
		header:  new_Node(nil),
		trailer: new_Node(nil),
		size:    0,
	}
	linked_list.header.next = linked_list.trailer
	linked_list.trailer.prev = linked_list.header
	return linked_list
}

func (ll linked_list) Length() int {
	return ll.size
}

func (ll linked_list) get_current_node(index int) *node {
	var current *node
	if ll.size-index >= ll.size/2 {
		current = ll.header
		for i := 0; i <= index; i++ {
			current = current.next
		}
	} else {
		current = ll.trailer
		for i := 0; i <= ll.size-index; i++ {
			current = current.prev
		}
	}
	return current
}

func (ll *linked_list) Append_element(value int) {
	var new_node *node = new_Node(&value)
	if ll.size == 0 {
		ll.header.next = new_node
		ll.trailer.prev = new_node
		new_node.next = ll.trailer
		new_node.prev = ll.header
	} else {
		new_node.next = ll.trailer
		new_node.prev = ll.trailer.prev
		ll.trailer.prev.next = new_node
		ll.trailer.prev = new_node
	}
	ll.size += 1
}

func (ll *linked_list) Insert_element_at(value *int, index int) {
	if index >= ll.size || index < 0 {
		log.Fatal("ERROR: Index out of bounds")
	}

	var new_node *node = new_Node(value)
	if ll.size-index >= ll.size/2 {
		var current *node = ll.header
		for i := 0; i < index; i++ {
			current = current.prev
		}
		new_node.next = current.next
		new_node.prev = current
		current.next.prev = new_node
		current.next = new_node
	} else {
		var current *node = ll.trailer
		for i := 0; i < index; i++ {
			current = current.prev
		}
		new_node.next = current
		new_node.prev = current.prev
		current.prev.next = new_node
		current.prev = new_node
	}
	ll.size += 1
}

func (ll *linked_list) Remove_element_at(index int) int {
	if index >= ll.size || index < 0 {
		log.Fatal("ERROR: Index out of bounds")
	}

	var current *node = ll.get_current_node(index - 1)
	var deletedValue int
	if index == ll.size-1 {
		deletedValue = *current.next.value
		current.next = current.next.next
		ll.trailer.prev = current
	} else {
		deletedValue = *current.next.value
		current.next = current.next.next
		current.next.prev = current
	}
	ll.size -= 1
	return deletedValue
}

func (ll *linked_list) Get_element_at(index int) int {
	if index >= ll.size || index < 0 {
		log.Fatal("ERROR: Index out of bounds")
	}

	var current *node = ll.get_current_node(index + 1)
	return *current.value
}

func (ll *linked_list) Rotate_left() {
	if ll.size <= 0 {
		return
	}
	var node_to_rotate int = ll.Remove_element_at(0)
	ll.Append_element(node_to_rotate)
}

func (ll linked_list) String() string {
	if ll.size == 0 {
		return "[ ]"
	}
	var current *node = ll.header
	var contents string = "["
	for {
		if current.next == ll.trailer {
			break
		}
		current = current.next
		contents += fmt.Sprintf(" %d,", *current.value)
	}
	var finalString string = contents[:len(contents)-1]
	return finalString + " ]"
}
