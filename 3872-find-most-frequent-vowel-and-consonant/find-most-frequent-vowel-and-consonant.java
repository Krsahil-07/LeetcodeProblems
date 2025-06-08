class Solution {
    public int maxFreqSum(String s) {
        HashMap<Character, Integer> vow = new HashMap<>();
        HashMap<Character, Integer> cons = new HashMap<>();
        Set<Character> s1 = Set.of('a', 'e', 'i', 'o', 'u');

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (s1.contains(ch)) {
                vow.put(ch, vow.getOrDefault(ch, 0) + 1);
            } else {
                cons.put(ch, cons.getOrDefault(ch, 0) + 1);
            }
        }
        int maxVowelFreq = vow.values().stream().max(Integer::compare).orElse(0);
        int maxConsFreq = cons.values().stream().max(Integer::compare).orElse(0);
        return maxVowelFreq+maxConsFreq;
    }
}
