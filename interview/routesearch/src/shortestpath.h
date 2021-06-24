#ifndef _SHORTEST_PATH_
#define _SHORTEST_PATH_

#include <vector>
#include <map>

class DirectedGraph;

class ShortestPath
{
	public:
		ShortestPath(const DirectedGraph * graph);

		//A-B的最小路径，A和B可以相同
		// outRoute是输出的路径, 不包含a，但是包含b（如果存在到b的路径）
		// outDist是输出的距离
		void FindSP(int a, int b, std::vector<int> * outRoute, double * outDist);

	private:
		//每个顶点的最小路径树
		std::map<int, std::map<int, std::pair<int, double>>> vertexes_;
};

#endif
