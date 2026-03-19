from PIL import Image
import argparse
import os

full_tile_index = 4
dual_corners_tile_index = 3

tile_size = 16

size_x = tile_size * 4
size_y = tile_size * 5

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates a 15-tile dual-grid autotile tileset using a 5-tile template")
    parser.add_argument("filepath", help="Path to the input file")
    args = parser.parse_args()
    
    filepath = args.filepath
    filename = os.path.basename(filepath)
    base = Image.open(filepath)
    parent = os.path.dirname(filepath)

    img = Image.new("RGBA", (size_x, size_y), (0, 0, 0, 0))

    for i in range(0, 5):

        amount = 4
        if i == full_tile_index:
            amount = 1
        elif i == dual_corners_tile_index:
            amount = 2

        for j in range(0, amount):
            start_left = tile_size * j
            start_top = tile_size * i
            end_right = start_left + tile_size
            end_bottom = start_top + tile_size

            box = (0, start_top, tile_size, end_bottom)
            sub_image = base.crop(box)
            sub_image = sub_image.rotate(-90 * j)
            img.paste(sub_image, (start_left, start_top))

    img.save(os.path.join(parent, "result" + filename))
