import satchecker


def main():
    verticesA = [[0, 0], [70, 0], [0, 70], [70, 70]]
    verticesB = [[80, 80], [150, 70], [70, 150]]
    verticesC = [[30, 30], [150, 70], [70, 150]]

    print (satchecker.SATCheck(verticesA, verticesB))
    print (satchecker.SATCheck(verticesA, verticesC))
    print (satchecker.SATCheck(verticesB, verticesC))


if __name__ == "__main__":
    main()
