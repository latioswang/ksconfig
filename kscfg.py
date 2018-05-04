from libkscfg import *
import sys
import glog as log

if __name__ == "__main__":
    source = ''
    with open(sys.argv[1], 'r') as config_file:
        source = config_file.read()
    code = compile(source, sys.argv[1], "exec")
    exec(code)
    export_json = getExportJson()
    assert export_json, "Have you called exportIfLast(proto_message) ? "
    json_path = cfgPathToJsonPath(sys.argv[1])
    with open(json_path, "w") as json_file:
        json_file.write(export_json)
    log.info(f"Successfully generated: {json_path}")

