#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int playerChoice, computerChoice;

    // Seed the random number generator
    srand(time(0));

    // Generate a random number (0 for Rock, 1 for Paper, 2 for Scissors)
    computerChoice = rand() % 3;

    printf("Welcome to Rock, Paper, Scissors!\n");
    printf("Choose your move:\n");
    printf("0 - Rock\n");
    printf("1 - Paper\n");
    printf("2 - Scissors\n");

    // Get the player's choice
    scanf("%d", &playerChoice);

    if (playerChoice < 0 || playerChoice > 2) {
        printf("Invalid choice. Please choose 0, 1, or 2.\n");
    } else {
        printf("You chose: ");
        switch (playerChoice) {
            case 0:
                printf("Rock\n");
                break;
            case 1:
                printf("Paper\n");
                break;
            case 2:
                printf("Scissors\n");
                break;
        }

        printf("Computer chose: ");
        switch (computerChoice) {
            case 0:
                printf("Rock\n");
                break;
            case 1:
                printf("Paper\n");
                break;
            case 2:
                printf("Scissors\n");
                break;
        }

        // Determine the winner
        if (playerChoice == computerChoice) {
            printf("It's a tie!\n");
        } else if ((playerChoice == 0 && computerChoice == 2) || (playerChoice == 1 && computerChoice == 0) || (playerChoice == 2 && computerChoice == 1)) {
            printf("You win!\n");
        } else {
            printf("Computer wins!\n");
        }
    }

    return 0;
}
