import imp
import subprocess
import os
import sys

import google.protobuf.json_format as json_format

sys.path.append("_python_pb")


def cfgPathToJsonPath(cfg_path: str):
    parts = cfg_path.split('.')[:-1] + ["json"]
    return ".".join(parts)

def protoToPythonPath(proto_path: str) -> tuple:
    assert proto_path.endswith(".proto")
    folder, proto_file = os.path.split(proto_path)
    without_extension = proto_file.replace(".proto", "")
    assert (not proto_path.startswith("/"))
    return f"_python_pb", f"_python_pb/{folder}/{without_extension}_pb2.py"


def importProto(proto_path):
    output_folder, python_path = protoToPythonPath(proto_path)
    # os.mkdir(output_folder)
    cmd = ['protoc', f'--python_out={output_folder}', proto_path]
    print(f"running {cmd}\n")
    subprocess.check_call(cmd)
    return imp.load_source(proto_path, python_path)


def importPython(python_path):
    return imp.load_source(python_path, python_path)


EXPORT_JSON = None


def getExportJson():
    global EXPORT_JSON
    return EXPORT_JSON


def exportIfLast(message):
    global EXPORT_JSON
    EXPORT_JSON = json_format.MessageToJson(message)
