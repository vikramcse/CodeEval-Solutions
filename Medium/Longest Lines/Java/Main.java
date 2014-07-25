package longestLines;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.TreeMap;

public class Main {
    public static void main (String[] args) throws IOException{
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));

        TreeMap<Integer, String> map = new TreeMap<Integer, String>();
        String line;
        String N = in.readLine();

        while ((line = in.readLine()) != null) {
            line = line.trim();
            if (line.length() > 0 && !line.equals(N))
                map.put(line.length(), line);
        }

        int limit = Integer.parseInt(N);
        int countTo = 0;

        for (Integer i : map.descendingKeySet()) {
            if (countTo != limit) {
                System.out.println(map.get(i));
                countTo++;
            }
            else
                break;
        }
    }
}
