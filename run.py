import sys
from scripts.deidentify import deidentify_segments
from scripts.maps import (
    N1_map,
    N3_map,
    N4_map,
    NM1_map,
    PER_map,
)
from scripts.utils import (
    read_text_file, 
    split_text_into_segments, 
    join_segments_into_text,
    write_text_file
)


map_835 = (
    "code", 
    {
        "N1": N1_map,
        "N3": N3_map,
        "N4": N4_map,
        "NM1": NM1_map,
        "PER": PER_map,
    }
)

def main(file_path):
    edi_data = read_text_file(file_path)
    edi_segments = split_text_into_segments(edi_data)
    deid_segments = deidentify_segments(edi_segments, map_835)
    deid_data = join_segments_into_text(deid_segments)
    write_text_file(file_path.replace("input", "output"), deid_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <edi_input_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)