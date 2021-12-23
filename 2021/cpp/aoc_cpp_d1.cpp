#include <iostream>
#include <fstream>
#include <string>

void part_one()
{
	std::ifstream input("d1.txt");
	std::string   line;
	
	getline(input, line);
	int prev_x = std::stoi(line);
	
	int total = 0;
	
	while (getline(input, line))
	{
		int this_x = std::stoi(line);
		
		total += this_x > prev_x ? 1 : 0;
		
		prev_x = this_x;
	}
	
	input.close();
	
	std::cout << "Part 1 answer = " << total << '\n';
}

void part_two()
{
	std::ifstream input("d1.txt");
	std::string   line;
	
	getline(input, line);
	int x_i0 = std::stoi(line);
	
	getline(input, line);
	int x_i1 = std::stoi(line);
	
	getline(input, line);
	int x_i2 = std::stoi(line);
	
	int total = 0;
	
	while (getline(input, line))
	{
		int x_i3 = std::stoi(line);
		
		total += x_i3 > x_i0 ? 1 : 0;
		
		x_i0 = x_i1;
		x_i1 = x_i2;
		x_i2 = x_i3;
	}
	
	input.close();
	
	std::cout << "Part 2 answer = " << total << '\n';
}


int main() {
	
	part_one();
	
	part_two();
	
	return 0;
}
