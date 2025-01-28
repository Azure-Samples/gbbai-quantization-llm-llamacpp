import mlflow
from mlflow.models.signature import ModelSignature
from mlflow.types import Schema, ColSpec, DataType
from mlflow.types.schema import ColSpec, ParamSchema, ParamSpec, Schema


def text_generation(code_path, model_path, conda_path):
    input_schema = Schema([ColSpec(DataType.string, "text", False)])
    output_schema = Schema([ColSpec(DataType.string, None, False)])
    params_schema = ParamSchema(
    [
        ParamSpec("max_tokens", "integer", 32),
        ParamSpec("max_length", "long", 30),
        ParamSpec("temperature", "double", 0.62),
    ]
)   
    sign = ModelSignature(input_schema, output_schema, params_schema)
    print(f"text-generation task: Model signature={sign}", flush=True)
    mlflow.set_experiment("custom_llamacpp")
    mlflow.pyfunc.log_model(
        "model",
        loader_module="custom_loader.chat_loader",
        data_path=model_path,
        code_path=[code_path],#["/home/azureuser/cloudfiles/code/Users/karinaa/fine-tuning-text-to-sql/src/core/custom_loader"],
        signature=sign,
        conda_env=conda_path#"conda.yaml",
    )

def tracking_mlflow_model(code_path, model_path, conda_path):
    with mlflow.start_run():
        text_generation(code_path, model_path, conda_path)
