#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <iomanip>

#include <omp.h>

double get_random(double min, double max, unsigned *seed) {
    return (rand_r(seed) / (double) RAND_MAX) * (double) (max - min) + (double) min;
}

struct point {
    double x;
    double y;
};

point generate_random_point(point min, point max, unsigned *seed){
    double random_point_x = get_random(min.x, max.x, seed);
    double random_point_y = get_random(min.y, max.y, seed);
    return { random_point_x, random_point_y };
}

double integrator (point min, point max, bool is_under_plot, long long number_of_points) {
    long long points_in_area = 0; //counter of points that lie under graphic of function
    #pragma omp parallel default(none) shared(min, max, points_in_area, number_of_points)
    {
        #pragma omp parallel for
        for (long long i = 0; i < number_of_points; i++) { 
            unsigned int myseed = time(0);

            // point random = generate_random_point(min, max, &myseed);

            double random_point_x = (rand_r(&myseed) / (double) RAND_MAX) * (double) (max.x - min.x) + (double) min.x;
            double random_point_y = (rand_r(&myseed) / (double) RAND_MAX) * (double) (max.y - min.y) + (double) min.y;
            point random = { random_point_x, random_point_y };

            if (random.y <= random.x)
                points_in_area ++;
        }
    }

    long long points_out_of_area = number_of_points - points_in_area; //counter of point that lie over graphic of function

    double square_of_area = (max.x - min.x) * (max.y - min.y); //area of area in which method 
    if (is_under_plot) {                                                          //has been applied
        double square_under = square_of_area * 
            ((number_of_points - points_in_area) / (double) number_of_points); //area under the graphic of function
        return square_under;
    } else {
        double square_over = square_of_area * 
            ((number_of_points - points_out_of_area) / (double) number_of_points); // area of area over 
        return square_over;
    }
}

int main () {
    unsigned int seed = time(nullptr);
    std::srand(seed);

    std::cout << "seed = " << seed << "\n";

    point min;

    std::cout << "min.x = ";
    std::cin >> min.x;
    std::cout << "min.y = ";
    std::cin >> min.y;

    point max;

    std::cout << "max.x = ";
    std::cin >> max.x;
    std::cout << "max.y = ";
    std::cin >> max.y;

    std::cout << "number_of_points = ";

    long long number_of_points;
    std::cin >> number_of_points;

    std::cout << "If you want to know area under the graphic of function press \"Enter\",\n"
        "    otherwise write: \"over\": ";

    std::string word;
    getline(std::cin, word); // Skip line
    getline(std::cin, word);

    bool is_under_plot = true;
    if (word == "over") {
        std::cout << "selected mode = over\n";
        is_under_plot = false;
    } else {
        std::cout << "selected mode = under\n";
    }

    std::cout.flush();

    double result = integrator(min, max, is_under_plot, number_of_points);
    std::cout << std::endl;

    std::cout << "result = " << std::setprecision(30) << result << "\n";
}
