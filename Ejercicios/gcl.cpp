#include <iostream>
#include <map>

int main () {
	int m, a, c, z;
	double r;
	std::cin >> m >> a >> c >> z;
	std::map<double, bool> seen;
	for (int i = 1; ; i ++) {
		z = ((a * z) + c) % m;
		r = (double) z / m;
		if (seen.find(r) == seen.end()) {
			seen[r] = true;
			std::cout << i << ".- r: " << r << " z: " << z << std::endl;
		}
		else break;
	}
	return 0;
}