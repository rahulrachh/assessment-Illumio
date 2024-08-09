from collections import defaultdict
from typing import Dict, Tuple
import logging
from constants import Constants
from exceptions import FileProcessingError


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_flow_log(flow_log_file: str, lookup_table: Dict[Tuple[str, str], str]) -> Tuple[
    Dict[str, int], Dict[Tuple[str, str], int]]:
    """
    Processes the flow log file and generates tag and port/protocol combination counts.
    sample_flow_log fields are referenced from https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html
    According to the fields present in above link, in AWS VPS flow log, Destination port is present in 6th index and protocol position id 7th index.

    Args:
        flow_log_file (str): Path to the flow log file.
        lookup_table (Dict[Tuple[str, str], str]): A dictionary mapping (dstport, protocol) tuples to tags.

    Returns:
        Tuple[Dict[str, int], Dict[Tuple[str, str], int]]: A tuple containing dictionaries for tag counts and port/protocol combination counts.
    """
    tag_counts = defaultdict(int)
    combination_counts = defaultdict(int)

    try:
        with open(flow_log_file, mode='r', encoding='ascii') as file:
            for row in file:
                row = row.split()
                # print(row)
                if len(row) >= 14:
                    dstport = row[Constants.DSTPRT_POS].strip()
                    protocol_number = int(row[Constants.PROTOCOL_POS].strip())
                    protocol = Constants.PROTOCOL_MAP.get(protocol_number, '').lower()

                    combination_key = (dstport, protocol)
                    tag = lookup_table.get(combination_key, "Untagged")

                    tag_counts[tag] += 1
                    combination_counts[combination_key] += 1
                else:
                    raise FileProcessingError("Processing failed for row: ", row)
        logging.info("Flow log processed successfully.")
    except Exception as e:
        logging.error(f"Failed to process flow log: {e}")

    return tag_counts, combination_counts
