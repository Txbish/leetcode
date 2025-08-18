class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string ret;
        while (word1.length() && word2.length())
        {
            ret.push_back(word1.front());
            word1.erase(word1.begin());
            ret.push_back(word2.front());
            word2.erase(word2.begin());
        }

        while (word1.length())
        {
            ret.push_back(word1.front());
            word1.erase(word1.begin());
        }
        while (word2.length())
        {
            ret.push_back(word2.front());
            word2.erase(word2.begin());
        }
        return ret;
    }
};