package main

import (
	"fmt"

	linkedlist "github.com/NDJSec/LinkedList/cmd/LinkedList"
)

func main() {
	ll := linkedlist.New_Linked_List()
	ll.Append_element(1)
	ll.Append_element(2)
	ll.Rotate_left()
	fmt.Println(ll)
}
