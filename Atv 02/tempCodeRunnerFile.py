:
        print(f"Assento {seat} já reservado.")
    else:
        map[seat[0]][seat[1]] = "X"
        print(f"Assento {seat} reservado.")