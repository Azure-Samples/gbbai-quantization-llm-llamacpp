import os
import subprocess
import argparse
import logging
import shutil
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def clone_repo(
    repo_url="https://github.com/ggerganov/llama.cpp", target_dir="llama.cpp"
):
    """
    Clones a git repository into the specified directory.

    Parameters:
    repo_url (str): The URL of the repository to clone.
    target_dir (str): The directory where the repository should be cloned.
    """
    subprocess.run(["git", "clone", repo_url, target_dir], check=True)


def build_project():
    """Build the project using make in the llama.cpp directory."""
    logging.info("Building the project...")
    subprocess.run(["cmake", "-B", "build"], cwd="llama.cpp", check=True)
    subprocess.run(
        ["cmake", "--build", "build", "--config", "Release"],
        cwd="llama.cpp",
        check=True,
    )


def quantize_model(quantized_model_path, method):
    """Quantize the model using the specified method."""
    logging.info("Quantizing the model...")
    qtype = f"{quantized_model_path}/{method.upper()}.gguf"
    subprocess.run(
        [
            "./build/bin/llama-quantize",
            f"{quantized_model_path}/FP16.gguf",
            qtype,
            method,
        ],
        cwd="llama.cpp",
        check=True,
    )


def show_files_in_directory(directory_path):
    """Show all files in the specified directory."""
    logging.info(f"Files in {directory_path}:")
    if os.path.exists(directory_path):
        for entry in os.listdir(directory_path):
            logging.info(f" - {entry}")
    else:
        logging.warning(f"{directory_path} does not exist.")


def convert_model_to_gguf(original_model_path, quantized_model_path):
    """Convert the model to gguf format."""
    start_time = time.time()
    logging.info("Starting conversion of model to gguf format...")

    os.makedirs(quantized_model_path, exist_ok=True)

    try:
        subprocess.run(
            [
                "python",
                "./llama.cpp/convert_hf_to_gguf.py",
                original_model_path,
                "--outtype",
                "f16",
                "--outfile",
                f"{quantized_model_path}/FP16.gguf",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.decode() if e.stderr else str(e)
        logging.error(f"Error during model conversion: {error_message}")
        return

    end_time = time.time()
    logging.info(
        f"Finished conversion of model to gguf format in {end_time - start_time:.2f} seconds."
    )


def main(quantized_model_path, method):
    """Main function to handle the model quantization process."""

    start_time = time.time()
    logging.info("Starting the model quantization process...")

    # Quantize the Model
    quantize_model(quantized_model_path, method)

    end_time = time.time()
    logging.info(
        f"Finished the model quantization process in {end_time - start_time:.2f} seconds."
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Quantize a model using llama.cpp")
    parser.add_argument(
        "--original_model_path",
        type=str,
        required=True,
        help="Path to the original model",
    )
    parser.add_argument(
        "--quantized_model_path",
        type=str,
        required=True,
        help="Path to save the quantized model",
    )
    parser.add_argument(
        "--method", type=str, required=True, help="Quantization method to use"
    )

    args = parser.parse_args()

    if not os.path.exists(args.quantized_model_path):
        os.makedirs(args.quantized_model_path, exist_ok=True)

    main(args.original_model_path, args.quantized_model_path, args.method)

    # Delete the model_download folder if it exists
    if os.path.exists(args.original_model_path):
        shutil.rmtree(args.original_model_path)
