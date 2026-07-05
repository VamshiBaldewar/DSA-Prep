class Solution {
    public int[] pathsWithMaxScore(List<String> board) {
        int n = board.size();
        int[][] maxScore = new int[n][n];
        int[][] paths = new int[n][n];
        int MOD = 1000000007;

        paths[n - 1][n - 1] = 1;

        int[][] dirs = {{1, 0}, {0, 1}, {1, 1}};

        for (int r = n - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (paths[r][c] == 0 || board.get(r).charAt(c) == 'X') {
                    continue;
                }

                for (int[] dir : dirs) {
                    int nr = r - dir[0];
                    int nc = c - dir[1];

                    if (nr >= 0 && nc >= 0 && board.get(nr).charAt(nc) != 'X') {
                        int currentVal = 0;
                        if (board.get(nr).charAt(nc) != 'E') {
                            currentVal = board.get(nr).charAt(nc) - '0';
                        }
                        
                        int nextScore = maxScore[r][c] + currentVal;

                        if (nextScore > maxScore[nr][nc]) {
                            maxScore[nr][nc] = nextScore;
                            paths[nr][nc] = paths[r][c];
                        } else if (nextScore == maxScore[nr][nc]) {
                            paths[nr][nc] = (paths[nr][nc] + paths[r][c]) % MOD;
                        }
                    }
                }
            }
        }

        return new int[]{maxScore[0][0], paths[0][0]};
        
    }
}