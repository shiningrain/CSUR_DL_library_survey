# A Survey of Deep Learning Library Testing Methods

## TL;DR

This paper provides an overview of the testing research related to various DL libraries, discusses the strengths and weaknesses of existing methods, and provides guidance and reference for the application of the DL library.
In this paper, we have collected 8 state-of-the-art open-sourced testing methods using different testing techniques (i.e., [Muffin](https://github.com/library-testing/Muffin), [FreeFuzz](https://github.com/ise-uiuc/FreeFuzz), [DocTer](https://github.com/lin-tan/DocTer), [DeepREL](https://github.com/ise-uiuc/DeepREL), [TitanFuzz](https://github.com/ise-uiuc/TitanFuzz), [Muffin-TVM](https://github.com/wzh99/GenCoG/tree/master/muffin), [Tzer](https://github.com/Tzer-AnonBot/tzer), [GenCoG](https://github.com/wzh99/GenCoG)) and compared their effects on DL frameworks TensorFlow (2.7.0) and PyTorch (1.10.0), as well as DL compiler TVM (0.8.0).

This repository provides more details on experiment setting, results, and other open-source data (such as collected papers) of our survey as supplement materials.



## Repo Structure

```                 
- Supplimental_Materials/
    - Experiment_Results
    - PaperList.xlsx
- README.md  
```

## Experiment Setting and Results

### Setting
All experiments are conducted on a server with Intel(R) Xeon(R) Gold 6226R 2.90GHz 16-core processors, 130 GB of RAM, and an NVIDIA L40 GPU running on Ubuntu 22.04.
In experiments, all testing methods use the configurations and instructions recommended by their repositories.
Following the experiments of existing work([1](https://dl.acm.org/doi/10.1145/3527317),[2](https://arxiv.org/pdf/2109.01002)), we run compiler testing methods for 4 hours and framework testing methods for 48 hours to ensure that each method thoroughly explored the behavior of the DL library.

### Metrics
In our experiments, we recorded two metrics: 1)coverage and 2)testing results.
The experiment results are stored in this [directory](./Supplimental_Materials/Experiment_Results).

1. **Coverage**: For DL frameworks that provide user-friendly APIs, following the settings of [prior testing research](https://arxiv.org/abs/2212.14834), we record API coverage of DL framework testing methods.
For DL compilers, we follow [prior work](https://dl.acm.org/doi/10.1145/3527317) to count line coverage of DL compiler testing methods.
2. **Testing Results**: To compare their testing results, we count the number of bug candidates reported by each testing method, which is the final detection output we could find.
Specifically, the final outputs of DL libary testing methods like DocTer, DeepRel, FreeFuzz, Muffin, Tzer, and GenCoG provide directories or files named `bugs` or `potential bugs`.
We directly counted the number of cases/files in these directories as bug candidates.
TitanFuzz captures five types of candidates based on different test oracles in tests, namely `VarTypeConflictCatch`,`VarInconsistentCatch`,`ExecStateCatch`,`FrameworkCrashCatch`,`ExceptMsgCatch`, and we count the number of these captured cases.
Muffin-TVM throws exceptions when TVM could not execute the given test cases converted from DL models (i.e., crash bug).
We counted the number of these crashed cases.

## Collected Papers

We have collected 93 papers in the literature collection, where 69 of them are related to DL framework testing, 12 are related to DL compiler testing and 13 are related to DL hardware library testing.
Paper list is in this [file](./Supplimental_Materials/PaperList.xlsx).
