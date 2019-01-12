import numpy

numZeroesForLabel = [ [], [], [], [], [], [], [], [], [], [] ]
numOnesTwosForLabel = [ [], [], [], [], [], [], [], [], [], [] ]
instancesOfLabel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
priorProb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # An array that holds the prior probability for each label, i.e. P(label = 0) is held in slot 0
probPixelIsZero = [ [], [], [], [], [], [], [], [], [], [] ] # An array that holds the conditional probabilities that a pixel is zero for a given label
probPixelIsOneTwo = [ [], [], [], [], [], [], [], [], [], [] ] # An array that holds all conditional probabilities for ones and twos

'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)


'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
    features=[]

    for rowIndex, row in enumerate(digit_data):
        for colIndex, col in enumerate(row):
            # Get the pixel
            if digit_data[rowIndex][colIndex] == 0:
                features.append(False)
            else:
                features.append(True)
    #_raise_not_defined()

    return features

'''
Extract advanced features that you will come up with 
'''
def extract_advanced_features(digit_data, width, height, input_features=[]):

    features = input_features[:]
    if len(features) == 0:
        for x in range(height*width):
            if x % 2 == 0:
                features.append(True)
            else:
                features.append(False)  

    rowLimit = 6
    counter = 0

    for rowIndex, row in enumerate(digit_data):
        counter = 0
        for colIndex, col in enumerate(row):
            # See if amount of 1s/2s in row surpasses "limit"
            if digit_data[rowIndex][colIndex] != 0:
                counter += 1

        if counter >= rowLimit:
            features[rowIndex] = True
        else:
            features[colIndex] = True


    OnesAndTwos = 0
    leftMost = width
    topMost = height
    topHalfOneAndTwo = 0

    # Calculating the width and height of the digit
    # Calculating the number of 1's and 2's in the top half
    for index, item in enumerate(digit_data):

        row = digit_data[index]

        for pixelIndex, pixel in enumerate(row):
            if row[pixelIndex] != 0:
                OnesAndTwos += 1
                if (pixelIndex < leftMost):
                    leftMost = pixelIndex
                if (index < topMost):
                    topMost = index
                if index <= (len(digit_data) + 1) / 2:
                    topHalfOneAndTwo += 1
            
    digitWidth = width - (leftMost * 2)


    digitHeight = height - (topMost * 2)
    ratio = float(digitWidth) / digitHeight
        
    for n in range(10):
        if (ratio > 0.33):
            features[(n + 1) * 10] = True
        
    topHalf = float(topHalfOneAndTwo) / OnesAndTwos
    for n in range(5):
        if (topHalf > 0.35):
            features[-(n + 1) * 10] = True
    
    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):

    features = extract_basic_features(digit_data, width, height)

    features = extract_advanced_features(digit_data, width, height, features)

    return features

'''
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):

    #if feature_extractor == "extract_advanced_features":
    #    return 0

    global numZeroesForLabel
    global numOnesTwosForLabel
    global instancesOfLabel
    global priorProb
    global probPixelIsZero
    global probPixelIsOneTwo

    k = 0.075 # Smoothing constant

    # Initializing stuff
    for x in range(10):

        for y in range(width*height):

            numZeroesForLabel[x].append(0)
            numOnesTwosForLabel[x].append(0)
            probPixelIsZero[x].append(0)
            probPixelIsOneTwo[x].append(0)

    number = int((percentage * len(data))/100)

    tempFeatures = []

    for index in range(number):
        if label[index] == 0:
            instancesOfLabel[0] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # Particular pixel is zero
                    numZeroesForLabel[0][counter] += 1
                else:
                    numOnesTwosForLabel[0][counter] += 1

        elif label[index] == 1:
            instancesOfLabel[1] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[1][counter] += 1
                else:
                    numOnesTwosForLabel[1][counter] += 1

        elif label[index] == 2:
            instancesOfLabel[2] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[2][counter] += 1
                else:
                    numOnesTwosForLabel[2][counter] += 1

        elif label[index] == 3:
            instancesOfLabel[3] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[3][counter] += 1
                else:
                    numOnesTwosForLabel[3][counter] += 1

        elif label[index] == 4:
            instancesOfLabel[4] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[4][counter] += 1
                else:
                    numOnesTwosForLabel[4][counter] += 1

        elif label[index] == 5:
            instancesOfLabel[5] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[5][counter] += 1
                else:
                    numOnesTwosForLabel[5][counter] += 1

        elif label[index] == 6:
            instancesOfLabel[6] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[6][counter] += 1
                else:
                    numOnesTwosForLabel[6][counter] += 1

        elif label[index] == 7:
            instancesOfLabel[7] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[7][counter] += 1
                else:
                    numOnesTwosForLabel[7][counter] += 1

        elif label[index] == 8:
            instancesOfLabel[8] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[8][counter] += 1
                else:
                    numOnesTwosForLabel[8][counter] += 1

        else:
            instancesOfLabel[9] += 1

            tempFeatures = feature_extractor(data[index], width, height) # For conditional probability

            for counter, item in enumerate(tempFeatures):
                if item == False: # It's a zero
                    numZeroesForLabel[9][counter] += 1
                else:
                    numOnesTwosForLabel[9][counter] += 1

    # Compute all prior and conditional probabilities 
    for i in range(10):
        priorProb[i] = float(instancesOfLabel[i])/number

        for j in range(width*height):

            # Applying Laplace smoothing
            probPixelIsZero[i][j] = float(numZeroesForLabel[i][j] + k)/(numZeroesForLabel[i][j] + numOnesTwosForLabel[i][j] + 2*k)
            probPixelIsOneTwo[i][j] = float(numOnesTwosForLabel[i][j] + k)/(numZeroesForLabel[i][j] + numOnesTwosForLabel[i][j] + 2*k)

    #_raise_not_defined()

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    predicted = -1

    global priorProb
    global probPixelIsZero
    global probPixelIsOneTwo

    mostProbLabel = [] #List of probabilities for each label, given feature
    sumCondProb = []

    for label in range(10):
        prior = numpy.log(priorProb[label])

        for index, pixel in enumerate(features):
            if pixel == False: # It's a zero
                sumCondProb.append(numpy.log(probPixelIsZero[label][index]))
            else:
                sumCondProb.append(numpy.log(probPixelIsOneTwo[label][index]))

        mostProbLabel.append(prior + sum(sumCondProb))
        sumCondProb = []

    predicted = mostProbLabel.index(max(mostProbLabel))

    #_raise_not_defined()

    return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):

    predicted=[]

    for index in range(len(data)):

        tempFeatures = feature_extractor(data[index], width, height)
        predicted.append(compute_class(tempFeatures))

    #_raise_not_defined()

    return predicted
