def grep(pattern, flags, files):
    # Normalize flags to list
    if isinstance(flags, str):
        flags = flags.split()

    flag_i = "-i" in flags
    flag_v = "-v" in flags
    flag_x = "-x" in flags
    flag_n = "-n" in flags
    flag_l = "-l" in flags

    multiple_files = len(files) > 1

    # Prepare pattern comparison
    pattern_cmp = pattern.lower() if flag_i else pattern

    results = []

    for filename in files:
        match_found = False

        # Read lines from file
        with open(filename) as f:
            for lineno, raw_line in enumerate(f, start=1):
                line = raw_line.rstrip("\n")
                line_cmp = line.lower() if flag_i else line

                # Check full-line match or substring match
                if flag_x:
                    is_match = line_cmp == pattern_cmp
                else:
                    is_match = pattern_cmp in line_cmp

                # Apply invert flag if needed
                if flag_v:
                    is_match = not is_match

                if is_match:
                    match_found = True
                    if not flag_l:
                        prefix = ""
                        if multiple_files:
                            prefix += filename + ":"
                        if flag_n:
                            prefix += f"{lineno}:"
                        # Append line with newline!
                        results.append(prefix + line + "\n")

        # For -l, show only filenames that had a match
        if flag_l and match_found:
            results.append(filename + "\n")

    # Must return a single string (not list)
    return "".join(results)
