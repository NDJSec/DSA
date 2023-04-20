package Java;

/**
 * Linked_List
 * @param <T>
 */

class Linked_List<T> {
    private class Node<T> {
        public  T value;
        public Node<T> next;
        public Node<T> prev;

        public Node(T value) {
            this.value = value;
            this.next = null;
            this.prev = null;
        }
    }

    private int size;
    private Node<T> header;
    private Node<T> trailer;

    public Linked_List() {
        this.header = new Node<T>(null);
        this.trailer =  new Node<T>(null);
        this.size = 0;

        header.next = this.trailer;
        trailer.prev = this.header;
    }

    public int length() {
        return this.size;
    }

    private Node<T> getCurrentNode(int index) {
        Node<T> current;
        if(this.size - index >= this.size / 2) {
            current = this.header;
            for(int i = 1; i <= index; i++) {
                current = current.next;
            }
        } else {
            current = this.trailer;
            for (int i = 0; i < this.size - index; i++) {
                current = current.prev;
            }
        }
        return current;
    }

    public void appendElement(T value) {
        Node<T> new_node = new Node<T>(value);
        if(this.size == 0) {
            this.header.next = new_node;
            this.trailer.prev = new_node;
            new_node.next = this.trailer;
            new_node.prev = this.header;
        } else {
            new_node.next = this.trailer;
            new_node.prev = this.trailer.prev;
            this.trailer.prev.next = new_node;
            this.trailer.prev = new_node;
        }
        this.size++;
    }

    public void insertElementAt(T value, int index) {
        if(index >= this.size || index < 0) { 
            throw new IndexOutOfBoundsException("ERROR: Index out of bounds"); 
        }

        Node<T> new_node = new Node<T>(value);
        if(this.size - index >= this.size / 2) {
            Node<T> current = this.header;
            for(int i = 1; i <= index; i++) {
                current = current.next;
            }
            new_node.next = current.next;
            new_node.prev = current;
            current.next.prev = new_node;
            current.next = new_node;
        } else {
            Node<T> current = this.trailer;
            for (int i = 0; i < this.size - index; i++) {
                current = current.prev;
            }
            new_node.next = current;
            new_node.prev = current.prev;
            current.prev.next = new_node;
            current.prev = new_node;
        }

        this.size++;
    }

    public T removeElementAt(int index) {
        if(index >= this.size || index < 0) { 
            throw new IndexOutOfBoundsException("ERROR: Index out of bounds"); 
        }

        Node<T> current = getCurrentNode(index);
        T deletedValue;
        if(index == this.size - 1) {
            deletedValue = current.next.value;
            current.next = current.next.next;
            this.trailer.prev = current;
        } else {
            deletedValue = current.next.value;
            current.next = current.next.next;
            current.next.prev = current;
        }
        this.size--;
        return deletedValue;
    }

    public T getElementAt(int index) {
        if(index + 1 > this.size || index < 0) {
            throw new IndexOutOfBoundsException("ERROR: Index out of bounds"); 
        }

        Node<T> current = getCurrentNode(index+1);
        return current.value;
    }

    public void rotateLeft() {
        if(this.size <= 0) {
            return;
        }
        T nodeToRotate = removeElementAt(0);
        appendElement(nodeToRotate);
    }

    @Override
    public String toString() {
        if(this.size == 0) {
            return "[ ]";
        }

        Node<T> current = this.header;
        String contents = "[";
        while(current.next != this.trailer) {
            current = current.next;
            contents += String.format(" %s,", current.value);
        }
        return contents.substring(0, contents.length()-1)+" ]";
    }

}


