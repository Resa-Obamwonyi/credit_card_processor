# Basic Credit Card Processing
This program will add new credit card accounts, process charges and credits against them, and display summary information.

## Design Descisions
- A major design principle I attempted to communicate in this task is that "simple is better". I understood that since this was a standard read and write of input, there was no need for an actual database for long term storage. 
- I proceeded to mimic a database model using python, this kept my logic simple, precise and clear.
- I chose to use python because of the simplicity and accessibility it provides and because of my familiarity and comfort with the language.
### Technologies Used
- Python 3 and a few of its inbuilt libraries.

### How to Run the program
#### Test with txt file
- To run the program with a txt file, in the root of the working directory, run `python3 main.py file_name.txt` (please ensure your file is in the root directory also, or specify the path e.g `python3 main.py  path_to_file/file_name.txt`), there is also a test txt file available named `data.txt`, you can run `python3 main.py data.txt` to test with that.
#### Test with input
- To run the program with direct input, run `python3 main.py` and paste or write all your transactions and then `CTRL-D` (Mac) or `CTRL-Z followed by <return>` (Windows) to signify End of File or Writing. 

### How to Run tests
- To run tests use the command `python3 -m unittest discover` or `python3 -m unittest test_program.py`