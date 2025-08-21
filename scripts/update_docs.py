import os
import re
from datetime import datetime

def get_demo_dirs():
    """Returns a list of demo directories."""
    return [d for d in os.listdir('demos') if os.path.isdir(os.path.join('demos', d))]

def get_status_path(demo_dir):
    """Returns the path to the STATUS.md file for a demo."""
    return os.path.join('demos', demo_dir, 'STATUS.md')

def get_readme_path(demo_dir):
    """Returns the path to the README.md file for a demo."""
    return os.path.join('demos', demo_dir, 'README.md')

def get_gemini_path(demo_dir):
    """Returns the path to the GEMINI.md file for a demo."""
    return os.path.join('demos', demo_dir, 'GEMINI.md')

def parse_status_file(status_path):
    """Parses a STATUS.md file and returns a dictionary of its contents."""
    status = {}
    if not os.path.exists(status_path):
        return status

    with open(status_path, 'r') as f:
        content = f.read()

    # This is a simple parser, it might not cover all edge cases.
    for line in content.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            status[key.strip()] = value.strip()
        elif '##' in line:
            status['Project name'] = line.replace('##', '').strip()

    return status

def get_git_info(demo_dir):
    """Gets information from git about the demo."""
    # In a real-world scenario, you'd use a git library for this.
    # For this example, we'll use some dummy data.
    return {
        'Creator': 'Riccardo Carlesso',
        'GitHub username': 'palladius',
        'Created': '2025-08-21',
    }

def get_demo_purpose(readme_path):
    """Gets the demo purpose from the README.md file."""
    if not os.path.exists(readme_path):
        return '...'

    with open(readme_path, 'r') as f:
        # This is a simple implementation. A more robust solution would parse the markdown.
        for line in f:
            if line.startswith('## '):
                return line.replace('## ', '').strip()
    return '...'


def update_status_file(demo_dir):
    """Creates or updates the STATUS.md file for a demo."""
    status_path = get_status_path(demo_dir)
    readme_path = get_readme_path(demo_dir)
    status = parse_status_file(status_path)
    git_info = get_git_info(demo_dir)

    # Update status with new information
    status['Project name'] = f'## {demo_dir}'
    status['Created'] = status.get('Created', git_info['Created'])
    status['Creator'] = status.get('Creator', git_info['Creator'])
    status['GitHub username'] = status.get('GitHub username', git_info['GitHub username'])
    status['Creator fav ice-cream'] = status.get('Creator fav ice-cream', '...')
    status['status'] = status.get('status', 'WorkInProgress')
    status['Demo purpose'] = get_demo_purpose(readme_path)
    status['Time to execute'] = status.get('Time to execute', '**XX** minutes')


    # Write the updated status file
    with open(status_path, 'w') as f:
        f.write(f"## {status['Project name']}\n\n")
        f.write(f"* Created: {status['Created']}\n")
        f.write(f"* Creator: {status['Creator']}\n")
        f.write(f"* GitHub username: {status['GitHub username']}\n")
        f.write(f"* Creator fav ice-cream: {status['Creator fav ice-cream']}\n")
        f.write(f"* status: {status['status']}\n")
        f.write("* Checkbox:\n")
        f.write("    * [ ] code_present\n")
        f.write("    * [ ] code_working\n")
        f.write("    * [ ] code_test\n")
        f.write("    * [ ] license_headers\n")
        f.write("    * [ ] documentation\n")
        f.write("    * [ ] video\n")
        f.write(f"* Demo purpose: {status['Demo purpose']}\n")
        f.write(f"* Time to execute: {status['Time to execute']}\n")


def update_main_readme(demo_dirs):
    """Updates the main README.md file with a table of demos."""
    readme_path = 'README.md'
    with open(readme_path, 'r') as f:
        content = f.read()

    # Find the table of demos
    table_start = content.find('| Status | Author | Demo Folder | Category | Description |')
    table_end = content.find('<!-- end-demos -->')

    if table_start == -1 or table_end == -1:
        print("Could not find the table of demos in README.md")
        return

    # Generate the new table
    table = '| Status | Author | Demo Folder | Category | Description |\n'
    table += '|---|---|---|---|---|
'
    for demo_dir in demo_dirs:
        status_path = get_status_path(demo_dir)
        status = parse_status_file(status_path)
        status_emoji = {
            'SignedOff': '🔝',
            'Complete': '✅',
            'Draft': '📝',
            'WorkInProgress': '🚧',
            'NotStarted': '🫙',
        }.get(status.get('status'), '🚧')

        table += f"| {status_emoji} | {status.get('Creator', '...')} | フォルダ [{demo_dir}/](demos/{demo_dir}/) | {status.get('category', '...')} | {status.get('Demo purpose', '...')} |\n"

    # Replace the old table with the new one
    new_content = content[:table_start] + table + content[table_end:]
    with open(readme_path, 'w') as f:
        f.write(new_content)


if __name__ == '__main__':
    demo_dirs = get_demo_dirs()
    for demo_dir in demo_dirs:
        print(f"Updating STATUS.md for {demo_dir}...")
        update_status_file(demo_dir)

    print("Updating main README.md...")
    update_main_readme(demo_dirs)
    print("Done.")
