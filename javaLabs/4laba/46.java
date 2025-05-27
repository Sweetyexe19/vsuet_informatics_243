import java.util.HashMap;
import java.util.Map;

public class RomanToArabic {
    private static final Map<Character, Integer> ROMAN_VALUES = new HashMap<>() {{
        put('I', 1);
        put('V', 5);
        put('X', 10);
        put('L', 50);
        put('C', 100);
        put('D', 500);
        put('M', 1000);
    }};

    public static int convert(String roman) {
        int arabic = 0;
        int prevValue = 0;
        for (int i = roman.length() - 1; i >= 0; i--) {
            int currentValue = ROMAN_VALUES.get(roman.charAt(i));
            if (currentValue < prevValue) {
                arabic -= currentValue;
            } else {
                arabic += currentValue;
            }
            prevValue = currentValue;
        }
        return arabic;
    }

    public static void main(String[] args) {
        String roman = "MCMLXXXVII";
        System.out.println(roman + " -> " + convert(roman));
    }
}