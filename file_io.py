import csv
import logging
from typing import Dict, Tuple
from exceptions import FileProcessingError

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_lookup_table(lookup_file: str) -> Dict[Tuple[str, str], str]:
    """
    Loads the lookup table from a CSV file.

    Args:
        lookup_file (str): Path to the CSV file containing the lookup table.

    Returns:
        Dict[Tuple[str, str], str]: A dictionary mapping (dstport, protocol) tuples to tags.
    """
    lookup = {}
    logging.debug(f"Loading lookup table from {lookup_file}")
    try:
        with open(lookup_file, mode='r', encoding='ascii') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = (row['dstport'].strip(), row['protocol'].strip().lower())
                lookup[key] = row['tag'].strip()
        logging.info("Lookup table loaded successfully.")
    except FileNotFoundError as e:
        raise FileProcessingError(f"Lookup file not found: {e}")
    except Exception as e:
        raise FileProcessingError(f"Failed to load lookup table: {e}")
    return lookup


def write_output(tag_counts: Dict[str, int], combination_counts: Dict[Tuple[str, str], int], output_file: str) -> None:
    """
    Writes the tag and port/protocol combination counts to a single output file.

    Args:
        tag_counts (Dict[str, int]): A dictionary mapping tags to counts.
        combination_counts (Dict[Tuple[str, str], int]): A dictionary mapping (port, protocol) tuples to counts.
        output_file (str): Path to the output file.
    """
    try:
        with open(output_file, mode='w', encoding='ascii') as file:
            file.write("Tag Counts:\n")
            file.write("Tag\t\tCount\n")
            for tag, count in tag_counts.items():
                if tag == "Untagged":
                    file.write(f"{tag}\t{count}\n")
                else:
                    file.write(f"{tag}\t\t{count}\n")

            file.write("\nPort/Protocol Combination Counts:\n")
            file.write("Port\tProtocol\tCount\n")
            for (port, protocol), count in combination_counts.items():
                file.write(f"{port}\t\t{protocol}\t\t\t{count}\n")
        logging.info("Output file written successfully.")
    except Exception as e:
        logging.error(f"Failed to write output file: {e}")