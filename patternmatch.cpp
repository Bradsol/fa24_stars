// Ranjana Rajagopalan
// 09/23/24
#include <iostream>
#include <string>

/* Runtime:
 * For loop runs (n - m + 1) times, which is O(n) because m (size of pattern) is smaller than n (size of text)
 * substr() function has runtime O(m), because extracting strings of length m
 * Outer loop is O(n) and substr is O(m) for every iteration of the loop so runtime is:
 *
 * O(n*m)
 */

void match(std::string str, std::string pattern)
{
    // check whether there is no match at the end
    bool noMatch = false;

    // go through the text
    for (int i = 0; i < str.size() - pattern.size() + 1; i++)
    {

        // extract the piece of text that is same length as pattern and compare
        std::string curr = str.substr(i, pattern.size());

        if (curr == pattern)
        {
            std::cout << "There is a pattern match at the index " << i << "." << std::endl;
            noMatch = true;
        }
    }

    if (!noMatch)
    {
        std::cout << "There is no pattern match." << std::endl;
    }
}

int main()
{
    std::string str1 = "TO BE OR NOT TO BE";
    std::string str2 = "to be or not to be";

    std::string pattern = "TO";

    match(str1, pattern);
    match(str2, pattern);
    return 0;
}