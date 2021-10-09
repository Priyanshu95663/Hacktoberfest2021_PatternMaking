import java.util.Scanner;

class staircase_pattern{
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter number of stairs");
        int a=s.nextInt();
        for(int i=1;i<a+1;i++){
            String n=" ";
            System.out.println(n.repeat(i-1)+"_");
            System.out.println(n.repeat(i)+"|");
        }
        s.close();
    }
}