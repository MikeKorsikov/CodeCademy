# QuickNote - Simple Command-Line Note Taker

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md) [![Version](https://img.shields.io/badge/version-v0.1.0-blue)](#) A lightweight command-line utility for quickly jotting down and retrieving plain text notes. Notes are stored locally in a simple directory structure.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

* **Add:** Quickly add new notes with titles.
* **List:** List all existing notes.
* **Show:** Display the content of a specific note.
* **Delete:** Remove a note.
* **Search:** Basic text search within note content (planned).
* Plain text storage (easy to backup and read manually).
* Simple command-line interface.

## Installation

### Prerequisites

* Python 3.7+
* `pip` (Python package installer)

### Steps

1.  **Clone the repository (optional):**
    If you want to install from source or contribute:
    ```bash
    git clone [https://github.com/yourusername/quicknote.git](https://github.com/yourusername/quicknote.git) # Replace with actual repo URL
    cd quicknote
    ```

2.  **Install via pip:**
    *(Assuming the package is available on PyPI or you are in the cloned directory)*
    ```bash
    # For installation from PyPI (if published)
    pip install quicknote

    # For local installation from cloned source
    pip install .
    ```

## Usage

QuickNote is run from the command line using the `quicknote` command followed by subcommands and arguments.

```bash
quicknote [COMMAND] [ARGUMENTS]