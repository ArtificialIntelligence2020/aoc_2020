#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <string>

#include <stdio.h>


bool process_line(std::string input_line)
{
	char min_string[5], max_string[5];
	char character{};
	char password[100];

	sscanf(input_line.c_str(), "%[^-]-%[^-] %c: %s", min_string, max_string, &character, password);

	int min = atoi(min_string);
	int max = atoi(max_string);

	int char_count = 0;
	std::string password_string{password};
	for (char c : password_string) 
	{
		if (c == character)
		{
			char_count++;
		}
	}

	if (char_count >= min && char_count <= max)
	{
		return true;
	}
	return false;
}


int main() {
	std::ifstream infile("./input_data.csv");
	std::string line;

	int valid_count = 0;
	while (std::getline(infile, line))
	{
		bool ret = process_line(line);
		if (ret)
		{
			valid_count++;
		}
	}

	std::cout << valid_count;

	return 0;
}