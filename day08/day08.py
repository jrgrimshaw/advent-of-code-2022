def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def main():
  file = readFile("input.txt")

  matrix = []
  matrix = file.split("\n")
  for i,row in enumerate(matrix):
    matrix[i] = [int(x) for x in list(row)]

  count = 0

  for i, row in enumerate(matrix):
    for j, col in enumerate(row):
      if i == 0 or j == 0 or i == len(matrix)-1 or j == len(row)-1 :
        count += 1
      else:
        visibility = {'n': True, 's': True, 'e': True, 'w': True}

        for r in range(i):
          if matrix[r][j] >= matrix[i][j]:
            visibility['n'] = False

        for r in range(len(matrix)-i-1):
          if matrix[r+i+1][j] >= matrix[i][j]:
            visibility['s'] = False

        for c in range(j):
          if matrix[i][c] >= matrix[i][j]:
            visibility['w'] = False

        for c in range(len(row)-j-1):
          if matrix[i][c+j+1] >= matrix[i][j]:
           visibility['e'] = False

        if visibility['n'] or visibility['s'] or visibility['e'] or visibility['w']:
          count += 1

  print(count)

if __name__ == "__main__":
  main()