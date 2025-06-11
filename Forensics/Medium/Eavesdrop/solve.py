# Extract and clean up the actual payload portion from the hexstream
full_hexstream = (
    "08002793ce73080027af399f080045000064ac904000400675f10a00020f0a000204"
    "dc32232a5ea28bc7405f546d801801f6186900000101080ad1a793f469410c675361"
    "6c7465645f5f3c4b26e8b8f91e2c4af8031cfaf5f8f16fd40c25d40314e6497b3937"
    "5808aba186f48da42eefa895"
)

# Find start of OpenSSL encrypted data (starts with "Salted__" = 53 61 6c 74 65 64 5f 5f)
start_marker = "53616c7465645f5f"
start_index = full_hexstream.find(start_marker)
assert start_index != -1, "Salted__ marker not found"

# Take from Salted__ onward
cleaned_hex = full_hexstream[start_index:]

# Convert to binary and save
binary_data = bytes.fromhex(cleaned_hex)
binary_path = "/mnt/data/extracted_stream.des3"
with open(binary_path, "wb") as f:
    f.write(binary_data)

# Decrypt with OpenSSL
decrypted_path = "/mnt/data/extracted_stream_decrypted.txt"
password = "supersecretpassword123"

result = subprocess.run([
    "openssl", "des3", "-d",
    "-salt",
    "-in", binary_path,
    "-out", decrypted_path,
    "-k", password
], capture_output=True, text=True)

# Output result
if result.returncode == 0:
    output = Path(decrypted_path).read_text()
else:
    output = f"ERROR: {result.stderr}"

output.strip()
