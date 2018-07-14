import os
from time import time
from DataetInformation import DatasetInformation
from ComputeFeatures import ComputeFeatures


def main():
    # Start to count the time.
    t0 = time()



    # Load path to dataset from config file.
    # [0] is path to dataset.
    import ConfigParser, os

    config = ConfigParser.ConfigParser()
    config.read('_config.cfg')
    path_to_dataset = config.get('PATHS', 'path_to_dataset')

    # Create new instance.
    extract_features = ComputeFeatures()

    # Go throw all subset in dataset.
    index = 1
    for sub_set in os.listdir(path_to_dataset):
        if sub_set.startswith("."):
            continue
        print "--------------------------------------------------------"
        print "-------- #" + str(index) + " " + sub_set
        print "--------------------------------------------------------"
        extract_features.extraction_manager(path_to_dataset + sub_set + '/bro/')
        index += 1

    # Add certificate to connections that does not contain any certificate.
    extract_features.add_cert_to_non_cert_conn()

    # Compute features and save them.
    extract_features.create_dataset()
    # Print final statistic
    extract_features.print_statistic()
    # Extract_features.compute_features()
    extract_features.save_dataset_information()

    print "<<< All dataset successfully finished in aproximate time: %f" % ((time() - t0)/60.0) + " min."


if __name__ == '__main__':
   main()
