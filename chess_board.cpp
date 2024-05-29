#include <iostream>
#include <vector>

class ChessBoard {
public:
    ChessBoard() {
        // board initialized with pieces
        board = {
            {'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'},
            {'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
            {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
            {'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'},
            {'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'}
        };
    }

    void display() const {
        for (int row = 0; row < 8; ++row) {
            std::cout << 8 - row << " "; // Print the row number
            for (int col = 0; col < 8; ++col) {
                std::cout << board[row][col] << " ";
            }
            std::cout << std::endl;
        }
        std::cout << "  a b c d e f g h" << std::endl; // Print the column letters
    }

private:
    std::vector<std::vector<char>> board;
};

int main() {
    ChessBoard chessBoard;
    chessBoard.display();
    return 0;
}