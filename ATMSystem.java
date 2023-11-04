import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Account {
    private String accountNumber;
    private String pin;
    private double balance;

    public Account(String accountNumber, String pin, double balance) {
        this.accountNumber = accountNumber;
        this.pin = pin;
        this.balance = balance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getPin() {
        return pin;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }
}

public class ATMSystem {
    private Map<String, Account> accounts;

    public ATMSystem() {
        accounts = new HashMap<>();
    }

    public void createAccount(String accountNumber, String pin, double initialBalance) {
        Account account = new Account(accountNumber, pin, initialBalance);
        accounts.put(accountNumber, account);
    }

    public boolean validateAccount(String accountNumber, String pin) {
        if (accounts.containsKey(accountNumber)) {
            Account account = accounts.get(accountNumber);
            return account.getPin().equals(pin);
        }
        return false;
    }

    public void displayMenu() {
        System.out.println("\nATM Menu:");
        System.out.println("1. Check Balance");
        System.out.println("2. Deposit");
        System.out.println("3. Withdraw");
        System.out.println("4. Exit");
    }

    public static void main(String[] args) {
        ATMSystem atm = new ATMSystem();
        atm.createAccount("12345", "1234", 1000.0);

        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the ATM System!");
        String accountNumber, pin;
        double amount;

        do {
            System.out.print("Enter your account number: ");
            accountNumber = scanner.next();
            System.out.print("Enter your PIN: ");
            pin = scanner.next();

            if (!atm.validateAccount(accountNumber, pin)) {
                System.out.println("Invalid account number or PIN. Please try again.");
            }
        } while (!atm.validateAccount(accountNumber, pin));

        System.out.println("Login successful!\n");

        int choice;
        do {
            atm.displayMenu();
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Your balance is: $" + atm.accounts.get(accountNumber).getBalance());
                    break;
                case 2:
                    System.out.print("Enter the deposit amount: $");
                    amount = scanner.nextDouble();
                    atm.accounts.get(accountNumber).deposit(amount);
                    System.out.println("Deposit successful. Your new balance is: $" + atm.accounts.get(accountNumber).getBalance());
                    break;
                case 3:
                    System.out.print("Enter the withdrawal amount: $");
                    amount = scanner.nextDouble();
                    if (atm.accounts.get(accountNumber).withdraw(amount)) {
                        System.out.println("Withdrawal successful. Your new balance is: $" + atm.accounts.get(accountNumber).getBalance());
                    } else {
                        System.out.println("Insufficient balance.");
                    }
                    break;
                case 4:
                    System.out.println("Thank you for using the ATM. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);
    }
}
