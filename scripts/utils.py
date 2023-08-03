def read_text_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines[0]

def split_text_into_segments(text):
    segments = text.split("~")
    return segments

def join_segments_into_text(segments):
    text = "~".join(segments)
    return text

def write_text_file(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)
    return