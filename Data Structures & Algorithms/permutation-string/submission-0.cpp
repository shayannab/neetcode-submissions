class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        vector<int> s1Count(26, 0);
        vector<int> windowCount(26, 0);
        int len1 = s1.size(), len2 = s2.size();

        // fill s1 count and first window
        for (int i = 0; i < len1; i++) {
            s1Count[s1[i] - 'a']++;
            windowCount[s2[i] - 'a']++;
        }

        // slide window
        for (int r = len1; r < len2; r++) {
            if (s1Count == windowCount)
                return true;

            windowCount[s2[r] - 'a']++;          // add new char on right
            windowCount[s2[r - len1] - 'a']--;   // remove old char on left
        }

        return s1Count == windowCount;  // check last window
    }
};