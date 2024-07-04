import java.util.Scanner;
public class StudentGradeCalculator {
    public static void main(String[] args){
        double totalMarks=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the total number of subjects");
        int numberOfSubjects = sc.nextInt();
        double[] marksArray = new double[numberOfSubjects];
        System.out.println("Enter the number obtained in each subjects out of 100");
        for(int i=0; i<numberOfSubjects; i++){
            double marks;
            while (true) {
                System.out.print("Enter marks for subject " + (i + 1) + ": ");
                marks = sc.nextDouble();
                if (marks >= 0 && marks <= 100) {
                    break;
                }else{
                    System.out.println("Invalid input. Please enter marks between 0 and 100.");
                }
            }
            marksArray[i] = marks;
        }
        for(double a:marksArray){
            totalMarks+=a;
        }
        System.out.println("\nYour total marks = " + totalMarks);
        double avgPercentage = totalMarks/numberOfSubjects;
        System.out.printf("Your average percentage = %.2f\n",avgPercentage);
        System.out.println("Your grade and remark based on your percentage is : ");
        if(avgPercentage>95){
            System.out.println("GRADE : A+ \nREMARK : EXCELLENT");
        }else if(avgPercentage>90){
            System.out.println("GRADE : A \nREMARK : VERY GOOD");
        }else if(avgPercentage>85){
            System.out.println("GRADE : B+ \nREMARK : GOOD");
        }else if(avgPercentage>80){
            System.out.println("GRADE : B \nREMARK : AVERAGE");
        }else if(avgPercentage>70){
            System.out.println("GRADE : C \nREMARK : NEED IMPROVEMENT");
        }else if(avgPercentage>60){
            System.out.println("GRADE : D \nREMARK : PASS");
        }else{
            System.out.println("GRADE : E \nREMARK : FAIL");
        }
    }
}
