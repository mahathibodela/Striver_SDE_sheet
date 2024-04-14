class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int start = 0, end = tokens.length - 1;
        int score = 0, maxScore = 0;

        while(start <= end){
            if(power < tokens[start]){
                if(score >= 1){
                    power += tokens[end];
                    end -= 1;
                    score -= 1;
                }
                else{
                    return maxScore;
                }
            }
            else{
                power -= tokens[start];
                score += 1;
                maxScore = score;
                start += 1;
            }
        }

        return maxScore;
    }
}