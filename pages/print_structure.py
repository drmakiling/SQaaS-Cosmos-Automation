import os

def print_directory_structure(root_dir):
    """
    Prints the directory structure starting from root_dir.
    """
    for root, dirs, files in os.walk(root_dir):
        # Calculate the level of the directory
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[DIR] {os.path.basename(root)}')
        for file in files:
            print(f'{indent}    {file}')

if __name__ == "__main__":
    # Set the root directory to your project root
    project_root = '/home/kgirard-admin/Downloads/learning-Automation-RT-master'  # Set this to your actual project root directory
    print_directory_structure(project_root)
