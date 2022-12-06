/**
 * assign
 */
import java.io.*;
import java.sql.Array;
import java.util.Scanner;
import java.util.regex.Pattern;  
import java.util.*;
class assign {

    static void checkTriangle(float a, float b, float c){
        // if (a<0 || b<0 || c<0 || (a+b <= c) || a+c <= b || b+c <= a) {
        //     System.out.println("Invalid inputs");
        //     System.exit(0);
        // }
        // else{
            Scanner sc = new Scanner(System.in);
            float semiPerimeter = (a+b+c)/2;
            float area=(float)Math.sqrt(semiPerimeter*(semiPerimeter-a)*(semiPerimeter-b)*(semiPerimeter-c));

            if(a == b && b ==c){
                System.out.println("This is an equilateral triangle with area of" + Float.toString(area));
                System.out.println("Would you like to enter another?");
                String answer = sc.nextLine();
                System.out.println(answer);
                if(answer.toLowerCase().equals("yes")){
                    main(null);
                }else{
                    System.exit(0);
                }
            }
            else if (a == b || b == c || a==c ) {
                System.out.println("This is an Isosceles triangle with area of" + Float.toString(area));
                System.out.println("Would you like to enter another?");
                String answer = sc.nextLine();
                if(answer.toLowerCase().equals("yes") || answer.toLowerCase().equals("y")){
                    main(null);
                }else{
                    System.exit(0);
                }
                
            } else if((a*a) + (b*b) == (c*c)){
                float area1 = (a*b)/2;
                System.out.println("This is an right angled triangle with area of " + Float.toString(area1));
                System.out.println("Would you like to enter another?");
                String answer = sc.nextLine();
                if(answer.toLowerCase().equals("yes") || answer.toLowerCase().equals("y")){
                    main(null);
                }else{
                    System.exit(0);
                }
                
            }else{
                System.out.println("Another type of Triangle");
                System.out.println("Would you like to enter another?");
                String answer = sc.nextLine();
                if(answer.toLowerCase().equals("yes") || answer.toLowerCase().equals("y")){
                    main(null);
                }else{
                    System.exit(0);
                }
            }
            
        //}
    }
    static String[] getInputs(){
        Scanner sc = new Scanner(System.in);
        Pattern ptr = Pattern.compile(" ");  
        System.out.println("What are the sides of the triagle. Place a Space between each number. ");
        String numbers=sc.nextLine();
        String[] data = ptr.split(numbers);
        return data;
    }

    public static void main(String[] args) {
       String[] data  = getInputs();
       List<Float> intList = new ArrayList<>();
       List<String> list = new ArrayList<String>(Arrays.asList(data));
       list.removeIf(Objects::isNull);
       list.removeIf(String::isEmpty);
       for(String s : list) intList.add(Float.valueOf(s));
       float a = intList.get(0);
       float b = intList.get(1);
       float c = intList.get(2);
       checkTriangle(a, b, c);
    //    System.out.println(answer);
    //     if(answer.toLowerCase()=="yes"){
    //         assign.main(args);
    //     }else{
    //         System.exit(0);
    //     }

        
    }
}