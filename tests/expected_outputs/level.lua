return {
  version = "1.9",
  luaversion = "5.1",
  tiledversion = "1.9.2",
  orientation = "orthogonal",
  renderorder = "right-down",
  width = 10,
  height = 5,
  tilewidth = 48,
  tileheight = 48,
  backgroundcolor = {0, 170, 255},
  nextlayerid = 2,
  nextobjectid = 1,
  compressionlevel = -1,
  infinite = false,
  properties = {},
  tilesets = {
    {
      name = "tileset",
      firstgid = 1,
      filename = "tileset.tsx"
    }
  },
  layers = {
    {
      x = 0,
      y = 0,
      opacity = 1,
      visible = true,
      id = 1,
      name = "Tile Layer 1",
      class = "",
      width = 10,
      height = 5,
      encoding = "lua",
      data = {
        0, 0, 0, 0, 0, 0, 0, 2, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 2, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 2, 0, 0,
        1, 1, 0, 0, 1, 1, 1, 1, 1, 1,
        3, 3, 0, 0, 3, 3, 3, 3, 3, 3
      }
    }
  }
}
