class RioranPaint:

    def __init__(self, height=32, width=22):
        self.rows = height
        self.cols = width
        self.map = [[0] * width for x in range(height)]

    def paint_circle(self, row, col, r):
        row_start = max(0, int(row - r))
        col_start = max(0, int(col - r))
        row_end = min(self.rows, int(row + r + 1))
        col_end = min(self.cols, int(col + r + 1))
        for i_row in range(row_start, row_end):
            for i_col in range(col_start, col_end):
                distance = ((i_row - row) ** 2 + (i_col - col) ** 2) ** 0.5
                if distance <= r:
                    self.map[i_row][i_col] = 1

    # row & col at top left corner of rectangle
    def paint_rectangle(self, row, col, height, width):
        row_start = max(0, row)
        col_start = max(0, col)
        row_end = min(self.rows, row + height + 1)
        col_end = min(self.cols, col + width + 1)
        for i_row in range(row_start, row_end):
            for i_col in range(col_start, col_end):
                self.map[i_row][i_col] = 1

    def delete_fill(self):
        tmp_arr = [item.copy() for item in self.map]
        for i_row in range(self.rows):
            for i_col in range(self.cols):
                if not self.map[i_row][i_col] == 1:
                    continue
                row_offset, col_offset = 0, -1
                pixel_must_be_purified = True
                for direction in range(4):
                    if row_offset == 0:
                        col_offset *= -1
                    row_offset, col_offset = col_offset, row_offset
                    try:
                        target = self.map[i_row + row_offset][i_col + col_offset]
                    except IndexError:
                        continue
                    if target == 0:
                        pixel_must_be_purified = False
                        break
                if pixel_must_be_purified:
                    tmp_arr[i_row][i_col] = 0
        for i_row in range(self.rows):
            for i_col in range(self.cols):
                if not self.map[i_row][i_col] == tmp_arr[i_row][i_col]:
                    self.map[i_row][i_col] = tmp_arr[i_row][i_col]

    def print(self):
        for i_row in range(self.rows):
            for i_col in range(self.cols):
                char = 'X' if self.map[i_row][i_col] > 0 else '-'
                print(char + ' ', end='')
            print('')
            

if __name__ == '__main__':
    dicture = RioranPaint()
    dicture.paint_circle(row = 6, col = 6, r = 5.5)
    dicture.paint_circle(row = 6, col = 15, r = 5.5)
    dicture.paint_rectangle(row = 6, col = 6, height = 20, width = 8)
    dicture.paint_circle(row = 25, col = 10, r = 5.5)
    dicture.delete_fill()
    dicture.paint_rectangle(row = 28, col = 10, height = 2, width = 0)
    dicture.print()
