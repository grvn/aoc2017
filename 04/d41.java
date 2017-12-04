import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.*;

public class d41{
    public static void main(String arg[]){

	String line;
	int valid = 0;
	System.out.print("filename:");
	String input = System.console().readLine();

	try {

	    BufferedReader bufferreader = new BufferedReader(new FileReader(input));
	    line = bufferreader.readLine();

	    while (line != null) {
		if(!dubbles(line)){ valid++;}
		line = bufferreader.readLine();
	    }

	} catch (FileNotFoundException ex) {
	    ex.printStackTrace();
	} catch (IOException ex) {
	    ex.printStackTrace();
	}
	System.out.println(valid);
    }

    public static boolean dubbles(String arg){
	String[] ss = arg.split("\\s+");
	Set<String> parts = new HashSet<String>();
	for(String s : ss){
	    if(parts.contains(s)){
		return true;
	    }
	    parts.add(s);
	}
	return false;
    }
}
