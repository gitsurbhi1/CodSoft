import java.util.Scanner;
class BankAccount{
    double balance;
    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }
    public double getBalance(){
        return balance;
    }
    public void deposit(double amount){
        if(amount>0){
            balance+=amount;
            System.out.println("Rs."+amount+" Successfully Deposited\n");
        }else{
            System.out.println("Invalid deposit amount\n");
        }
    }
    public boolean withdraw(double amount){
        if(amount>0 && amount<=balance){
            balance-=amount;
            System.out.println("Rs."+amount+" Successfully Withdrawn\n");
            System.out.println("Rs."+balance+" is the remaining balance\n");
            return true;
        }
        else if(amount<=balance){
            System.out.println("Insufficient balance\n");
        }else{
            System.out.println("Invalid withdrawn amount\n");
        }
        return false;
    }
    public void checkBalance(){
        System.out.println("Your current balance is Rs."+balance);
    }
}
public class ATMinterface {
     BankAccount account;
     Scanner scanner;

    public ATMinterface(BankAccount account) {
        this.account = account;
        this.scanner = new Scanner(System.in);
    }
    public void displayMenu() {
        while (true) {
            System.out.println("\nATM Menu:");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    account.checkBalance();
                    break;
                case 2:
                    handleDeposit();
                    break;
                case 3:
                    handleWithdraw();
                    break;
                case 4:
                    System.out.println("Thank you for using the ATM. Goodbye!");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
    private void handleDeposit() {
        System.out.print("Enter amount to deposit: ");
        double amount = scanner.nextDouble();
        account.deposit(amount);
    }

    private void handleWithdraw() {
        System.out.print("Enter amount to withdraw: ");
        double amount = scanner.nextDouble();
        account.withdraw(amount);
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000.00); // Initial balance
        ATMinterface atm = new ATMinterface(account);
        atm.displayMenu();
    }
}
