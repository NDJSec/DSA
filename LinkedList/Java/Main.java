package Java;

public class Main {
    public static void main(String[] args) {
        Linked_List<Integer> LL = new Linked_List<>();
        LL.appendElement(100);
        System.out.println(LL.length());
        System.out.println(LL.toString());
    }
}
