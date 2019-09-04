# FreqObjectOps
Some special functions for some python objects.

## Requirements

* Python 3+ (Tested in 3.7)
* pandas>=0.25.0
* pytest>=5.0.1
* Unidecode>=1.0.22


## Install with pip
```bash
$ pip install FreqObjectOps
```

## Usage
1. Import the library.
    ```python
    from FreqObjectOps import DateOps, DirOps, ListOps, StrOps
    ```
1. Each of the imported submodules has several functions. Please refer to respective help for more information.

#### ```DateOps```
1. ```DateOps.get_year(date_entity, date_format)```: get year from date
1. ```DateOps.text_to_datetime(text, date_format)```: convert text to date
1. ```DateOps.get_difference_in_year(from_date, to_date, date_format)```: get corrected year-difference between two dates
    
#### ```DirOps```
1. ```DirOps.get_directory_from_filepath(filepath)```: get directory from a filepath
1. ```DirOps.get_basename_from_filepath(filepath)```: get basename from filepath
1. ```DirOps.get_file_extension_from_filepath(filepath)```: get file extension from a file
1. ```DirOps.exists_folder(folder_path)```: check if folder exists
1. ```DirOps.get_filtered_list_without_temporary_files(file_list)```: filter temporary files from a list of files
1. ```DirOps.get_all_files_in_directory(folder_path, pattern, recursive)```: get all files in a directory that matches certain pattern
1. ```DirOps.get_latest_file_in_directory(folder_path, pattern)```: get latest file in a directory that matches certain pattern
1. ```DirOps.get_abs_path(filepath)```: get absolute path for a filepath
1. ```DirOps.get_norm_path(filepath)```: get normalized path for a filepath

#### ```ListOps```
1. ```ListOps.remove_duplicates(unfiltered_list, sorted, reversed)```: get filtered list with unique elements
1. ```ListOps.get_intersection(list_one, list_two)```: get common elements between two lists
1. ```ListOps.get_union(list_one, list_two)```: get all elements between two lists
1. ```ListOps.get_flat_list(list_of_lists)```: get flattened list

#### ```StrOps```
1. ```StrOps.is_camel_case(text)```: check if text is in camelCase
1. ```StrOps.remove_accent(text)```: remove accent from text
1. ```StrOps.clean_snake_case(text)```: clean snake case
1. ```StrOps.text_to_alpha_numeric(text, replace_string)```: remove non-alphanumeric characters from text
1. ```StrOps.text_to_camel_case(text, case)```: convert text to camelCase
1. ```StrOps.camel_case_to_snake_case(text, case)```: convert camelCase to snake_case
1. ```StrOps.text_to_snake_case(text, case)```: convert text to snake_case


## Author

* **&copy; Samyak Ratna Tamrakar** - [Github](https://github.com/srtamrakar), [LinkedIn](https://www.linkedin.com/in/srtamrakar/).