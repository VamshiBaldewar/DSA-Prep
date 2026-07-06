class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });
        
        int remainingCount = 0;
        int currentEnd = -1;
        
        for (int[] interval : intervals) {
            int end = interval[1];
            if (end > currentEnd) {
                remainingCount++;
                currentEnd = end;
            }
        }
        
        return remainingCount;
        
    }
}