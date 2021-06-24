#include "directedgraph.h"
#include "shortestpath.h"

#include <iostream>
#include <fstream>

void trim(std::string &s)
{
    if (s.empty()) {
	    return;
    }

    s.erase(0,s.find_first_not_of(" "));
    s.erase(s.find_last_not_of(" ") + 1);
}

void split(const std::string& s, std::vector<std::string>& v, const std::string& c)
{
    size_t len = s.length();

    std::string::size_type pos1, pos2;
    pos2 = s.find(c);
    pos1 = 0;

    while(std::string::npos != pos2) {
        v.emplace_back(s.substr(pos1, pos2-pos1));

        pos1 = pos2 + c.size();
        pos2 = s.find(c, pos1);
    }

    if(pos1 != len) {
        v.emplace_back(s.substr(pos1));
    }
}

void initGraph(DirectedGraph * graph, const std::string & graphStr)
{
	std::vector<std::string> tokens;
	split(graphStr, tokens, ",");

	for(auto & v : tokens) {
		trim(v);
		if(v.empty() || v.length() < 3) {
			continue;
		}
		int a = v[0];
		int b = v[1];
		double w = atof(v.c_str()+2);
		//std::cout << v << (char)a << (char)b  << w << std::endl;
		graph->Add(a, b, w);
	}
}

void testRouteExist(DirectedGraph * graph, const std::vector<int> & route)
{
	double dist;
	bool exist = graph->IsExist(route, &dist);
	if(exist) {
	} else {
		std::count << "NO SUCH ROUTE" << std::endl;
	}
}

void testCase1(DirectedGraph * graph)
{
	std::vector<int> route;
	route.push_back('A');
	route.push_back('B');
	route.push_back('C');

	testRouteExist(graph, route);
}

void testCase2(DirectedGraph * graph)
{
}

void testCase3(DirectedGraph * graph)
{
}

void testCase4(DirectedGraph * graph)
{
}

void testCase5(DirectedGraph * graph)
{
}

void testCase6(DirectedGraph * graph)
{
}

int main(int argc, const char * argv[]) 
{
	std::string graphStr = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7";
	if(argc > 1) {
		std::ifstream f(argv[1]);
		std::string tmp;
		std::getline(f, tmp);
		graphStr = tmp;
	}

	DirectedGraph graph;
	initGraph(&graph, graphStr);

	ShortestPath sp(&graph);

	testCase1(&graph);
	testCase2(&graph);
	testCase3(&graph);
	testCase4(&graph);
	testCase5(&graph);
	testCase6(&graph);

	std::cout << "hello " << std::endl;
}
