import sys
sys.path.append("./src/AI_files")
from punctuator import Punctuator
def punctuator_src_test():
    loc = "./src/AI_files/punctuator/Demo-Europarl-EN.pcl"
    p = Punctuator(loc)
    punctuated_converse = p.punctuate("some one")
    return punctuated_converse
def test():
    punctuated_conv = punctuator_src_test()
    expected_conv = "Some one."
    if punctuated_conv == expected_conv:
        print("Test Passed")
    print("Actual sentence: " + punctuated_conv + "    ---->   " + "Expected sentence: " + expected_conv)
test()