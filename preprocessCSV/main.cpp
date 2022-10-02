#include <iostream>
#include <sstream>
#include <istream>
#include <ostream>
#include <fstream>
#include <vector>

using namespace std;

template< char C >
std::istream& sep( std::istream& in )
{   // reads separator 'C'
    char c;
    if( in >> c && c != C )
        in.setstate( std::ios_base::failbit );
    return in;
}

int main() {

    ifstream infile("labeled_data.csv");
    vector<string> tweetData;
    string line;
    vector<string> fData;
    while (getline(infile, line))
    {
        string tempL = "";
        for (int i = 0; i < line.length(); i++){
            if (line[i] != ',' && i != line.length()-1 ){
                tempL = tempL + line[i];
            }
            else {
                tweetData.push_back(tempL);
                tempL = "";
            }
        }
//        tweetData.push_back(line); //Get each line of the file as a string
    }

    for (int i = 0; i < 5; i ++){
//        cout << endl;
        cout << tweetData[i] << endl;
        cout << endl;
    }

    for (int i = 0; i < tweetData.size(); i ++){
        string temp = "";
        for (int j = 0; j < tweetData[i].size(); ++j) {
            if (isdigit(tweetData[i][j]) || tweetData[i][j] == '?' || tweetData[i][j] == '!' || tweetData[i][j] == '%' || tweetData[i][j] == '-'  || tweetData[i][j] == '#'  || tweetData[i][j] == '@'  || tweetData[i][j] == '+'  || tweetData[i][j] == '{' || tweetData[i][j] == '}' || tweetData[i][j] == '`' || tweetData[i][j] == ',' || tweetData[i][j] == '.' || tweetData[i][j] == '\'' || tweetData[i][j] == '\"' || tweetData[i][j] == '\\' ){
                continue;
            }
            if ((tweetData[i][j] >= 'a' && tweetData[i][j] <= 'z') || (tweetData[i][j] >= 'A' && tweetData[i][j] <= 'Z' )|| tweetData[i][j] >= ' ') {
                temp = temp + tweetData[i][j];
            }
        }
//        cout << temp << endl;
        transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
        fData.push_back(temp);
        tweetData[i] = temp;
    }

    for (int i = 0; i < fData.size(); i ++){
//        cout << endl;
        cout << fData[i] << endl;
        cout << endl;
    }

    fstream my_file;
    my_file.open("tweetfile2.csv", ios::out);

    if (!my_file) {
        cout << "File not created!";
    }
    else {
        cout << "File created successfully!";
        for (int i = 0; i < fData.size(); i ++){

            if (i%2 == 1) {
                my_file << fData[i];
                my_file << endl;
                cout << fData[i] << endl;
            }
            if (i%2 == 0){
                my_file << fData[i];
                my_file << ",";
                cout << fData[i] << ",";
//                cout << endl;
            }
        }
        my_file.close();
    }
    return 0;
}
