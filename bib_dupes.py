import re

def readBibFile(file_path):
    dois = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            entry_content = ''
            for line in file:
                if line.startswith('@'):
                    # When encountering a new entry, process the previous entry content
                    if entry_content:
                        doi = extractDOI(entry_content)
                        if doi:
                            dois.append(doi)
                        entry_content = ''  # Reset for next entry
                entry_content += line
            # Process the last entry
            if entry_content:
                doi = extractDOI(entry_content)
                if doi:
                    dois.append(doi)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return dois

def extractDOI(entry_content):
    # Regex pattern to find the DOI within the entry
    doi_pattern = re.compile(r'doi\s*=\s*[{"]([^}"]+)[}"]', re.IGNORECASE)
    match = doi_pattern.search(entry_content)
    if match:
        return match.group(1).strip()
    return None

def findDuplicates(dois):
    seen = set()
    duplicates = set()

    for doi in dois:
        if doi in seen:
            duplicates.add(doi)
        else:
            seen.add(doi)

    return list(duplicates)

def main():
    # Replace 'yourfile.bib' with the path to your .bib file
    file_path = 'C:\\Users\\Logan Ritter\\Downloads\\xe_kr_hkust-abbrev.bib'
    dois = readBibFile(file_path)

    if dois:
        duplicates = findDuplicates(dois)
        if duplicates:
            print("Duplicate DOIs found:")
            for dupe in duplicates:
                print(dupe)
        else:
            print("No duplicate DOIs found.")
    else:
        print("No DOIs found in the file.")

if __name__ == "__main__":
    main()
