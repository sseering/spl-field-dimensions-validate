#!/usr/bin/env python3

import json
import sys
import os.path

import fastjsonschema


def main() -> None:
    exe_dir = os.path.dirname(sys.argv[0])
    with open(os.path.join(exe_dir, 'field-dimensions-schema.json'), mode="rt", encoding="utf8") as schema_in:
        field_dimensions_schema = json.load(schema_in)
    generated_code = fastjsonschema.compile_to_code(field_dimensions_schema)
    with open(os.path.join(exe_dir, '../autogenerated/validate.py'), mode="wt", encoding="utf8") as generated_code_out:
        generated_code_out.write(generated_code)

    print('done') 


if __name__ == "__main__":
    main()
