class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        ArrayList<Integer> ind = new ArrayList<>();
        int n = deck.length;
        int[] temp = new int[n];

        for(int i = 0; i < deck.length; i ++){
            ind.add(i);
            temp[i] = deck[i];
        }
        Arrays.sort(temp);

        int i = 0, j = 0, index = 0;
        while(ind.size() != 0){
            if(i == ind.size() - 2){
                index = ind.remove(i);
                deck[index] = temp[j];
                j += 1;
                i = 0;
            }
            else if(i == ind.size() - 1){
                index = ind.remove(i);
                deck[index] = temp[j];
                j += 1;
                if(ind.size() > 1){
                    i = 1;
                }
                else{
                    i = 0;
                }
            }
            else{
                System.out.println(i);
                index = ind.remove(i);
                deck[index] = temp[j];
                j += 1;
                i = i + 1;
            }
            
        }

        return deck;
      
    }
}