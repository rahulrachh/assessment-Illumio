from constants import Constants
from file_io import load_lookup_table, write_output
from processing import process_flow_log

def main() -> None:
    """
    Main function to execute the processing of flow logs and output results.
    """

    lookup_table = load_lookup_table(Constants.LOOKUP_FILE_PATH)
    tag_counts, combination_counts = process_flow_log(Constants.FLOW_LOG_FILE_PATH, lookup_table)
    write_output(tag_counts, combination_counts, Constants.OUTPUT_FILE_PATH)

if __name__ == "__main__":
    main()
