import os
import re
import argparse


# Pattern to replace _descriptor_pool.Default() with {CHAIN}_DESCRIPTOR_POOL
pattern = re.compile(r"_descriptor_pool\.Default\(\)")


def modify_proto_files(directory: str, chain: str):
    print(directory, chain)
    for root, _, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(".py") or "grpc" in filename:
                continue

            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            # Replace default pool with custom pool
            modified_content = pattern.sub(f"{chain}_DESCRIPTOR_POOL", content)

            custom_import = f"from pyinjective.proto.descriptor import {chain}_DESCRIPTOR_POOL"
            # Add custom pool import if not already present
            if custom_import not in modified_content:
                modified_content = f"{custom_import}\n{modified_content}"

            # Write back modified content
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(modified_content)
            print(f"Modified {filename}")


def main():
    parser = argparse.ArgumentParser(description="Modify Protobuf Python files to use a custom DescriptorPool.")
    parser.add_argument(
        "-c",
        "--chain",
        type=str,
        required=True,
        help="Chain name to specify the DescriptorPool (e.g., injective, osmosis)",
    )
    args = parser.parse_args()

    # Run the modification
    modify_proto_files("pyinjective/proto", args.chain.upper())


if __name__ == "__main__":
    main()
