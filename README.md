# NQueens with USC, A* and Genetic Algorithm

- Lab homework from HCMUS's 2023 Introduction to AI course.

## Content

- Read the attached pdf for full details.

### UCS and A*

- Initially, all the queens are placed at row -1, each column is occupied by exactly one queen.
- The solution for a specific N will always be the same no matter how many times it's run.

```text
--8 Queens A*--
Execution time:         16.0000 ms
Memory usage:            0.0278 MB
Solution: [7, 1, 3, 0, 6, 4, 2, 5]

        0   1   2   3   4   5   6   7 
     ----------------------------------
  0 |   *   *   *   Q   *   *   *   *  |  0
  1 |   *   Q   *   *   *   *   *   *  |  1
  2 |   *   *   *   *   *   *   Q   *  |  2
  3 |   *   *   Q   *   *   *   *   *  |  3
  4 |   *   *   *   *   *   Q   *   *  |  4
  5 |   *   *   *   *   *   *   *   Q  |  5
  6 |   *   *   *   *   Q   *   *   *  |  6
  7 |   Q   *   *   *   *   *   *   *  |  7
     ----------------------------------
        0   1   2   3   4   5   6   7 
```

### Genetic Algorithm

- Each generation has 100 chromosomes, there is an option to print out all generations with their chromosomes.
- The fittest chromosome is one where the number of attacking pairs of queens is 0. Mutation probability is set to 0.8.
- **The algorithm takes ***very long*** to find a solution.**

```text
--8 Queens Genetic Algorithm--
Solved in Generation 137155
Execution time:    1696469.0000 ms
Memory usage:            0.0322 MB
Solution: [4, 6, 0, 2, 7, 5, 3, 1]

        0   1   2   3   4   5   6   7 
     ----------------------------------
  0 |   *   *   Q   *   *   *   *   *  |  0
  1 |   *   *   *   *   *   *   *   Q  |  1
  2 |   *   *   *   Q   *   *   *   *  |  2
  3 |   *   *   *   *   *   *   Q   *  |  3
  4 |   Q   *   *   *   *   *   *   *  |  4
  5 |   *   *   *   *   *   Q   *   *  |  5
  6 |   *   Q   *   *   *   *   *   *  |  6
  7 |   *   *   *   *   Q   *   *   *  |  7
     ----------------------------------
        0   1   2   3   4   5   6   7 
```

## Prerequisites

- Any IDE, preferably VSCode.
- Python 3.10 and Jupyter package.
  - Alternatively, the `.ipynb` file can be run on Google Colab.

## Installation

- ***Do either one of these***:
  - Clone the repo.
  - Download just the `.ipynb` file then follow the instructions within.

## Built With

[vscodeicon]: https://skillicons.dev/icons?i=vscode&theme=dark
[vscodeurl]: https://code.visualstudio.com/

[pythonicon]: https://skillicons.dev/icons?i=py&theme=dark
[pythonurl]: https://www.python.org/

[jupytericon]: https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg
[jupyterurl]: https://code.visualstudio.com/docs/datascience/jupyter-notebooks

[windowsicon]: https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg
[windowsurl]: https://www.microsoft.com/en-us/windows/

| [![VSCode][vscodeicon]][vscodeurl] | [![Python][pythonicon]][pythonurl] | [![Jupyter][jupytericon]][jupyterurl] | [![Windows][windowsicon]][windowsurl] |
| :-: | :-: | :-: | :-: |
| 1.76.1 | 3.10.1 | VSCode | &nbsp;&nbsp; 10 &nbsp;&nbsp; |
