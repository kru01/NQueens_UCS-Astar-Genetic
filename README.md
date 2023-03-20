<a name="readme-top"></a>

# NQueens with USC, A* and Genetic Algorithm

- Lab homework from HCMUS's 2023 Introduction to AI course.

<details open>
  <summary>Table of Contents</summary>
  <ul>
    <li>
      <a href="#content">Content</a>
      <ul>
        <li>
          <a href="#ucs-and-a">UCS and A*</a>
          <ul>
            <li><a href="#complete-state-formulation">Complete-state formulation</a></li>
            <li><a href="#incremental-formulation">Incremental formulation</a></li>
          </ul>
        </li>
        <li><a href="#genetic-algorithm">Genetic Algorithm</a></li>
      </ul>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#built-with">Built With</a></li>
  </ul>
</details>

## Content

- Read the attached pdf for full details.

### UCS and A*

- There are 2 versions of the handleSearch function, one has `expanded` as a `list` and the other a `set`.
   - The `list` version runs slower but saves more memory while the `set` one is the exact opposite.
   - UCS should always use the latter, otherwise it will literally take ***an eternity*** to find a solution, especially in Complete-state formulation.

#### Complete-state formulation
- Initially, all queens are placed on random rows. Each column is occupied by exactly one queen.
- The solution varies depending on the initial state.
- UCS takes ***very long*** to find a solution.
```text
Input queens and algo: 8 2
Place queens incrementally? (0 for random initial state): 0
Initial state: [3, 5, 6, 4, 7, 1, 7, 7]    
   
        0   1   2   3   4   5   6   7      
     ----------------------------------    
  0 |   *   *   *   *   *   *   *   *  |  0
  1 |   *   *   *   *   *   Q   *   *  |  1
  2 |   *   *   *   *   *   *   *   *  |  2
  3 |   Q   *   *   *   *   *   *   *  |  3
  4 |   *   *   *   Q   *   *   *   *  |  4
  5 |   *   Q   *   *   *   *   *   *  |  5
  6 |   *   *   Q   *   *   *   *   *  |  6
  7 |   *   *   *   *   Q   *   Q   Q  |  7
     ----------------------------------
        0   1   2   3   4   5   6   7
   
--8 Queens A*--
Execution time:         47.0000 ms
Memory usage:            0.2720 MB
Solution: [2, 0, 6, 4, 7, 1, 3, 5]

        0   1   2   3   4   5   6   7
     ----------------------------------
  0 |   *   Q   *   *   *   *   *   *  |  0
  1 |   *   *   *   *   *   Q   *   *  |  1
  2 |   Q   *   *   *   *   *   *   *  |  2
  3 |   *   *   *   *   *   *   Q   *  |  3
  4 |   *   *   *   Q   *   *   *   *  |  4
  5 |   *   *   *   *   *   *   *   Q  |  5
  6 |   *   *   Q   *   *   *   *   *  |  6
  7 |   *   *   *   *   Q   *   *   *  |  7
     ----------------------------------
        0   1   2   3   4   5   6   7
```
#### Incremental formulation
- Initially, all queens are placed on row -1. Each column is occupied by exactly one queen.
- The solution for a specific N will always be the same no matter how many times it's run.
```text
Input queens and algo: 8 2
Place queens incrementally? (0 for random initial state): 1
--8 Queens A*--
Execution time:         15.0000 ms
Memory usage:            0.0559 MB
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>
