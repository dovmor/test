import base64

# Step 2: Define the content
content = "the password is: 123456"

# Step 3: Write the content to a text file
with open("password.txt", "w") as file:
    file.write(content)

# Step 4: Read the content from the file
with open("password.txt", "r") as file:
    file_content = file.read()

# Step 5: Encode the content using Base64
encoded_content = base64.b64encode(file_content.encode())

# Step 6: Write the encoded content to a new file
with open("encoded_password.txt", "wb") as file:
    file.write(encoded_content)