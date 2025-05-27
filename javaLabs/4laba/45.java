public class ArabicToRoman {
    private static final String[] ROMAN_NUMERALS = {
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    };
    private static final int[] ARABIC_VALUES = {
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    };

    public static String convert(int arabic) {
        if (arabic <= 0 || arabic >= 10000) {
            throw new IllegalArgumentException("Number must be in range 1 < n < 10000");
        }
        StringBuilder roman = new StringBuilder();
        for (int i = 0; i < ARABIC_VALUES.length; i++) {
            while (arabic >= ARABIC_VALUES[i]) {
                roman.append(ROMAN_NUMERALS[i]);
                arabic -= ARABIC_VALUES[i];
            }
        }
        return roman.toString();
    }

    public static void main(String[] args) {
        int arabic = 1987;
        System.out.println(arabic + " -> " + convert(arabic));
    }
}