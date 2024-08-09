# assessment-Illumio

This project contains the code for processing flow log files along with lookup file to get the following 2 outputs:
1. Count of matches for each tag.
2. Count of matches for each port/protocol combination.

## The project structure is as given below:

**constants.py** - Contains all the constants and file path used in the assessment.
It contains a protocol map which has all the protocols excluding Reserved and unmapped protocols mentioned in https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

**exceptions.py** - Contains custom exception used while processing the files.

**file_io.py** - Contains functions which reads the lookup table file and is responsible for giving the final_output.txt file.

**final_output.txt** - Contains the final output required for the assessment. Currently output path is set to root directory which can be changes from constants.py

**main.py** - Main file which reads both the files and gives the final output.

**processing.py** - Processes specifically AWS VPC flow logs to get the Counts of tags and port/protocol combination. Ref: https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html

## Instructions:
1. Before running the program, update the file paths in constants.py file.
2. After that run main.py file to get the final_output.txt at your desired path.
