import tkinter as tk
from PIL import Image, ImageTk

class Chessboard:
    def __init__(self, root):
        self.root = root

        # Create a canvas for the chessboard.
        self.canvas = tk.Canvas(root, width=512, height=512)
        self.canvas.pack()

        # Load the chess piece images.
        self.piece_images = {}
        for piece_name in ["wP", "wR", "wN", "wB", "wK", "wQ", "bP", "bR", "bN", "bB", "bK", "bQ"]:
            self.piece_images[piece_name] = ImageTk.PhotoImage(Image.open(f"images/{piece_name}.png"))

        # Draw the chessboard.
        for i in range(8):
            for j in range(8):
                color = "#eeeed2" if (i + j) % 2 == 0 else "#769656"
                self.canvas.create_rectangle(i * 64, j * 64, (i + 1) * 64, (j + 1) * 64, fill=color)

        PIECE_NAMES = ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP",
                       "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bR", "bN", "bB", "bK", "bQ", "bB", "bN", "bR"]
        # def get_piece_name(i, j):
        #     index = i * 8 + j
        #     if index < 0 or index >= len(PIECE_NAMES):
        #         return None
        #     else:
        #         return PIECE_NAMES[index]

        # Place the chess pieces on the board.
        # for i in range(8):
        #     for j in range(8):
        #         piece_name = get_piece_name(i, j)
        #         if piece_name is not None:
        #             piece_image = self.piece_images[piece_name]
        #             self.canvas.create_image(i * 64 + 32, j * 64 + 32, image=piece_image)
        # Place the white pieces.
        for i in range(8):
            piece_name = PIECE_NAMES[i]
            if piece_name is not None:
                piece_image = self.piece_images[piece_name]
                self.canvas.create_image(i * 64 + 32, 0 * 64 + 32, image=piece_image)

            # Place the white pawns.
        for i in range(8):
            piece_name = PIECE_NAMES[8 + i]
            if piece_name is not None:
                piece_image = self.piece_images[piece_name]
                self.canvas.create_image(i * 64 + 32, 1 * 64 + 32, image=piece_image)

            # Place the black pawns.
        for i in range(8):
            piece_name = PIECE_NAMES[16 + i]
            if piece_name is not None:
                piece_image = self.piece_images[piece_name]
                self.canvas.create_image(i * 64 + 32, 6 * 64 + 32, image=piece_image)

            # Place the black pieces.
        for i in range(8):
            piece_name = PIECE_NAMES[24 + i]
            if piece_name is not None:
                piece_image = self.piece_images[piece_name]
                self.canvas.create_image(i * 64 + 32, 7 * 64 + 32, image=piece_image)

root = tk.Tk()
root.title("Chessboard")

chessboard = Chessboard(root)

root.mainloop()