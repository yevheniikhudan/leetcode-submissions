class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        for (int wordNum = 0; wordNum < words.size(); wordNum++) {
            for (int chrPos = 0; chrPos < words[wordNum].size(); chrPos++) {
                if (chrPos >= words.size() ||
                    wordNum >= words[chrPos].size() ||
                    words[wordNum][chrPos] != words[chrPos][wordNum]) {
                        return false;
                    }
            }
        }
        return true;
    }
};
