
public class practicing {
  


  static boolean validateMagicSquare(int[][] array) {
    if (array == null || array.length == 0) {
        return false;
    }

    int size = array.length;

    // Finish: Compute the "correct" sum
    int correctSum = 0;
    for (int i = 0; i < size; i++) {
        correctSum += array[0][i];
    }

    // Check either "rows"
    int currentSum;
    for (int i = 0; i < size; i++) {
        currentSum = 0;
        for (int j = 0; j < size; j++) {
            currentSum += array[i][j];
        }
        if (currentSum != correctSum) {
            return false;
        }
    }

    // Check columns
    for (int i = 0; i < size; i++) {
        currentSum = 0;
        for (int j = 0; j < size; j++) {
            currentSum += array[j][i];
        }
        if (currentSum != correctSum) {
            return false;
        }
    }

    // Check one diagonal
    currentSum = 0;
    for (int i = 0; i < size; i++) {
        currentSum += array[i][i];
    }
    if (currentSum != correctSum) {
        return false;
    }


    currentSum = 0;
    for (int i = 0; i < size; i++) {
        currentSum += array[i][size - 1 - i];
    }
    if (currentSum != correctSum) {
        return false;
    }



    return true;
}
  // 02
  //11
  //20


  //210
  public static void main(String[] args) {   
    int[][] multi = new int[][] {
      { -6, -12, -5},
      { -10, -6, -7},
      {-7, -5, -11},
    };

    System.out.println(validateMagicSquare(multi));


    
  }

  
}
