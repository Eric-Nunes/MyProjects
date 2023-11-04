#include <stdio.h>
#include <string.h>

#define MAX_ACCOUNTS 100

// Structure to represent a bank account
struct Account {
    char name[50];
    int accountNumber;
    float balance;
    char password[50];
};

// Function to create a new account
int createAccount(struct Account accounts[], int numAccounts) {
    if (numAccounts >= MAX_ACCOUNTS) {
        printf("Maximum number of accounts reached.\n");
        return numAccounts;
    }

    struct Account newAccount;
    printf("Enter your name: ");
    scanf("%s", newAccount.name);
    printf("Enter a password: ");
    scanf("%s", newAccount.password);
    newAccount.accountNumber = numAccounts + 1; // Assign a unique account number
    newAccount.balance = 0.0;

    accounts[numAccounts] = newAccount;
    printf("Account created successfully. Your account number is: %d\n", newAccount.accountNumber);

    return numAccounts + 1;
}

// Function to log in to an account
int login(struct Account accounts[], int numAccounts, int* loggedInAccount) {
    int accountNumber;
    char password[50];
    printf("Enter your account number: ");
    scanf("%d", &accountNumber);
    printf("Enter your password: ");
    scanf("%s", password);

    for (int i = 0; i < numAccounts; i++) {
        if (accounts[i].accountNumber == accountNumber && strcmp(accounts[i].password, password) == 0) {
            *loggedInAccount = i;
            printf("Login successful. Welcome, %s!\n", accounts[i].name);
            return 1;
        }
    }

    printf("Login failed. Invalid account number or password.\n");
    return 0;
}

// Function to check the account balance
void checkBalance(struct Account accounts[], int loggedInAccount) {
    printf("Account Balance for %s (Account Number %d): $%.2f\n", accounts[loggedInAccount].name,
           accounts[loggedInAccount].accountNumber, accounts[loggedInAccount].balance);
}

// Function to transfer money to another account
void transferMoney(struct Account accounts[], int numAccounts, int loggedInAccount) {
    int recipientAccount;
    float amount;
    printf("Enter the recipient's account number: ");
    scanf("%d", &recipientAccount);

    if (recipientAccount <= 0 || recipientAccount > numAccounts || recipientAccount == accounts[loggedInAccount].accountNumber) {
        printf("Invalid recipient account number.\n");
        return;
    }

    printf("Enter the amount to transfer: $");
    scanf("%f", &amount);

    if (amount <= 0 || amount > accounts[loggedInAccount].balance) {
        printf("Invalid amount or insufficient balance.\n");
        return;
    }

    accounts[loggedInAccount].balance -= amount;
    accounts[recipientAccount - 1].balance += amount;
    printf("Money transferred successfully.\n");
}

int main() {
    struct Account accounts[MAX_ACCOUNTS];
    int numAccounts = 0;
    int loggedInAccount = -1; // Represents the index of the logged-in account

    while (1) {
        int choice;

        if (loggedInAccount != -1) {
            printf("\nWelcome, %s!\n", accounts[loggedInAccount].name);
            printf("1. Check Account Balance\n");
            printf("2. Transfer Money\n");
            printf("3. Logout\n");
            printf("Enter your choice: ");
            scanf("%d", &choice);

            if (choice == 1) {
                checkBalance(accounts, loggedInAccount);
            } else if (choice == 2) {
                transferMoney(accounts, numAccounts, loggedInAccount);
            } else if (choice == 3) {
                loggedInAccount = -1; // Logout
            } else {
                printf("Invalid choice.\n");
            }
        } else {
            printf("\n1. Create Account\n");
            printf("2. Login\n");
            printf("3. Exit\n");
            printf("Enter your choice: ");
            scanf("%d", &choice);

            if (choice == 1) {
                numAccounts = createAccount(accounts, numAccounts);
            } else if (choice == 2) {
                loggedInAccount = -1; // Ensure logged out before attempting login
                loggedInAccount = login(accounts, numAccounts, &loggedInAccount);
            } else if (choice == 3) {
                printf("Thank you for using the bank management system. Goodbye!\n");
                break;
            } else {
                printf("Invalid choice.\n");
            }
        }
    }

    return 0;
}
