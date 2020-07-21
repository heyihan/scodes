#ifndef _STUDY_ALG_H_HELPER_
#define _STUDY_ALG_H_HELPER_

#include <iostream>
#include <ctime>

class ProcessTime 
{
    public:
        ProcessTime() 
        {
            clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &lastTime_);
        }

        int64_t elapsedNs(bool renew = false)
        {
            timespec now;
            clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &now);

            if(renew)
            {
                lastTime_ = now;
            }

            return (now.tv_sec-lastTime_.tv_sec)*1e9 
                + (now.tv_nsec-lastTime_.tv_nsec);
        }

    private:
        timespec lastTime_;
};

typedef void (*func)();

void runOnce(const std::string & title, func f)
{
    f();
}

template<typename T>
std::ostream & operator<<(std::ostream & os, const std::vector<T> & elems)
{
    bool first = true;

    os << '[';
    for(auto &e : elems)
    {
        if(!first) 
        {
            os << ',';
        }
        os << e;
        first = false;
    }
    os << ']' << std::endl;

    return os;
}

#endif


