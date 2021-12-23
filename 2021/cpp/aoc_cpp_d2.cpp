#include <iostream>
#include <fstream>
#include <string>

void solve()
{
	std::ifstream input("d2.txt");
	std::string   line;
	
	int frwrd    = 0;
	int depth_p1 = 0;
	int depth_p2 = 0;
	
	while (getline(input, line))
	{
		std::string instruction = line.substr(0, line.find(" "));
		std::string delta_val   = line.substr(line.find(" ")+1, line.length());
		
		int delta_int = std::stoi(delta_val);
		
		if (instruction == "forward")
		{
			frwrd    += delta_int;
			depth_p2 += depth_p1 * delta_int;
		}
		else
		{
			depth_p1 += instruction == "down" ? delta_int : -delta_int;
		}
	}
	
	input.close();
	
	std::cout << depth_p1 * frwrd << '\n';
	std::cout << depth_p2 * frwrd << '\n';
}


int main() {
	
	solve();
	
	return 0;
}