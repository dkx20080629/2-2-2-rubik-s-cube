class RubiksCube:
    def __init__(self):
        self.sides = [ [list(input().split()) for _ in range(2)] for i in range(6) ]
    def matrix_turn_left(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                a = matrix[i][j]
                matrix[i][j] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = a

    def matrix_turn_right(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                a = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = a

    def U(self):
        for i in range(2):
            a = self.sides[1][0][i]
            self.sides[1][0][i] = self.sides[2][0][i]
            self.sides[2][0][i] = self.sides[3][0][i]
            self.sides[3][0][i] = self.sides[4][0][i]
            self.sides[4][0][i] = a
        self.matrix_turn_right(self.sides[5])
        print("U")

    def U_(self):
        for i in range(2):
            a = self.sides[1][0][i]
            self.sides[1][0][i] = self.sides[4][0][i]
            self.sides[4][0][i] = self.sides[3][0][i]
            self.sides[3][0][i] = self.sides[2][0][i]
            self.sides[2][0][i] = a
        self.matrix_turn_left(self.sides[5])
        print("U'")

    def F(self):
        for i in range(2):
            a = self.sides[5][1][i]
            self.sides[5][1][i] = self.sides[4][-i-1][1]
            self.sides[4][-i-1][1] = self.sides[0][0][-i-1]
            self.sides[0][0][-i-1] = self.sides[2][i][0]
            self.sides[2][i][0] = a
        self.matrix_turn_right(self.sides[1])
        print("F")

    def F_(self):
        for i in range(2):
            a = self.sides[5][1][i]
            self.sides[5][1][i] = self.sides[2][i][0]
            self.sides[2][i][0] = self.sides[0][0][-i-1]
            self.sides[0][0][-i-1] = self.sides[4][1 - i][1]
            self.sides[4][1 - i][1] = a 
        self.matrix_turn_left(self.sides[1])
        print("F'")

    def R(self):
        for i in range(2):
            a = self.sides[1][i][1]
            self.sides[1][i][1] = self.sides[0][i][1]
            self.sides[0][i][1] = self.sides[3][1 - i][0]
            self.sides[3][1 - i][0] = self.sides[5][i][1]
            self.sides[5][i][1] = a
        self.matrix_turn_right(self.sides[2])
        print("R")

    def R_(self):
        for i in range(2):
            a = self.sides[1][i][1]
            self.sides[1][i][1] = self.sides[5][i][1]
            self.sides[5][i][1] = self.sides[3][1 - i][0]
            self.sides[3][1 - i][0] = self.sides[0][i][1]
            self.sides[0][i][1] = a
        self.matrix_turn_left(self.sides[2])
        print("R'")

    def D(self):
        for i in range(2):
            a = self.sides[1][1][i]
            self.sides[1][1][i] = self.sides[4][1][i]
            self.sides[4][1][i] = self.sides[3][1][i]
            self.sides[3][1][i] = self.sides[2][1][i]
            self.sides[2][1][i] = a
        self.matrix_turn_right(self.sides[0])
        print("D")

    def D_(self):
        for i in range(2):
            a = self.sides[1][1][i]
            self.sides[1][1][i] = self.sides[2][1][i]
            self.sides[2][1][i] = self.sides[3][1][i]
            self.sides[3][1][i] = self.sides[4][1][i]
            self.sides[4][1][i] = a
        self.matrix_turn_left(self.sides[0])
        print("D'")

    def print_sides(self):
        print("Final state of each side:")
        for i, side in enumerate(self.sides):
            print(f"Side {i}:")
            for row in side:
                print(" ".join(row))
        print()
def step1(cube):
    print("Step 1")
    for i in range(4):
        if cube.sides[0][0][0] != "w":
            for i in range(4):
                if cube.sides[1][0][0] == "w":
                    cube.F()
                    cube.U()
                    cube.F_()
                    print("F U F' ---")
                elif cube.sides[1][0][1] == "w":
                    cube.U()
                    cube.U()
                    cube.F()
                    cube.U_()
                    cube.F_()
                    print("U2 F U' F' ---")
                elif cube.sides[5][1][1] == "w":
                    cube.R()
                    cube.U()
                    cube.U()
                    cube.R_()
                    cube.F()
                    cube.U()
                    cube.F_()
                    cube.U()
                    cube.U()
                    cube.R()
                    cube.U_()
                    cube.R_()
                    print("R U2 R' F U F' U2 R U' R' ---")
                elif cube.sides[1][1][0] == "w":
                    cube.F()
                    cube.U()
                    cube.F_()
                    cube.U_()
                    cube.F()
                    cube.U()
                    cube.F_()
                    print("F U F' U' F U F' ---")
                elif cube.sides[4][1][1] == "w":
                    cube.F()
                    cube.U_()
                    cube.F_()
                    cube.U()
                    cube.F()
                    cube.U_()
                    cube.F_()
                    print("F U' F' U F U' F' ---")
                else:
                    cube.U()
                    print("U ---")
                if cube.sides[0] == [["w","w"],["w","w"]]: break
        cube.D()
        print("D ---")

def step2(cube):
    print("Step 2")
    for i in range(4):
        if cube.sides == [["y", "y"],["y", "y"]]: break
        if cube.sides[5] != [["y", "y"], ["y", "y"]]:
            if cube.sides[5][0][0] == "y" and cube.sides[1][0][0] == "y" and cube.sides[2][0][0] == "y" and cube.sides[3][0][0] == "y":
                cube.R_()
                cube.U_()
                cube.R()
                cube.U_()
                cube.R_()
                cube.U()
                cube.U()
                cube.R()
                print("R' U' R U' R' U2 R ---")
            elif cube.sides[5][1][0] == "y" and cube.sides[1][0][1] == "y" and cube.sides[2][0][1] == "y" and cube.sides[3][0][1] == "y":
                cube.R()
                cube.U()
                cube.R_()
                cube.U()
                cube.R()
                cube.U()
                cube.U()
                cube.R_()
                print("R U R' U R U2 R' ---")
            elif cube.sides[5][0][0] == "y" and cube.sides[5][1][1] == "y" and cube.sides[1][0][0] == "y" and cube.sides[2][0][1] == "y":
                cube.F()
                cube.R_()
                cube.F_()
                cube.R()
                cube.U()
                cube.R()
                cube.U_()
                cube.R_()
                print("F R' F' R U R U' R' ---")
            elif cube.sides[5][0][1] == "y" and cube.sides[5][1][1] == "y" and cube.sides[1][0][0] == "y" and cube.sides[3][0][1] == "y":
                cube.R()
                cube.U()
                cube.R_()
                cube.U_()
                cube.R_()
                cube.F()
                cube.R()
                cube.F_()
                print("R U R' U' R' F R F' ---")
            elif cube.sides[5][0][1] == "y" and cube.sides[5][1][1] == "y" and cube.sides[4][0][0] == "y" and cube.sides[4][0][1] == "y":
                cube.F()
                cube.R()
                cube.U()
                cube.R_()
                cube.U_()
                cube.F_()
                print("F R U R' U' F' ---")
            elif cube.sides[1][0][0] == "y" and cube.sides[1][0][1] == "y" and cube.sides[3][0][0] == "y" and cube.sides[3][0][1] == "y":
                cube.R()
                cube.R()
                cube.U()
                cube.U()
                cube.R_()
                cube.U()
                cube.U()
                cube.R()
                cube.R()
                print("R2 U2 R' U2 R2 ---")
            elif cube.sides[1][0][1] == "y" and cube.sides[3][0][0] == "y" and cube.sides[4][0][0] == "y" and cube.sides[4][0][1] == "y":
                cube.F()
                for i in range(2):
                    cube.R()
                    cube.U()
                    cube.R_()
                    cube.U_()
                cube.F_()
                print("F ( R U R' U')*2 F' ---")
            cube.U()
            print("U ---")
def step3(cube):
    print("Step 3")
    if cube.sides[2][0][0] == cube.sides[2][0][1]:
        cube.U()
        cube.U()
        print("U2 ---")
    elif cube.sides[3][0][0] == cube.sides[3][0][1]:
        cube.U_()
        print("U' ---")
    elif cube.sides[1][0][0] == cube.sides[1][0][1]:
        cube.U()
        print("U ---")
    elif cube.sides[2][0][0] != cube.sides[2][0][1] and cube.sides[1][0][0] != cube.sides[1][0][1] and cube.sides[3][0][0] != cube.sides[3][0][1] and cube.sides[4][0][0] != cube.sides[4][0][1]:
        cube.R()
        cube.U()
        cube.R_()
        cube.F_()
        cube.R()
        cube.U()
        cube.R_()
        cube.U_()
        cube.R_()
        cube.F()
        cube.R()
        cube.R()
        cube.U_()
        cube.R_()
        print("R U R' F' R U R' U' R' F R2 U' R' ---")
    for i in range(4):
        if cube.sides[4][0][0] == cube.sides[4][0][1] and cube.sides[1][0][0] == cube.sides[1][0][1] and cube.sides[2][0][0] == cube.sides[2][0][1] and cube.sides[3][0][0] == cube.sides[3][0][1]:
            break
        if cube.sides[4][0][0] == cube.sides[4][0][1] and cube.sides[1][0][0] != cube.sides[1][0][1]:
            cube.R()
            cube.U()
            cube.R_()
            cube.F_()
            cube.R()
            cube.U()
            cube.R_()
            cube.U_()
            cube.R_()
            cube.F()
            cube.R()
            cube.R()
            cube.U_()
            cube.R_()
            print("R U R' F' R U R' U' R' F R2 U' R' ---")
        else:
            cube.U()
            print("U ---")

def step4(cube):
    if cube.sides[1][1][0] != cube.sides[1][1][1] and cube.sides[2][1][0] != cube.sides[2][1][1] and cube.sides[3][1][0] != cube.sides[3][1][1] and cube.sides[4][1][0] != cube.sides[4][1][1]:
        cube.R_()
        cube.D_()
        cube.R()
        cube.F()
        cube.R_()
        cube.D_()
        cube.R()
        cube.D()
        cube.R()
        cube.F_()
        cube.R()
        cube.R()
        cube.D()
        cube.R()
        print("R' D' R F R' D' R D R F' R2 D R ---")
    for i in range(2):
        if cube.sides[4][1][0] == cube.sides[4][1][1] and cube.sides[1][1][0] == cube.sides[1][1][1] and cube.sides[2][1][0] == cube.sides[2][1][1] and cube.sides[3][1][0] == cube.sides[3][1][1]:
            break
        if cube.sides[4][1][0] == cube.sides[4][1][1]:
            cube.R_()
            cube.D_()
            cube.R()
            cube.F()
            cube.R_()
            cube.D_()
            cube.R()
            cube.D()
            cube.R()
            cube.F_()
            cube.R()
            cube.R()
            cube.D()
            cube.R()
            print("R' D' R F R' D' R D R F' R2 D R ---")
        elif cube.sides[1][1][0] == cube.sides[1][1][1]:
            cube.D_()
            print("D' ---")
        elif cube.sides[2][1][0] == cube.sides[2][1][1]:
            cube.D()
            cube.D()
            print("D2 ---")
        elif cube.sides[3][1][0] == cube.sides[3][1][1]:
            cube.D()
            print("D ---")

    while cube.sides[4][1] != cube.sides[4][0]:
        cube.D()
        print("D ---")

cube = RubiksCube()
cube.print_sides()
print("-----")
step1(cube)
print("-----")
step2(cube)
print("-----")
step3(cube)
print("-----")
step4(cube)
cube.print_sides()