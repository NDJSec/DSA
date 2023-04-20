mod linked_list;

use linked_list::LinkedList as LL;

fn main() {
    let mut ll = LL::<i32>::new();
    ll.append_element(1);
    ll.append_element(2);
    ll.append_element(3);
    

    println!("Element at 1: {:?}", ll.get_element_at(1).unwrap());

    println!("The list has {} elements", ll.length());
    println!("The list contains {}", ll.to_string())
}
