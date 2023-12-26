import java.io.FileNotFoundException;
import java.net.URISyntaxException;

public class Main {
    public static void main(String[] args) throws FileNotFoundException, URISyntaxException {
        Day1 day1 = new Day1();
        System.out.printf("The maximum calories: %d\n", day1.part1());
        System.out.printf("The top 3 calories summed: %d\n", day1.part2());

    }
}