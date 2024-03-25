# Stable Matching Algorithm

This repository contains an implementation of the Gale-Shapley algorithm to solve the stable matching problem, commonly applied in scenarios like matching candidates to hospitals or students to schools based on mutual preferences.

## Overview

The stable matching problem seeks to find a stable match between two sets of elements given a set of preferences for each element. A match is considered stable if there are no two elements that would prefer each other over their current partners. This implementation focuses on a basic variation of the Gale-Shapley algorithm to match an equal number of hospitals and candidates based on their preferences.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system to run the script. This code has been tested with Python 3.8, but it should be compatible with most Python 3.x versions.

### Installation

Clone this repository to your local machine to get started:

```bash
git clone https://github.com/Radfahrer00/Stable-Matching.git
cd Stable-Matching
```

Run the program:

```bash
python stable_matching.py
```

## Customization
To customize the input preferences for the hospitals and candidates, modify the prefer list in the stable_matching.py file. This list contains the preferences of hospitals and candidates, where the first N lists are the preferences of hospitals over candidates, followed by N lists of candidates' preferences over hospitals.

Ensure that the preference list is complete for each participant and accurately reflects their ranking of all possible matches.
