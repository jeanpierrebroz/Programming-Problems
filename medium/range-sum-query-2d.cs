public class NumMatrix {

    private List<List<int>> rows = [];
    private List<List<int>> cols = [];
    private int[][] matrix;
    private int[][] prefixSum;
    public NumMatrix(int[][] matrix) {
        int NUM_ROWS = matrix.Length;
        int NUM_COLS = matrix[0].Length;
        this.matrix = matrix;
        prefixSum = new int[NUM_ROWS + 1][];
        for (int i = 0; i <= NUM_ROWS; i++) prefixSum[i] = new int[NUM_COLS + 1];

        for (int i = 0; i < NUM_ROWS; i++) {
            for (int j = 0; j < NUM_COLS; j++) {
                prefixSum[i + 1][j + 1] = matrix[i][j] + prefixSum[i][j + 1] + prefixSum[i + 1][j] - prefixSum[i][j];
            }
        }
    }
    
    public int SumRegion(int row1, int col1, int row2, int col2) {
        return prefixSum[row2 + 1][col2 + 1] - prefixSum[row1][col2 + 1] - prefixSum[row2 + 1][col1] + prefixSum[row1][col1];
    }
}