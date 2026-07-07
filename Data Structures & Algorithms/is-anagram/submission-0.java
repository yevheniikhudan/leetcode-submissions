class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] counters = new int[26];

        for (int i = 0; i < s.length(); i++) {
            counters[s.charAt(i) - 'a'] += 1;
            counters[t.charAt(i) - 'a'] -= 1;
        }

        for (int counter : counters) {
            if (counter != 0)
                return false;
        }

        return true;
    }
}
