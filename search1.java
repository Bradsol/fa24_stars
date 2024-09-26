public class search1 {

  public static boolean patternFound(char[] pattern, char[] code) {
      
    int patLen = pattern.length;
    int codeLen = code.length;

    for (int i = 0; i <= codeLen - patLen; i++) { // checking each individual letter in code to see if it could be start of the pattern
      int j; 

      for (j = 0; j < patLen; j++) { // once we have potential start of pattern, check if the pattern continues on (for the whole length of the pattern)
        if (code[i +j] != pattern[j]) {
          break;
        }
      }

      if (j == patLen) { // returns true if pattern is present in code
        return true;
      }

    }
    return false;



  }

  public static boolean patternFound(String pattern, String code) {
    

    // checking each individual letter in code to see if it could be start of the pattern
    for (int i = 0; i <= code.length() - pattern.length(); i++) { 
      int j; 

      // once we have potential start of pattern, check if the pattern continues on (for the whole length of the pattern)
      for (j = 0; j < pattern.length(); j++) { 

        // when pattern doesnt match anymore, leave and go to next potential start

        if (code.charAt(i+j) != pattern.charAt(j)) { 
          break;
        }
      }

      // returns true if pattern is present in code
      if (j == pattern.length()) { 
        return true;
      }

    }
    return false;



  }





  public static void main(String args[]) {

    char[] p = {'g','t', 'g'};
    char[] series = {'g', 'a', 't', 'g','t', 'g','c', 'a','g', 'c','c', 'c'};

    String pat = "gcg";
    String code = "gatgtgcagccc";

    String gene = "ATGCGTACGATCGTAGCTAGCTAGCTAGCTGATCGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGATCGATCGTACGATCGATCGTAGCTAGCTAGCATGCTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCTAGCTAGCTGATCGTACGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGATCGATCGTACGATCGTAGCTAGCTAGCTAGCTGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCATGCTGATCGTACGATCGTAGCTAGCTGATCGATCGTACGATCGTACGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGATCGATCGTAGCTAGCTGATCGTAGCTAGCTAGCTAGCTAGCTAGCTGATCGTAGCTAGCTAGCTAG";
    String cancerGene1 = "AGCTAGCTAGCTAGC";
    String cancerGene2 = "TGCAAGCTTGACCTG";

    System.out.println(gene.contains(cancerGene1));

    System.out.println("Code contains this pattern : " + patternFound(p, series));
    System.out.println("Code contains this pattern : " + patternFound(pat, code));


    System.out.println("\nCancer gene 1 exists in gene : " + patternFound(cancerGene1, gene));
    System.out.println("Cancer gene 2 exists in gene : " + patternFound(cancerGene2, gene));






    
  }
  
}
