#!/bin/bash

# Function to update STATUS.md
update_status_md() {
  demo_dir=$1
  status_file="demos/$demo_dir/STATUS.md"
  readme_file="demos/$demo_dir/README.md"
  project_name=$demo_dir
  creator="Riccardo Carlesso"
  github_username="palladius"
  created_date=$(date +%Y-%m-%d)
  demo_purpose=$(grep -m 1 "^## " "$readme_file" | sed 's/## //')

  # Create or update STATUS.md
  echo "## $project_name" > "$status_file"
  echo "" >> "$status_file"
  echo "* Created: $created_date" >> "$status_file"
  echo "* Creator: $creator" >> "$status_file"
  echo "* GitHub username: $github_username" >> "$status_file"
  echo "* Creator fav ice-cream: ..." >> "$status_file"
  echo "* status: WorkInProgress" >> "$status_file"
  echo "* Checkbox:" >> "$status_file"
  echo "    * [ ] code_present" >> "$status_file"
  echo "    * [ ] code_working" >> "$status_file"
  echo "    * [ ] code_test" >> "$status_file"
  echo "    * [ ] license_headers" >> "$status_file"
  echo "    * [ ] documentation" >> "$status_file"
  echo "    * [ ] video" >> "$status_file"
  echo "* Demo purpose: $demo_purpose" >> "$status_file"
  echo "* Time to execute: **XX** minutes" >> "$status_file"
}

# Function to update main README.md
update_main_readme() {
  readme_file="README.md"
  temp_readme="README.md.tmp"
  table_start_pattern="| Status | Author | Demo Folder | Category | Description |"
  table_end_pattern="<!-- end-demos -->"
  
  # Copy content before the table
  sed "/$table_start_pattern/q" "$readme_file" > "$temp_readme"
  
  # Add the table header
  echo "$table_start_pattern" >> "$temp_readme"
  echo "|---|---|---|---|---|" >> "$temp_readme"

  # Add a row for each demo
  for demo_dir in demos/*/; do
    demo_name=$(basename "$demo_dir")
    status_file="demos/$demo_name/STATUS.md"
    status=$(grep "status:" "$status_file" | awk '{print $2}')
    creator=$(grep "Creator:" "$status_file" | cut -d':' -f2- | xargs)
    demo_purpose=$(grep "Demo purpose:" "$status_file" | cut -d':' -f2- | xargs)
    status_emoji="🚧" # Default to WorkInProgress

    case $status in
      "SignedOff") status_emoji="🔝" ;;
      "Complete") status_emoji="✅" ;;
      "Draft") status_emoji="📝" ;;
      "NotStarted") status_emoji="🫙" ;;
    esac

    echo "| $status_emoji | $creator | フォルダ [$demo_name/](demos/$demo_name/) | ... | $demo_purpose |" >> "$temp_readme"
  done
  
  # Add the end of table marker
  echo "$table_end_pattern" >> "$temp_readme"

  # Copy content after the table
  sed "1,/$table_end_pattern/d" "$readme_file" >> "$temp_readme"

  # Replace the old README with the new one
  mv "$temp_readme" "$readme_file"
}

# Main script
for demo_dir in demos/*/; do
  demo_name=$(basename "$demo_dir")
  echo "Updating STATUS.md for $demo_name..."
  update_status_md "$demo_name"
done

echo "Updating main README.md..."
update_main_readme

echo "Done."
