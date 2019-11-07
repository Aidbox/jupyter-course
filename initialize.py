import json
import sys
import os
import os.path


async def import_bundle(client, filename):
    with open(filename) as fd:
        patient_json = json.load(fd)
    bundle = client.resource('Bundle')
    bundle['type'] = 'transaction'
    bundle['entry'] = patient_json['entry']
    await bundle.save()


async def import_dataset(client, dataset_path):
    sys.stdout.write("Import progress: 0%   \r")
    
    filenames = [
        filename for filename in os.listdir(dataset_path)
        if filename.endswith('.json')]

    total_count = len(filenames)
    for index, filename in enumerate(filenames):
        await import_bundle(client, os.path.join(dataset_path, filename))
        progress = int(float(index + 1) / float(total_count) * 100)
        sys.stdout.write("Import progress: %d%%   \r" % progress)
        sys.stdout.flush()
    sys.stdout.write("Import progress: 100%\n")
    sys.stdout.write("{0} bundles imported".format(total_count))
