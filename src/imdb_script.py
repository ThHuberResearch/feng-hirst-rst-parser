import os 
import shlex
import subprocess 
import parse
import time

def parse_imdb():
    src_dir = "../texts/IMDB/preprocessed/{}/{}"
    choice1 = ["test", "train"]
    choice2 = ["pos", "neg"]

    log_dir = "imdb_log.log"
    if os.path.exists(log_dir):
        os.remove(log_dir)
    flog = open(log_dir, "a+")

    for choice1 in ["test", "train"]:
        for choice2 in ["pos", "neg"]:
            for fname in os.listdir(src_dir.format(choice1, choice2)):
                start_time = time.time()
                full_fn = os.path.join(src_dir.format(choice1, choice2), fname)
                output_dir = "IMDB/{}/{}".format(choice1, choice2)
                cmd = "python parse.py -g -t {} {}".format(output_dir, full_fn)

                pipe = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    stdout, stderr = pipe.communicate(timeout=180)
                except subprocess.TimeoutExpired:
                    print ("RST parser timeout: {}".format(full_fn))
                    flog.write(full_fn + "\n")
                    flog.flush()
                    continue

                if len(stderr) > 0:
                    print ("Failed: {}".format(full_fn))
                    flog.write(full_fn + "\n")
                    flog.flush()
                else:
                    print ("Done:   {} in {:.2f} seconds".format(full_fn, time.time() - start_time))

    
    flog.close()

if __name__ == "__main__":
    parse_imdb()