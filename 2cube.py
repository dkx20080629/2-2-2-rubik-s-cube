class RubiksCube:
    def __init__(self):
        #self.sides = [ [list(input().split()) for _ in range(2)] for i in range(6) ]
        #self.sides = [[["w","w"],["w","w"]],[["g","g"],["g","g"]],[["o","o"],["o","o"]],[["b","b"],["b","b"]],[["r","r"],["r","r"]],[["y","y"],["y","y"]]]
        self.sides = [[["g","w"],["g","r"]],[["o","b"],["r","b"]],[["y","o"],["r","y"]],[["w","b"],["g","o"]],[["r","g"],["w","w"]],[["y","b"],["y","o"]]]
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
            self.sides[5][1][i] = self.sides[4][1 - i][1]
            self.sides[4][1 - i][1] = self.sides[0][0][i]
            self.sides[0][0][i] = self.sides[2][i][0]
            self.sides[2][i][0] = a
        self.matrix_turn_right(self.sides[1])
        print("F")

    def F_(self):
        for i in range(2):
            a = self.sides[5][1][i]
            self.sides[5][1][i] = self.sides[2][i][0]
            self.sides[2][i][0] = self.sides[0][0][i]
            self.sides[0][0][i] = self.sides[4][1 - i][1]
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
        self.matrix_turn_left(self.sides[2])
        print("R")

    def R_(self):
        for i in range(2):
            a = self.sides[1][i][1]
            self.sides[1][i][1] = self.sides[5][i][1]
            self.sides[5][i][1] = self.sides[3][1 - i][0]
            self.sides[3][1 - i][0] = self.sides[0][i][1]
            self.sides[0][i][1] = a
        self.matrix_turn_right(self.sides[2])
        print("R")

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
#
def step1(cube):
    print("Starting Step 1...")
    for _ in range(4):
        if cube.sides[0][0][0] != "w":
            if cube.sides[1][0][0] == "w":
                cube.F()
                cube.U()
                cube.F_()
                print("F U F'")
            elif cube.sides[1][0][1] == "w":
                cube.U()
                cube.U()
                cube.F()
                cube.U_()
                cube.F_()
                print("U2 F U' F'")
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
                print("R U2 R' F U F' U2 R U' R'")
            elif cube.sides[1][1][0] == "w":
                cube.F()
                cube.U()
                cube.F_()
                cube.U_()
                cube.F()
                cube.U()
                cube.F_()
                print("F U F' U' F U F'")
            else:
                cube.U()
                print("U")
            if all(cube.sides[0][i][j] == "w" for i in range(2) for j in range(2)):
                break
        cube.D()
        print("D")

def step2(cube):
    print("Starting Step 2...")
    if cube.sides[5] != [["y", "y"], ["y", "y"]]:
        if cube.sides[5][0][0] == "y" and all(cube.sides[i][0][0] == "y" for i in range(1, 5)):
            cube.R_()
            cube.U_()
            cube.R()
            cube.U_()
            cube.R_()
            cube.U()
            cube.U()
            cube.R()
            print("R' U' R U' R' U2 R")
        elif cube.sides[5][1][0] == "y" and all(cube.sides[i][0][1] == "y" for i in range(1, 5)):
            cube.R()
            cube.U()
            cube.R_()
            cube.U()
            cube.R()
            cube.U()
            cube.U()
            cube.R_()
            print("R U R' U R U2 R'")
        elif cube.sides[5][1][1] == "y" and all(cube.sides[i][1][1] == "y" for i in range(1, 5)):
            cube.U()
            cube.R()
            cube.U()
            cube.R_()
            cube.U()
            cube.R()
            cube.U()
            cube.R_()
            print("U R U R' U R U R'")
        elif cube.sides[5][0][1] == "y" and all(cube.sides[i][1][0] == "y" for i in range(1, 5)):
            cube.U()
            cube.R()
            cube.U()
            cube.R_()
            cube.U()
            cube.R()
            cube.U()
            cube.R_()
            print("U R U R' U R U R'")
        else:
            cube.U()
            print("U")
    else:
        print("The top layer is already solved.")

def step3(cube):
    print("Starting Step 3...")
    if cube.sides[0][0][0] == "w":
        cube.R()
        cube.U()
        cube.R_()
        cube.U()
        cube.R()
        cube.U()
        cube.R_()
        cube.F()
        cube.U()
        cube.F_()
        cube.U_()
        cube.R()
        cube.U()
        cube.R_()
        cube.U_()
        cube.R()
        cube.U()
        cube.R_()
        cube.U()
        cube.F()
        cube.U()
        cube.F_()
        print("R U R' U R U R' U F U F' U' R U R' U'")
    elif cube.sides[0][0][1] == "w":
        cube.F()
        cube.U()
        cube.F_()
        cube.U_()
        cube.R()
        cube.U()
        cube.R_()
        cube.U_()
        cube.R()
        cube.U()
        cube.R_()
        cube.F()
        cube.U()
        cube.F_()
        print("F U F' U' R U R' U R U R' U' F U F'")
    else:
        print("The yellow cross is not in the correct position.")

def step4(cube):
    print("Starting Step 4...")
    if cube.sides[0][0][0] == "w":
        cube.R()
        cube.U()
        cube.R_()
        cube.U()
        cube.R()
        cube.U()
        cube.R_()
        cube.F()
        cube.U()
        cube.F_()
        cube.U_()
        cube.R()
        cube.U()
        cube.R_()
        cube.U_()
        cube.R()
        cube.U()
        cube.R_()
        cube.U()
        cube.F()
        cube.U()
        cube.F_()
        print("R U R' U R U R' U F U F' U' R U R' U'")
    else:
        print("The cube is not in the expected state.")

cube = RubiksCube()
cube.print_sides()
step1(cube)
"""step2(cube)
step3(cube)
step4(cube)"""

print("Final state of the cube:")
cube.print_sides()
