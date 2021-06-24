#include "directedgraph.h"
#include <map>

void DirectedGraph::Add(int a, int b, double weight)
{
	graph_[a][b] = weight;

	auto iter = graph_.find(b);
	if(iter == graph_.end()) {
		graph_[b] = std::map<int, double>();
	}
}
