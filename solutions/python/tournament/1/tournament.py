def tally(rows):
    # Stats index: MP, W, D, L, P
    stats = {}

    def init(team):
        if team not in stats:
            stats[team] = [0, 0, 0, 0, 0]

    for row in rows:
        if not row.strip():
            continue

        team1, team2, result = row.split(";")
        init(team1)
        init(team2)

        stats[team1][0] += 1  # MP
        stats[team2][0] += 1  # MP

        if result == "win":
            stats[team1][1] += 1  # W
            stats[team1][4] += 3  # P
            stats[team2][3] += 1  # L
        elif result == "loss":
            stats[team2][1] += 1  # W
            stats[team2][4] += 3  # P
            stats[team1][3] += 1  # L
        elif result == "draw":
            stats[team1][2] += 1  # D
            stats[team2][2] += 1  # D
            stats[team1][4] += 1  # P
            stats[team2][4] += 1  # P
        else:
            raise ValueError("Invalid result")

    # Sort: Points DESC, then team name ASC
    ordered = sorted(stats.items(), key=lambda x: (-x[1][4], x[0]))

    header = "Team                           | MP |  W |  D |  L |  P"
    table = [header]

    for team, (mp, w, d, l, p) in ordered:
        table.append(f"{team:31}| {mp:2d} | {w:2d} | {d:2d} | {l:2d} | {p:2d}")

    return table

