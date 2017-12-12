import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class d121{
  public static void main(String arg[]){
    String line;
    Pattern p = Pattern.compile("^(\\d*)\\W+([\\d ,]*)$");
    HashMap<Integer,HashSet<Integer>> pipes = new HashMap<>();
    Matcher match;
    System.out.print("filename:");
    String input = System.console().readLine();
    
    try {
      BufferedReader bufferreader = new BufferedReader(new FileReader(input));
      line = bufferreader.readLine();
      while (line != null) {
	match = p.matcher(line);
	if(match.matches()){
	  HashSet<Integer> ints = new HashSet<>();
	  int key = Integer.parseInt(match.group(1));
	  for(String s : match.group().split("\\W+")){
	    ints.add(Integer.parseInt(s));
	  }
	  pipes.put(key, ints);
	}
	line = bufferreader.readLine();
      }
      bufferreader.close();
    } catch (FileNotFoundException ex) {
	ex.printStackTrace();
    } catch (IOException ex) {
	ex.printStackTrace();
    }
    Stack<Integer> stack = new Stack<>(); 
    HashSet<Integer> visit = new HashSet<>();
    stack.push(0);
    while(!stack.empty()){
      int i = stack.pop();
      visit.add(i);
      for(int j : pipes.get(i)){
        if(!visit.contains(j)){stack.push(j);}
      }
    }
    System.out.println(visit.size());
  }
}
