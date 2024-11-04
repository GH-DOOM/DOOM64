# DOOM on Contribution Graph
![Banner on graph](/assets/banner_on_graph.png)

## Requirements
- DOOM 64 <sub>(tested on Epic Games version)</sub>
- Firefox
- Python 3

Feel free to port to other browsers!

## How to Use
1. **Install requirements** with `pip install -r requirements.txt`
2. **Start DOOM 64** before running the program, or it won't detect the game window.

## How Does It Work?
The program will:
1. Take a screenshot of your game as quickly as possible.
2. Resize the image to 51x7 pixels (not 52, as the last week isn’t always full).
3. Change the color of each pixel.
4. Repeat!

For best results, run DOOM 64 in 800x600 resolution in windowed mode.

### Inspiration
[`"Fixing" My GitHub`](https://www.youtube.com/watch?v=_aDvNg9F6w8) by Dev Detour.