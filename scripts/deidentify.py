
def deidentify_segments(segments, maps):
    deid_segments = []

    for segment in segments:
        print(segment)
        fields = segment.split("*")
        i = 0
        submap = maps
        while i < len(fields):
            field_type, subtree = submap
            if field_type == "code":
                if fields[i] in subtree:
                    submap = subtree[fields[i]]
                else:
                    break
            if field_type == "recursive_code":
                codes = list(subtree.keys())
                while i < len(fields):
                    if fields[i] in codes:
                        temp_submap = subtree[fields[i]]
                        _, temp_subtree = temp_submap
                        deid_value = list(temp_subtree.keys())[0]
                        i += 1
                        fields[i] = deid_value
                    i += 1
                break
            elif field_type == "value":
                deid_value = list(subtree.keys())[0]
                if fields[i]:
                    fields[i] = deid_value
                submap = subtree[deid_value]
                if not submap:
                    break
            else:
                pass
            i += 1
        deid_segment = "*".join(fields)
        print(deid_segment)
        print()
        deid_segments.append(deid_segment)

    return deid_segments