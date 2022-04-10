def write_d():
    asterisk_positions = [[1,2,3],[1,4],[1,5],[1,5],[1,5],[1,4],[1,2,3]]
    ast_d = ""
    for i in range(len(asterisk_positions)):
        out_string = ""
        for j in range(7):
            if j in asterisk_positions[i]:
                out_string += "*"
            else:
                out_string += " "
        ast_d += out_string
        if i != len(asterisk_positions)-1:
            ast_d += "\n"
    return ast_d

print(write_d())

print(write_d() + write_d())