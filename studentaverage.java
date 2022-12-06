import java.util.*;
import java.io.File;
import java.util.regex.Pattern;  

public class studentaverage {
    static Double getAverage(String[] mydata){
        String[] str_array = mydata;
        List<Float> intList = new ArrayList<>();
        List<String> list = new ArrayList<String>(Arrays.asList(str_array));
        list.removeIf(Objects::isNull);
        list.removeIf(String::isEmpty);
        list.remove(0);
        list.remove(0);
        list.remove("-999");
        for(String s : list) intList.add(Float.valueOf(s));
        double sum = 0;
        for(Float d : intList)
            sum += d;
        double average = (sum/intList.size());
        return average;
                    
        
    }
    public static void main(String[] args) throws Exception {
        List<String> data = new ArrayList<String>();
        File file = new File("data.txt");
        Pattern ptr = Pattern.compile(" ");  
        Scanner sc = new Scanner(file);
        while (sc.hasNextLine()){
         data.add(sc.nextLine());
        }
        
        String Student1 = data.get(0);
        String[] CIS110s1 = ptr.split((data.get(1)));
        String[] ENG111s1= ptr.split(data.get(2));
        String[] MTH141s1 = ptr.split(data.get(3));
        String[] CHM121s1= ptr.split(data.get(4));
        double CIS110s1ave = getAverage(CIS110s1);
        double ENG111s1ave = getAverage(ENG111s1);
        double MTH141s1ave = getAverage(MTH141s1);
        double CHM121s1ave = getAverage(CHM121s1);
        String[] Student2 = ptr.split(data.get(5));
        String[] CIS110s2 = ptr.split(data.get(6));
        String[] ENG111s2 = ptr.split(data.get(7));
        String[] MTH141s2 = ptr.split(data.get(8));
        String[] CHM121s2 = ptr.split(data.get(9));
        double CIS110s2ave = getAverage(CIS110s2);
        double ENG111s2ave = getAverage(ENG111s2);
        double MTH141s2ave = getAverage(MTH141s2);
        double CHM121s2ave = getAverage(CHM121s2);
        
        double aveStudent1=((CIS110s1ave+ENG111s1ave+MTH141s1ave+CHM121s1ave)/4);
        double aveStudent2=((CHM121s2ave+ENG111s2ave+MTH141s2ave+CHM121s2ave)/4);


        System.out.println("CourseID Student# Course Average");
        System.out.println("CIS 110     1      "+CIS110s1ave+" ");
        System.out.println("            2      "+CIS110s2ave+" ");
        System.out.println("ENG 111     1      "+ENG111s1ave+" ");
        System.out.println("            2      "+ENG111s2ave+" ");
        System.out.println("MTH 141     1      "+MTH141s1ave+" ");
        System.out.println("            2      "+MTH141s2ave+" ");
        System.out.println("CHM 121     1      "+CHM121s1ave+" ");
        System.out.println("            2      "+CHM121s2ave+" ");
        System.out.println("Average for student 1: "+ Double.toString(aveStudent1));
        System.out.println("Average for student 2: "+ Double.toString(aveStudent2));
        System.out.println("     0   10    20     30    40   50     60    70     80    90   100");
        System.out.println("     |----|-----|-----|-----|-----|-----|-----|------|-----|-----|");
        System.out.println("CIS  ************************************************");
        System.out.println("     #######################################");
        System.out.println("ENG  ********************************************");
        System.out.println("     ####################################################");
        System.out.println("MTH  *****************************************************");
        System.out.println("     #################################################");
        System.out.println("CHM  ********************************************");
        System.out.println("     ########################################################");




       
       
    }
}
