import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class myprog{
    public static void main(String[] args) {
        try (FileInputStream input = new FileInputStream("abc.txt");
             FileOutputStream output = new FileOutputStream("xyz.txt")) {
            int byteRead;
            while ((byteRead = input.read()) != -1) {
                output.write(byteRead);
            }
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}