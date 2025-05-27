import java.util.Arrays;
import java.util.Random;

public class SnakeSort {
    public static int[] snailSort(int[][] array) {
        if (array == null || array.length == 0) return new int[0];
        int n = array.length;
        int[] result = new int[n * n];
        int index = 0;
        int rowStart = 0, rowEnd = n - 1;
        int colStart = 0, colEnd = n - 1;

        while (rowStart <= rowEnd && colStart <= colEnd) {

            for (int i = colStart; i <= colEnd; i++) {
                result[index++] = array[rowStart][i];
            }
            rowStart++;
            for (int i = rowStart; i <= rowEnd; i++) {
                result[index++] = array[i][colEnd];
            }
            colEnd--;
            if (rowStart <= rowEnd) {
                for (int i = colEnd; i >= colStart; i--) {
                    result[index++] = array[rowEnd][i];
                }
                rowEnd--;
            }
            if (colStart <= colEnd) {
                for (int i = rowEnd; i >= rowStart; i--) {
                    result[index++] = array[i][colStart];
                }
                colStart++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 3;
        int[][] array = new int[n][n];
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                array[i][j] = random.nextInt(10);
            }
        }
        System.out.println("Original:");
        for (int[] row : array) {
            System.out.println(Arrays.toString(row));
        }
        System.out.println("sorted: " + Arrays.toString(snailSort(array)));
    }
}