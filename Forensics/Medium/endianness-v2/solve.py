def reverse_endianness(input_path, output_path):
    with open(input_path, "rb") as f:
        data = f.read()

    reversed_data = bytearray()

    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        reversed_data.extend(chunk[::-1])  

    with open(output_path, "wb") as f:
        f.write(reversed_data)

    print(f"File selesai ditulis ke: {output_path}")

reverse_endianness("challengefile", "fixed_output.jpg")

