#include <iostream>
#include <vector>
#include "helper.h"

typedef int (*sortfunc)(std::vector<int> &);

void runSort(
        const std::string & name, 
        std::vector<int> input,
        sortfunc f)
{
    auto copy = input;
    ProcessTime t;
    auto cnt = f(copy);
    auto durNs = t.elapsedNs();

    std::cout << name << " count:" << cnt << " dur:" << durNs << "ns";
    std::cout << " input:" << input;
    std::cout << " result:" << copy;
    std::cout << std::endl;
}

int insertSort(std::vector<int> & elems)
{
    int len = elems.size();
    if(len <= 1)
    {
        return 1;
    }

    int cnt = 0;
    for(int i = 1; i < len; i++)
    {
        auto tmp = elems[i];
        int j = i-1;
        while(j >= 0)
        {
            if(tmp >= elems[j]) //don't use elems[i]
            {
                break;
            }
            elems[j+1] = elems[j];
            j--;
        }
        elems[j+1] = tmp;
        cnt += i-j;
    }

    return cnt;
}

void mergeTwoSlice(std::vector<int> & elems, 
        int start, int firstLen, int secondLen)
{
    std::vector<int> tmp(firstLen + secondLen);

    std::copy(tmp.begin(), tmp.end(), elems.begin()+start);
}

int mergeSort(std::vector<int> & elems, int start, int len)
{
    if((start < 0) || (len <= 0) || ((start+len) > (int)elems.size())) 
    {
        return 0;
    }
    if(len == 1) 
    {
        return 1;
    }
    if(len == 2)
    {
        if(elems[start] > elems[start+1])
        {
            auto tmp = elems[start+1];
            elems[start+1] = elems[start];
            elems[start] = tmp;
        }
        return 1;
    }

    int cnt = mergeSort(elems, start, len/2)
        + mergeSort(elems, start + len/2, len - len/2)
        + len;
    mergeTwoSlice(elems, start, len/2, len - len/2);

    return cnt;
}

int mergeSort(std::vector<int> & elems)
{
    return mergeSort(elems, 0, elems.size());
}

int main() 
{
    std::vector<int> d1 = {
        3,6,5,4,3,9,12,31,32,45,
        7,1,23,21,50,2,60,33,8,24,
        25,26};
    runSort("insertion-sort", d1, insertSort);
    runSort("merge-sort", d1, mergeSort);

}





