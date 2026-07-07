class Solution {
    public boolean confusingNumber(int n) {
        Map<Integer, Integer> invertMap = Map.of(0, 0, 1, 1, 8, 8, 6, 9, 9, 6);
        int invertNumber = 0;
        int nCopy = n;

        while (nCopy > 0) {
            int temp = nCopy % 10;

            if (!invertMap.containsKey(temp)) return false;

            invertNumber = invertNumber * 10 + invertMap.get(temp);
            nCopy /= 10;
        }

        return invertNumber != n;
    }
}
