class Solution {
public:
    int calculateTime(string keyboard, string word) {
        unordered_map<char, int> indices;
        for (int i = 0; i < keyboard.length(); i++) {
            indices[keyboard[i]] = i;
        }

        int ans = indices[word[0]];
        for (int i = 1; i < word.length(); i++) {
            ans += abs(indices[word[i-1]] - indices[word[i]]);
        }
        return ans;
    }
};
