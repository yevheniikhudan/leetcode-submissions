class Solution {

    public int calculateTime(String keyboard, String word) {
        Map<Character, Integer> indices = new HashMap<>();
        for (int i = 0; i < keyboard.length(); i++) {
            indices.put(keyboard.charAt(i), i);
        }

        int ans = indices.get(word.charAt(0));
        for (int i = 1; i < word.length(); i++) {
            ans += Math.abs(
                indices.get(word.charAt(i - 1)) - indices.get(word.charAt(i))
            );
        }
        return ans;
    }
}
