#include <iostream>
#include <memory>
#include <string>

namespace data_structures
{
    namespace linked_list
    {
        bool isDigit(const std::string &s)
        {
            for (char i : s)
            {
                if (!isdigit(i))
                {
                    return false;
                }
            }
            return true;
        }

        class link
        {
        private:
            int pvalue;
            std::shared_ptr<link> pnext;

        public:
            int val() { return pvalue; }
            std::shared_ptr<link> &next() { return pnext; }
            explicit link(int value = 0) : pvalue(value), pnext(nullptr) {}
        };
    }
}