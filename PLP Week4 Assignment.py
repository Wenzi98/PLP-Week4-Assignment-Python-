
# Get the filename from the user
filename = input("Enter the filename to read (e.g., notes.txt): ")

try:
    # Read the original file
    with open(filename, "r") as file:
        original_content = file.read()  # Read existing content
    print("Current content:\n" + original_content)

    # Get new content from the user
    new_content = input("\nEnter new content to add: ")

    # Combine old and new content
    modified_content = original_content + "\n" + new_content

    # Create a new filename (e.g., "notes_modified.txt")
    if "." in filename:
        name_part, extension = filename.split(".", 1)  # Split at the first dot
        new_filename = f"{name_part}_modified.{extension}"
    else:
        new_filename = f"{filename}_modified"

    # Save to the new file
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"\n✅ Success! Modified content saved to: {new_filename}")

except FileNotFoundError:
    print(f"\n❌ Error: The file '{filename}' doesn't exist!")
except Exception as e:
    print(f"\n❌ Something went wrong: {str(e)}")