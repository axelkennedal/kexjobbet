from extract import *
import glob
import sklearn.svm as svm
import numpy as np
import sys, os
import getopt
import copy

dataBaseDir = '../../../data/NNMD_out/'
printCFMatrix = False
nJobs = 1
offsetMode = OffsetMode.START
duration = 30

trainingData = { 'data': [], 'group': [] }
songHashGenreName = {}

## Main function
def main():
    global songHashGenreName
    global nJobs

    process_args()
    print(dataBaseDir)
    print(offsetMode)
    print("Snippet duration: " + str(duration) + " seconds")

    print('Extracting features...')
    ## Generate sample, feature vector matrix (training data)
    filenames = glob.glob(dataBaseDir + 'training/*.mp3')

    (trainingData, songHashGenreName) = generate_feature_vector(filenames, nJobs, offsetMode, duration)
    data = np.array(trainingData['data'])
    group = np.array(trainingData['group'])

    # np.save('songHashGenreName', songHashGenreName);
    # np.savetxt('mfccdata.dat', data, fmt = '%f')
    # np.savetxt('gdata.dat', group, fmt = '%d')
    # data = np.loadtxt('mfccdata.dat', dtype=float)
    # group = np.loadtxt('gdata.dat', dtype=int)
    # songHashGenreName = np.load('songHashGenreName.npy').item()

    print('\nTraining classifier...')
    # Generate classifier model
    classifier = svm.SVC(kernel = 'rbf', gamma = 3, C = 1, tol = 0.00001)
    classifier.fit(data, group)
    print('Score: %f' % classifier.score(data, group))

    # Get predict data
    print('Classifying data...')
    filenames = glob.glob(dataBaseDir + 'classify/*.mp3')
    (predictDataDict, _) = generate_feature_vector(filenames, nJobs, offsetMode, duration)
    predictGenre = np.array(predictDataDict['group'])
    predictData = np.array(predictDataDict['data'])

    # np.savetxt('predData.dat', predictData, fmt = '%f')
    # np.savetxt('predGroup.dat', predictGenre, fmt = '%d')
    # predictData = np.loadtxt('predData.dat', dtype=float)
    # predictGenre = np.loadtxt('predGroup.dat', dtype=int)

    result = classifier.predict(predictData)

    hit = 0
    for i in range(0, len(result)):
        if result[i] == predictGenre[i]:
            hit += 1

    if printCFMatrix:
        print_confusion_matrix(result, predictGenre)

    print("\n\nFinished classifying %d songs." % len(result))
    print("Accuracy {}% [{}/{}]".format(100 * hit / len(result), hit, len(result)))

##---------------------------------------------------------
##----------------------- Main end ------------------------
##---------------------------------------------------------
def print_help():
    print("Usage: ")
    print("    classify.py -h")
    print("    classify.py base_dir_path")
    print("    classify.py [OPTIONS]")
    print("    classify.py [OPTIONS] base_dir_path")
    print("\nOPTIONS:")
    print("    -h                           - prints this help text.")
    print("    -i, --input-dir              - data base directory")
    print("    -p, --print-confusion-matrix - prints the confusion matrix")
    print("    -j, --jobs                   - number of jobs to run in parallel")
    print("    -o, --offset-mode            - which OffsetMode to use; START, MIDDLE, END or RANDOM")
    print("    -d, --duration               - snippet duration")

def process_args():
    global dataBaseDir
    global printCFMatrix
    global nJobs
    global offsetMode
    global duration

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:pj:o:d:", ["jobs=", "input-dir=", "print-confusion-matrix", "offset-mode=", "duration="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    if len(args) > 1:
        print("Unknown argument!")
        sys.exit(1)

    elif len(args) == 1:
        path = args[0]
        if path[-1] != '/':
            path += '/'
        if os.path.isdir(path):
            dataBaseDir = path

    for (opt, arg) in opts:
        if opt == "-h":
            print_help()
            sys.exit()

        elif opt in ("-i", "--input-dir"):
            path = arg
            if path[-1] != '/':
                path += '/'
            if os.path.isdir(path):
                dataBaseDir = path

            else:
                sys.exit(1)

        elif opt in ("-p", "--print-confusion-matrix"):
            printCFMatrix = True

        elif opt in ("-j", "--jobs"):
            if int(arg) <= 0:
                print("Number of jobs must be greater than 0")
                sys.exit(1)

            nJobs = int(arg)

        elif opt in ("-o", "--offset-mode"):
            offsetMode = OffsetMode[arg]

        elif opt in ("-d", "--input-dir"):
            if int(arg) <= 0:
                print("Duration must be greater than 0")
                sys.exit(1)

            duration = int(arg)

        else:
            print("Unknown argument " + opt)
            sys.exit(1)

def print_confusion_matrix(classRes, expected):
    mat = {}
    totalGenre = {}

    for key in songHashGenreName:
        totalGenre.update({ key: 0 })

    for key in songHashGenreName:
        mat.update({key: copy.deepcopy(totalGenre)})

    for i in range(0, len(classRes)):
        key = classRes[i]
        mat[expected[i]][key] += 1


    print("Confusion matrix:\n")

    print("              ", end="")
    for genre in songHashGenreName:
        print("{:>12}  ".format(songHashGenreName[genre]), end="")

    for actual in mat:
        print("\n{:>12} ".format(songHashGenreName[actual]), end="")

        for pred in songHashGenreName:
            print("{:>12} ".format(mat[actual][pred]), end="")

    print("")


if __name__  == '__main__':
    main()
