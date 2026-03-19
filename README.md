# dual-grid-tileset-generator
Generates a 15-tile dual-grid tilesystem tileset using a 1x5 template

# usage
./dualgrid-generate-linux <path-to-image>

The image must have the same format as the template image:
1. 16x80 image
2. The first tile is a corner tile, situated on the top left
3. The second tile is an edge tile, located on the left
4. The third tile is joint tile, with the outwards-facing side facing south-east
5. The fourth tile is a dual-corner tile; one on top-left, the other bottom right
6. The final tile is a completely filled tile

For reference, see these videos: 
- https://youtu.be/aWcCNGen0cM by Nonsensical 2D
- https://www.youtube.com/watch?v=jEWFSv3ivTg by jess::codes

I made this script for my own game which uses 16x16 tiles. Therefore, the script does not by default support tile sizes other than 16x16, but it is easy enough to configure by changing a variable value in the code.
