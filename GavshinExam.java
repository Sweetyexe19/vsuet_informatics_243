public class Main {
    static class HashTable {
        //Хранений ключей
        private String[] keysArray;
        //Хранение значений
        private String[] valuesArray;
        //Счетчик
        private int count;

        //Сборщик
        public HashTable(int howMuchItCanHold) {
            keysArray = new String[howMuchItCanHold];
            valuesArray = new String[howMuchItCanHold];
            count = 0;
        }

        //Добаить значения
        public void put(String keyThing, String valueThing) {

            int whereToPut = Math.abs(keyThing.hashCode()) % keysArray.length;

            //Пропуск если место занято
            while (keysArray[whereToPut] != null && !keysArray[whereToPut].equals(keyThing)) {
                whereToPut = (whereToPut + 1) % keysArray.length;
            }

            //Добавление если место пустое
            if (keysArray[whereToPut] == null) {
                count++;
            }

            //Добавление ключ значение
            keysArray[whereToPut] = keyThing;
            valuesArray[whereToPut] = valueThing;
        }

        //Достать значения обратно
        public String get(String keyThing) {
            int whereToLook = Math.abs(keyThing.hashCode()) % keysArray.length;

            //Ищем пока не найдем
            while (keysArray[whereToLook] != null) {
                if (keysArray[whereToLook].equals(keyThing)) {
                    return valuesArray[whereToLook]; // Ура, нашли!
                }
                whereToLook = (whereToLook + 1) % keysArray.length;
            }

            return null;
        }

        //Колв-во элементов
        public int howManyThingsInside() {
            return count;
        }
    }

    //Тест
    public static void main(String[] args) {
        MyCoolHashTable myTable = new MyCoolHashTable(10);

        myTable.put("apple", "яблоко");
        myTable.put("banana", "банан");
        myTable.put("orange", "апельсин");
        myTable.put("grape", "виноград");

        System.out.println("apple -> " + myTable.get("apple"));    // Должно быть "яблоко"
        System.out.println("banana -> " + myTable.get("banana"));  // Должно быть "банан"

        System.out.println("pear -> " + myTable.get("pear"));      // Должно быть null

        System.out.println("Всего элементов: " + myTable.howManyThingsInside()); // Должно быть 4
    }
}