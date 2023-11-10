import argparse
from pathlib import Path 
from shutil import copyfile 
from concurrent.futures import ThreadPoolExecutor
import logging

parser = argparse.ArgumentParser(description='App for sorting folder') 
parser.add_argument('-s', '--source', help="Source folder", required=True) 
parser.add_argument('-o', '--output', default='dist') 
args = vars(parser.parse_args())  # object -> dict
source = args.get('source') 
output = args.get('output')

def grabs_folder(path: Path): 
    folders = [el for el in path.iterdir() if el.is_dir()]
    with ThreadPoolExecutor() as executor:
        executor.map(grabs_folder, folders)
    return folders

def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_file(): 
            ext = el.suffix
            new_path = output_folder / "dist" / ext
            try:
                new_path.mkdir(parents=True, exist_ok=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logging.error(e)

if __name__ == "__main__":        
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s") 
    base_folder = Path(source) 
    output_folder = Path(output)

    folders = [base_folder]  # Initialize the list with the base folder
    folders.extend(grabs_folder(base_folder))

    print(folders)  # Print the list of folders before sorting

    with ThreadPoolExecutor() as executor:
        executor.map(sort_file, folders)

    print('Sorting completed. Check the "dist" folder in the specified output directory.')
