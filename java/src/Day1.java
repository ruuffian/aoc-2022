import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Day1 {

    Scanner read_data() throws FileNotFoundException {
        File data = new File("resources/day1.txt");
        return new Scanner(data);
    }

    public int part1() throws FileNotFoundException {
        Scanner scanner = read_data();
        int max = 0;
        while (scanner.hasNext()) {
            String cal;
            int elf = 0;
            cal = scanner.nextLine();
            while (!cal.equals("") && scanner.hasNext()) {
                elf += Integer.parseInt(cal);
                cal = scanner.nextLine();
            }
            if (elf > max) {
                max = elf;
            }
        }
        return max;
    }

    public int part2() throws FileNotFoundException {
        Scanner scanner = read_data();
        ArrayList<Integer> lst = new ArrayList<>();
        while (scanner.hasNext()) {
            String cal;
            int elf = 0;
            cal = scanner.nextLine();
            while (!cal.equals("") && scanner.hasNext()) {
                elf += Integer.parseInt(cal);
                cal = scanner.nextLine();
            }
            lst.add(elf);
        }
        Collections.sort(lst);
        Collections.reverse(lst);
        return lst.get(0) + lst.get(1) + lst.get(2);
    }
}
