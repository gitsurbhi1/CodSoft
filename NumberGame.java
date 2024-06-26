import java.util.Random;
import java.util.Scanner;
public class NumberGame{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int no_of_guesses=0;
        int no_of_rounds_won=0;
        int no_of_rounds_played=0;
        System.out.println("! WELCOME TO THE NUMBER GUSSING GAME !\nYou have to guess the number in 10 chances to win the round");
        while(true){
            no_of_rounds_played++;
            Random random = new Random();
            int computerNumber = random.nextInt(100)+1;
            while(true){
                 System.out.println("Guess a number from 1 to 100");
            int yourGuessedNumber=sc.nextInt();
                no_of_guesses++;
                    if(computerNumber==yourGuessedNumber){
                        System.out.println("Hurray! You guessed it right in "+ no_of_guesses+"guesses.\n");
                        System.out.println("You won the round "+no_of_rounds_played);
                        no_of_rounds_won++;
                        break;
                    }else if(computerNumber>yourGuessedNumber&&no_of_guesses<10){
                        System.out.println("Oops! Too low.\nTry to guess high.\n");
                    }else if(computerNumber<yourGuessedNumber&&no_of_guesses<10){
                        System.out.println("Oops! Too high.\nTry to guess low.\n");
                    }else{
                        System.out.println("! GAME OVER !\n");
                        break;
                    }
            }
            System.out.println("Enter 1 for another round otherwise 0\n");
            int r=sc.nextInt();
            if(r==0){
                break;
            }
        }
        System.out.println("You won "+no_of_rounds_won+"rounds out of "+ no_of_rounds_played);
    }
}