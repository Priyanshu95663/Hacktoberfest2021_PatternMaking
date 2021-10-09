import java.util.Scanner;

public class VerticalTriangle {

	public static void main(String[] args) {
		// Numerical Pattern
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		int nr = 2 * n - 1;
		int nst = 1;
		int val;
		for (int row = 1; row <= nr; row++) {
			if(row>=nr/2 +1) {
			    val = (nr-row) +1;	
			}else {
		    	val = row;	
			}
			for (int stars = 1; stars <= nst; stars++) {
				if (stars % 2 == 0) {
					System.out.print("*");
				} else {
					System.out.print(val);
				}
			}
			System.out.print("\n");

			if (row <= nr / 2) {
				nst = nst + 2;
			} else {
				nst = nst - 2;
			}
		}

	}

}
