#include <ios>
#include <iostream>
#include <fstream>
#include <ostream>
#include <string>
#include <vector>
#include <cmath>

// g++ solve_day_03.cpp -o solve_day_03

// very dumb, but hey, it works
int binaryVectorToInt(std::vector<int> vector) {
    int power = std::pow(2,vector.size()-1);
    int returnInt = 0;
    for (int i = 0; i < vector.size(); i++){
        if (vector[i] == 1) {
            returnInt += power;
        }
        power = power/2;
    }
    return returnInt;
}

int main() {

    //    cout<<"fyi: "<<lastTriangleNumber(rows)<<endl;
    //    cout<<"also: " << lengthOfInt(lastTriangleNumber(rows)) << endl;

    std::fstream inputfile;
    inputfile.open("input_day_3",std::ios::in);
    std::string line;
    bool doOnce = true;
    std::vector<int> vectorOne(12, 0);
    std::vector<int> vectorZero(12, 0);
    std::vector<int> vectorFinal(12, 0);
    std::vector<int> vectorFinalInverted(12, 0);
    while(std::getline(inputfile, line)){
        int lengthOfString = line.length();
        if (doOnce){
            std::vector<int> vectorOne(lengthOfString, 0);
            std::vector<int> vectorZero(lengthOfString, 0);
            std::vector<int> vectorFinal(lengthOfString, 0);
            std::vector<int> vectorFinalInverted(lengthOfString, 0);
            doOnce = false;
        }
        for (int i = 0; i < lengthOfString; i++ ){
            switch (line[i]) {
            case ('0'):
                vectorZero[i]++;
                break;
            case ('1'):
                vectorOne[i]++;
            }
        }
    }
    inputfile.close();

    for (int i = 0; i < vectorFinal.size(); i++){
        if (vectorOne[i] > vectorZero[i]) {
            vectorFinal[i] = 1;
            vectorFinalInverted[i] = 0;
        } else {
            vectorFinal[i] = 0;
            vectorFinalInverted[i] = 1;
        }
    }

    for (int i = 0; i < vectorFinal.size(); i++){
        std::cout << vectorFinal.at(i);
    }
    std::cout << std::endl;

    for (int i = 0; i < vectorFinalInverted.size(); i++){
        std::cout << vectorFinalInverted.at(i);
    }
    std::cout << std::endl;

    int solution_A = binaryVectorToInt(vectorFinal) * binaryVectorToInt(vectorFinalInverted);

    std::cout << solution_A << std::endl;

    return 0;
}