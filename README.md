# nanoGPT x Friends: Generating Friends TV Show Episodes with NanoGPT

Welcome to the nanoGPT x Friends project! This repository reviews and implements the concepts from the seminal "Attention is All You Need" paper, where the Transformer architecture was introduced. Following Andrej Karpathy's YouTube series, we adapt these ideas to create a nanoGPT model trained on the Friends TV Show Script dataset to generate new episodes.

## Table of Contents

-   [Introduction](#introduction)
-   [Dataset](#dataset)
-   [Model Architecture](#model-architecture)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Results](#results)
-   [Acknowledgements](#acknowledgements)
-   [License](#license)

## Introduction

This project aims to explore and apply the principles of the Transformer model as described in the "Attention is All You Need" paper. We follow the tutorial series by Andrej Karpathy to build a simplified version of the GPT model, dubbed nanoGPT. The model is then trained on scripts from the Friends TV show to generate new, realistic episodes.

## Dataset

We use the Friends TV Show Script dataset from Kaggle, which contains the scripts from all 10 seasons of the show. The dataset is available [here](https://www.kaggle.com/datasets/divyansh22/friends-tv-show-script).

## Model Architecture

The nanoGPT model follows the architecture of the original Transformer with several layers of encoder-decoder structures. Key components include:

-   Multi-Head Self-Attention Mechanism
-   Positional Encoding
-   Feed-Forward Neural Networks
-   Layer Normalization and Dropout

## Installation

To set up the environment and install necessary dependencies, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/nanoGPT-x-Friends.git
    cd nanoGPT-x-Friends
    ```

## Usage

## Results

The generated scripts aim to mimic the style and humor of the original Friends episodes. Sample outputs and evaluation metrics will be added here after training the model.

## Acknowledgements

-   **Transformers**: Vaswani et al. (2017), "Attention is All You Need" [link](https://arxiv.org/abs/1706.03762).
-   **nanoGPT**: Andrej Karpathy's YouTube series on building GPT from scratch [link](https://www.youtube.com/watch?v=kCc8FmEb1nY).
-   **Dataset**: Friends TV Show Script dataset from Kaggle [link](https://www.kaggle.com/datasets/divyansh22/friends-tv-show-script).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

We hope you find this project insightful and useful! Feel free to contribute by opening issues or submitting pull requests. For any questions, contact Ignacio Correcher at [ignaciocorrecher@hotmail.com].
