# Medico
<p align="center">
  <img width="300" height="300" src="/img/medico_round.png">
</p>

**Medico:- Medico is a medical terms detection system via your Voice.**

# Current stable versions
[![Alt v1.0](https://img.shields.io/badge/release--1.0-ok-green.svg)](https://github.com/pranayjoshi/Medico/releases/tag/1.0)  ![licence](https://img.shields.io/github/license/pranayjoshi/Medico) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpranayjoshi%2FMedico&count_bg=%23DD8524&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=visitors&edge_flat=false)](https://github.com/pranayjoshi/medico) ![stars](https://img.shields.io/github/stars/pranayjoshi/Medico) ![forks](https://img.shields.io/github/forks/pranayjoshi/Medico) ![issues](https://img.shields.io/github/issues/pranayjoshi/Medico) [![tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fpranayjoshi%2FMedico)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fpranayjoshi%2FMedico)
# Installation
**Run these commands on Terminal/CMD/bash dpending on your OS**
* run ``` git clone https://github.com/pranayjoshi/Medico```. This will clone the Repo to your local system.
* than run ``` cd Medico``` .This will set Medico as your present directory.

## Installing Dependencies
### 1. Windows Users
* **BASH Installed**
  * Run the following command to install the dependencies required:- ```./install.sh```
* **BASH not Installed**
  * Just run the setup.py by ``` pip install -r requirements.txt ``` or ``` pip3 install -r requirements.txt``` depending on the pip version.
  * Install pyaudio by ``` pip install install/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl ```.
### 2. Mac OSX USers
* Run the following command to install the dependencies required:- ```./mac_install.sh```
### 3. Debian based Linux Users( Ubuntu, Mint etc..)
* Run the following command to install the dependencies required:- ```./debian_install.sh```
### 4. For NIX Users
* Run the following command to install the dependencies required:- ```./install.sh```

**Dependencies for **Medico** has succesfully installed on your system.**

## Running Files
### 1. Python Scripts/Commands
* To run the software use:- ```python3 run.py``` or ```python run.py``` based on your python version.
* To run the tests use:- ```python3 RunTests.py``` or ```python RunTests.py``` based on your python version.
* Start Conversing after you hear ``` I am ready for your command ```.
### 2. Bash Scripts/Commands
* To run the software use:- ```./start.sh```.
* To run the software use:- ```./runtest.sh```.
* Start Conversing after you hear ``` I am ready for your command ```.

# Description
* A software that recognize medical terms
* Dataset used:- Snomed international(Sample)

# Working.
* Takes the **Medical Conversation**(Mainly between Doctor and Patient) as the input.
* Use that Voice Conversation and Convert it to text using **Speech To Text**.
* Than the **fetch_recent.py** takes the file containg all the conversation and returns the latest conversation.
* After that the **Punctuator Model** takes the latest conversation and does the **Magic**(adds the punctuations) to the conversation.
* Than we use the **Punctuated Conversation** and the whole conversation/document gets divided into particular sentences, by the **Sentence Tokenizer Model**.
* After that we use the **Tokenized Sentence**, and check them One by One wheter they are **Medical Sentences**(Contains Medical Terms) or not.
* If they are considered Medical Statements than:-
  * The **Medical Term Detection Model** starts. It Further divides those **Medical Sentences** into **100000+ Categories.**
  * After that a **Printer Function** prints all the necessary details.
* Otherwise the sentence is Skipped.
* At Last a Final Report is printed, Displaying all the **Medical Terms** found in the **Whole Conversation.**

## Thank you
