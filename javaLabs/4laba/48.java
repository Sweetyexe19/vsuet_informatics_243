import java.util.TreeSet;

public class USequence {
    public static void generateUSequence(int x) {
        TreeSet<Integer> sequence = new TreeSet<>();
        sequence.add(1); // u(0) = 1

        for (int i = 0; i < x; i++) {
            int current = sequence.first();
            sequence.remove(current);

            int y = 2 * current + 1;
            int z = 3 * current + 1;

            sequence.add(y);
            sequence.add(z);
        }

        System.out.println("U sequence: " + sequence);
    }

    public static void main(String[] args) {
        int x = 10;
        generateUSequence(x);
    }
}