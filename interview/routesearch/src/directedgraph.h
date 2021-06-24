#ifndef _DIRECTED_GRAPH_
#define _DIRECTED_GRAPH_

#include <map>
#include <vector>

class ShortestPath;

class DirectedGraph 
{
	public:
		//增加一条边
		void Add(int f, int t, double weight);

		//判断是否存在A-B-C类似的精确的路径以及总距离
		//ourDist为返回的距离
		bool IsExist(const std::vector<int> & route, double * outDist) const;

		//找到不超过N跳的A到B的路径
		// outRoutes为符合条件的所有的路径，route不包含A
		void FindRoutesByStops(int a, int b, int maxStops, 
				std::vector<std::vector<int>> * outRoutes) const;

		//找到不超过距离M的A到B的路径
		// outRoutes为符合条件的所有的路径，route不包含A
		void FindRoutesByDistance(int a, int b, double maxDist, 
				std::vector<std::vector<int>> * outRoutes) const;

	private:
		friend ShortestPath;

		//顶点以及从顶点出发的边
		std::map<int, std::map<int, double>> graph_;
};

#endif
