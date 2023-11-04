#include <stdio.h>
#include <stdlib.h>

// Function to convert decimal to binary
void decimalToBinary(int decimal) {
    int binary[32];
    int i = 0;
    
    while (decimal > 0) {
        binary[i] = decimal % 2;
        decimal /= 2;
        i++;
    }

    printf("Binary: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary[j]);
    }
    printf("\n");
}

// Function to convert binary to decimal
void binaryToDecimal(char* binary) {
    int decimal = strtol(binary, NULL, 2);
    printf("Decimal: %d\n", decimal);
}

// Function to convert decimal to octal
void decimalToOctal(int decimal) {
    int octal[32];
    int i = 0;

    while (decimal > 0) {
        octal[i] = decimal % 8;
        decimal /= 8;
        i++;
    }

    printf("Octal: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", octal[j]);
    }
    printf("\n");
}

// Function to convert octal to decimal
void octalToDecimal(char* octal) {
    int decimal = strtol(octal, NULL, 8);
    printf("Decimal: %d\n", decimal);
}

// Function to convert hexadecimal to binary
void hexadecimalToBinary(char* hexadecimal) {
    char binary[32];
    int i = 0;
    int j = 0;

    while (hexadecimal[i]) {
        switch (hexadecimal[i]) {
            case '0':
                binary[j] = '0'; break;
            case '1':
                binary[j] = '1'; break;
            case '2':
                binary[j] = '10'; break;
            case '3':
                binary[j] = '11'; break;
            case '4':
                binary[j] = '100'; break;
            case '5':
                binary[j] = '101'; break;
            case '6':
                binary[j] = '110'; break;
            case '7':
                binary[j] = '111'; break;
            case '8':
                binary[j] = '1000'; break;
            case '9':
                binary[j] = '1001'; break;
            case 'A':
            case 'a':
                binary[j] = '1010'; break;
            case 'B':
            case 'b':
                binary[j] = '1011'; break;
            case 'C':
            case 'c':
                binary[j] = '1100'; break;
            case 'D':
            case 'd':
                binary[j] = '1101'; break;
            case 'E':
            case 'e':
                binary[j] = '1110'; break;
            case 'F':
            case 'f':
                binary[j] = '1111'; break;
        }
        i++;
        j += 4;
    }

    binary[j] = '\0';
    printf("Binary: %s\n", binary);
}

// Function to convert binary to hexadecimal
void binaryToHexadecimal(char* binary) {
    char hexadecimal[32];
    int i = 0;
    int j = 0;

    while (binary[i]) {
        int nibble = 0;
        for (int k = 0; k < 4; k++) {
            nibble = (nibble << 1) | (binary[i] - '0');
            i++;
        }

        switch (nibble) {
            case 0:
                hexadecimal[j] = '0'; break;
            case 1:
                hexadecimal[j] = '1'; break;
            case 2:
                hexadecimal[j] = '2'; break;
            case 3:
                hexadecimal[j] = '3'; break;
            case 4:
                hexadecimal[j] = '4'; break;
            case 5:
                hexadecimal[j] = '5'; break;
            case 6:
                hexadecimal[j] = '6'; break;
            case 7:
                hexadecimal[j] = '7'; break;
            case 8:
                hexadecimal[j] = '8'; break;
            case 9:
                hexadecimal[j] = '9'; break;
            case 10:
                hexadecimal[j] = 'A'; break;
            case 11:
                hexadecimal[j] = 'B'; break;
            case 12:
                hexadecimal[j] = 'C'; break;
            case 13:
                hexadecimal[j] = 'D'; break;
            case 14:
                hexadecimal[j] = 'E
