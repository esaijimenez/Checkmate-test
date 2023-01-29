from tools.mates import mateIn1
from tools.mates import mateIn2
from tools.mates import mateIn3
from tools.mates import mateIn4
from tools.mates import mateIn5

#Converts all the DataFrames to a .json file
mateIn1.to_json(r'\checkmate\mateIn1.json',orient='records')

mateIn2.to_json(r'\checkmate\mateIn2.json',orient='records')

mateIn3.to_json(r'\checkmate\mateIn3.json',orient='records')

mateIn4.to_json(r'\checkmate\mateIn4.json',orient='records')

mateIn5.to_json(r'\checkmate\mateIn5.json',orient='records')