from pathlib import Path  # type: ignore[import]

directory = '.'
output_file = 'sum.md'


def merge_markdown_files(directory: str, output_file: str) -> None:
  """Merges the content of all markdown files in the specified directory into a single file."""
  with Path(output_file).open('w', encoding='utf-8') as merged_file:
    for file_path in Path(directory).iterdir():
      if file_path.suffix == '.md' and file_path.name != '00_Summary.md' and not file_path.name.startswith('merged_'):
        with Path(file_path).open(encoding='utf-8') as file:
          merged_file.write(file.read())
          merged_file.write('\n\n')

  print(f"All markdown content has been merged into '{output_file}'")


merge_markdown_files(directory, output_file)
