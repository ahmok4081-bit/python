gcc --version
#include <stdio.h>

int main() {
    int age;
    char gender;

    // Prompt the user to enter age and gender
    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Enter your gender (M/F): ");
    scanf(" %c", &gender);

    // Check eligibility based on age and gender
    if (age >= 18) {
        if (gender == 'M') {
            printf("You are eligible for military service.\n");
        }
        else if (gender == 'F') {
            printf("You are eligible for voluntary military service.\n");
        }
        else {
            printf("Invalid gender input.\n");
        }
    }
    else {
        printf("You are not eligible for military service.\n");
    }

    return 0;
}
