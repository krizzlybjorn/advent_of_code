#include <ios>
#include <iostream>
#include <fstream>
#include <ostream>
#include <string>
#include <vector>
#include <cmath>

// g++ solve_day_03_B.cpp -o solve_day_03_B

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

// store all values in a vector so they can be examined more than once
std::vector<std::string> get_input() {
    std::fstream inputfile;
    inputfile.open("input_day_3",std::ios::in);
    std::string line;
    std::vector<std::string> input_vector;
    while(std::getline(inputfile, line)){
        input_vector.push_back(line);
    }
    return input_vector;
}

int main() {
    int numberOfZero = 0;
    int numberOfOnes = 0;

    std::vector<std::string> input_data = get_input();
    std::vector<std::string> storage_vector;
    copy(input_data.begin(), input_data.end(), back_inserter(storage_vector));
    std::vector<int> indexWith1;
    std::vector<int> indexWith0;

    int stringIndex = 0;
    bool loopControl = true;

    int retVal1;
    int retVal2;

    while(loopControl){
        numberOfZero = 0;
        numberOfOnes = 0;
        indexWith1.clear();
        indexWith0.clear();
        for (int i = 0; i < input_data.size(); i++) {
            if (input_data[i][stringIndex] == '1'){
                numberOfOnes++;
                indexWith1.push_back(i);
            } else {
                numberOfZero++;
                indexWith0.push_back(i);
            }
        }
        std::cout << "Size: " << input_data.size() << std::endl;

        if (numberOfOnes >= numberOfZero){
            while (indexWith0.size() >= 1) {
                input_data.erase(input_data.begin() + indexWith0.back());
                indexWith0.pop_back();
            }
        } else {
            while (indexWith1.size() >= 1) {
                input_data.erase(input_data.begin() + indexWith1.back());
                indexWith1.pop_back();
            }
        }
        if (input_data.size() == 1){
            loopControl = false;
        } else {
            stringIndex++;
        }
    }

    std::cout << "Number: " << input_data[0] << std::endl;

    std::vector<int> temp_Vector;
    for (int i = 0; i < input_data[0].size(); i++) {
        if (input_data[0][i] == '0'){
            temp_Vector.push_back(0);
        } else {
            temp_Vector.push_back(1);
        }
    }

    retVal1 = binaryVectorToInt(temp_Vector);

    std::cout << "Number: " << retVal1 << std::endl;

    // Next number

    input_data.clear();
    copy(storage_vector.begin(), storage_vector.end(), back_inserter(input_data));
    stringIndex = 0;
    loopControl = true;

    while(loopControl){
        numberOfZero = 0;
        numberOfOnes = 0;
        indexWith1.clear();
        indexWith0.clear();
        for (int i = 0; i < input_data.size(); i++) {
            if (input_data[i][stringIndex] == '1'){
                numberOfOnes++;
                indexWith1.push_back(i);
            } else {
                numberOfZero++;
                indexWith0.push_back(i);
            }
        }

        std::cout << "Size: " << input_data.size() << std::endl;

        if (numberOfOnes >= numberOfZero){
            while (indexWith1.size() >= 1) {
                input_data.erase(input_data.begin() + indexWith1.back());
                indexWith1.pop_back();
            }
        } else {
            while (indexWith0.size() >= 1) {
                input_data.erase(input_data.begin() + indexWith0.back());
                indexWith0.pop_back();
            }
        }
        if (input_data.size() == 1){
            loopControl = false;
        } else {
            stringIndex++;
        }
    }

    std::cout << "Number: " << input_data[0] << std::endl;

    temp_Vector.clear();
    for (int i = 0; i < input_data[0].size(); i++) {
        if (input_data[0][i] == '0'){
            temp_Vector.push_back(0);
        } else {
            temp_Vector.push_back(1);
        }
    }

    retVal2 = binaryVectorToInt(temp_Vector);

    std::cout << "Number: " << retVal2 << std::endl;

    std::cout << "Solution: " << retVal1*retVal2 << std::endl;

    return 0;
}

int not_main() {

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