package practise;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Practise {

	public static void main(String[] args) {

		List<String> boxList = Arrays.asList("ykc 82 01", "eo first qpx", "09z cat hamster", "06f 12 25 6",
				"azo first qpx", "236 cat dog rabbit snake");
		
		List <String> filter1 = boxList.stream().filter(s->s.contains("cat dog rabbit")).collect(Collectors.toList());
		System.out.println(filter1);

		
		
	}

	private static boolean contains(List<String> boxList, String s) {
		for(String box: boxList) {
			if(box.contains(s)) {
				
			}
		}
		return false;
	}
	
	

}
