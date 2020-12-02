#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>

std::vector<int> read_from_file(std::string filename)
{
	std::fstream myfile(filename, std::ios_base::in);

	std::vector<int> numbers{};
	int a;
	while (myfile >> a)
	{
		numbers.push_back(a);
	}
	return numbers;
}

std::pair<std::size_t, std::size_t> find_sum_indices(std::vector<int> numbers, int target_sum)
{
	std::size_t left = 0;
	std::size_t right = numbers.size() - 1;

	while (left != right)
	{
		int sum = numbers[left] + numbers[right];
		if (sum == target_sum)
		{
			return {left, right};
		}
		else if (sum < target_sum)
		{
			++left;
		}
		else
		{
			--right;
		}
	}
	return {-1, -1};
}

int main(int argc, char * argv[])
{
	std::vector<int> numbers = read_from_file("./input_data.csv");
	std::sort(numbers.begin(), numbers.end());
	std::pair<std::size_t, std::size_t> sum_indices = find_sum_indices(numbers, 2020);

	std::cout << "Indices are " << sum_indices.first << " " << sum_indices.second << std::endl;
	std::cout << "Product is " << numbers[sum_indices.first] * numbers[sum_indices.second] << std::endl;

	return 0;
}
