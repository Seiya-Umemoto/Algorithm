package kr.ac.sunmoon;

import java.util.Vector;

public class PrintSubset {
	private static void subsetPrint(Vector<Character> given_array, Vector<Character> subset, int depth) {
		if(depth == given_array.size()) {
			print(subset);
		} else {
			subsetPrint(given_array, subset, depth+1);
			subset.add(given_array.get(depth));
			subsetPrint(given_array, subset, depth+1);
			subset.remove(subset.size()-1);
		}
	}
	
	private static void print(Vector<Character> subset) {
		System.out.print('{');
		for(int i=0; i<subset.size(); i++) {
			if (i<subset.size()-1)
				System.out.print(subset.get(i) + ", ");
			else
				System.out.print(subset.get(i));
		}
		System.out.println('}');
	}
	
	public static void main(String[] args) {
		Vector<Character> given_array = new Vector<Character>();
		given_array.add('a');
		given_array.add('b');
		given_array.add('c');
		Vector<Character> subset = new Vector<Character>();
		subsetPrint(given_array, subset, 0);
	}
}
