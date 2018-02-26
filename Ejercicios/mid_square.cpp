#include <iostream>

int main () {
	
	unsigned long long int x;
	while(std::cin >> x) {
		x *= x;
		std::cout << x << std::endl;
	}
	return 0;
}	