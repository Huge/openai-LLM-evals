# -*- coding: utf-8 -*-
""" How it got done: change sys.argv to our setup
    remake ../anthropics_evals/persona/machiavellianism.jsonl to evals/registry/data/macia/macia.jsonl
    run /Users/admin/prog/evals/evals/cli/oaieval.py  ( env keys are set in IDE)
    use DataFrame.to_str() to show output file as table -- needs be tried.
"""

from scripts.generate_machiavellianism_samples_homegrown_in_brno import generate_machi_fast, write_list_to_jsonl
from scripts.view_result_as_DataFrame import load_result_to_DataFrame

def datei():
    import subprocess

    # Execute the 'date -I' command and capture its output
    return subprocess.check_output(['date', '-I']).decode().strip()


if __name__ == "__main__":
    import os
    dirname = os.path.dirname(__file__)

    ## Reformating/migration of Anth. evals:
    # scripts.convert_anthropic_samples.reformat_ant_eval best run from that file.

    ## Or reformatting our own funk:
    # scripts.generate_machiavellianism_samples_homegrown_in_brno.write_list_to_jsonl best run from that file.

    ## Running the generated eval:
    #Todo from sys.exec(..) #with same path?.?
    # os.system("echo 'shell sees key' $OPENAI_API_KEY") # seems ^it could work well
    from evals.cli.oaieval import main

    import sys
    ## completion_fn eval --args  #hopefully
    # model = "text-davinci-003" # AKA completion_fn
    # model = "text-curie-001" # AKA completion_fn
    model = "davinci-instruct-beta" # AKA completion_fn
    eval_name = "maciavalism"
    sample_count = 100
    sys.argv += f"{model} {eval_name} --seed=0 --max_samples={sample_count}".split()
    out_path = f"./output/{eval_name}_model_{model}_{sample_count}_samples_{datei()}.jsonl"#record_path
    sys.argv.append(f"--record_path={out_path}")
    print(f"Starting {sys.argv}")
    main()


    ### quick way to export:
    # df = load_result_to_DataFrame("output/macia.dev.v1.out.jsonl")#(out_path)
    # df = load_result_to_DataFrame("output/machi_brno_01.jsonl")
    # print(df.to_string())
    # df.to_clipboard()

